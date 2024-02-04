#imports and app initialization
from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI
import pymysql

app = Flask(__name__)

weightedTotalCredits = []
unweightedTotalCredits = []

#instantiating database object and conection to AWS SQL DB
db = pymysql.connect(host='gpa-db.c38eckgmktvd.us-east-2.rds.amazonaws.com', user='admin', password='200723Sd!', db='gpaData')
cursor = db.cursor()

classId = 1

#takes user input and calculates the credit that they would recieve for it
def calculate_grades(counter, class_data):
    global weightedTotalCredits, unweightedTotalCredits, classId

    grades, classTypes, classNames, weightedGrades, unWeightedGrades = [], [], [], [], []

    print(class_data)

    #validates the data the user inputs
    for i in range(1, counter + 1):
        classType = str(class_data["class-" + str(i)])
        className = class_data["name-" + str(i)]
        gradeLevel = class_data["grade-level-" + str(i)]
        try:
            classGrade = int(class_data["grade-" + str(i)])
        except:
            return None, None, None, "Grade must be a number"
        if 0 <= classGrade <= 100:
            classTypes.append(classType)
            grades.append(classGrade)
            classNames.append(className)
        else:
            return None, None, None, "Grade must be between 0 - 100!"


    #converts grades to weighted credits
    for i in range(len(grades)):
        if classTypes[i] == "credit5":
            if grades[i] >= 90:
                weightedGrades.append(5)
            elif grades[i] >= 80:
                weightedGrades.append(4)
            elif grades[i] >= 70:
                weightedGrades.append(3)
            else:
                weightedGrades.append(0)
        else:
            if grades[i] >= 90:
                weightedGrades.append(4)
            elif grades[i] >= 80:
                weightedGrades.append(3)
            elif grades[i] >= 70:
                weightedGrades.append(2)
            else:
                weightedGrades.append(0)

    if len(weightedGrades) == 0:
        return None, None, None, "You must enter at least 2 grades to calculate!"

    weightedTotalCredits += weightedGrades
    CWgpa = sum(weightedTotalCredits) / len(weightedTotalCredits)

    #converts grades to unweighted credits
    for i in range(0, len(grades)):
        if (grades[i] >= 90):
            unWeightedGrades.append(4)
        elif (grades[i] >= 80):
            unWeightedGrades.append(3)
        elif (grades[i] >= 70):
            unWeightedGrades.append(2)
        else:
            unWeightedGrades.append(0)

    unweightedTotalCredits += unWeightedGrades
    CUgpa = sum(unweightedTotalCredits) / len(unweightedTotalCredits)

    totalClasses = len(grades)

    #stores data in database
    sql = """insert into `ClassInfo` (classId, className, classCreditWeighted, 
                                    classCreditUnweighted, classType, classGradeLevel)
            values (%s, %s, %s, %s, %s, %s) 
        """
    for i in range(0, len(grades)):
        cursor.execute(sql, (classId, classNames[i], weightedGrades[i], unWeightedGrades[i], classTypes[i], gradeLevel))
        db.commit()
        classId+=1


    return CWgpa, CUgpa, totalClasses, None

#returns the template with an error message
def render_template_with_error(template, error=None, **kwargs):
    return render_template(template, error=error, **kwargs)

#takes the date from the grade calculation and outputs it to the user
def process_grade_route(route, template):
    global weightedTotalCredits, unweightedTotalCredits

    
    if request.method == "POST":
        #stores class type
        counter = int(request.form.get("counter"))

        class_data = {
            f"class-{i}": request.form.get(f"class-{i}") 
            for i in range(1, counter + 1)
        }

        #stores grades for each class
        class_data.update(
            {
                f"grade-{i}": request.form.get(f"grade-{i}") 
                for i in range(1, counter + 1)
            }
        )

        #stores class name
        class_data.update(
            {
                f"name-{i}": request.form.get(f"name-{i}") 
                for i in range(1, counter + 1)
            }
        )

        #stores grade-level
        class_data.update(
            {
                f"grade-level-{i}": request.form.get(f"grade-level-{i}") 
                for i in range(1, counter + 1)
            }
        )



        CWgpa, CUgpa, totalClasses, error = calculate_grades(counter, class_data)

        if error:
            return render_template_with_error(template, error=error)

        return render_template(template, totalW=CWgpa, totalU=CUgpa, totalClasses=totalClasses)
    else:
        return render_template(template)

#checks if the input to the AI assisstant is relvant to GPA calculation
def isRelevant(question):
    question = question.lower()
    keywords = ['gpa', 'grade point average', 'grade average', 'calculate', 'calculate gpa', 'how to calculate gpa', 'grades', 'increase']

    for i in keywords:
        if i in question:
            return True
        
    return False

#sends a request to the ChatGPT API and recieves a result
def chatgpt_api_request(question):

    client = OpenAI(
        api_key="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",
    )
    role = "You are a interactive question and answer chatbot that should respond to user question about GPA and how it is calculated. You're response should be less than 50 words. Be sure to say something happy and cheerful in the beginning such as 'Hello, happy to help', etc."
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": role,

            },
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content

#User inputs the grade and returns a result to the user with ChatGPT output
@app.route('/chatbot', methods=["GET", "POST"])
def ask_question():
    question = request.form.get("question")
    if request.method == "POST":

        if question == None:
            return render_template('chatbot.html', response="Please ask a question!", question=question)

        if isRelevant(question):
            response = chatgpt_api_request(question)
            return render_template('chatbot.html', response=response, question=question)
        else:
            return render_template('chatbot.html', response="Sorry, I can only respond to relevant questions.", question=question)
    else:
        return render_template('chatbot.html', response="Ask me anything!")
    
#the user routes
@app.route('/')
def home():
    return redirect(url_for('NinthGradeGPA'))

@app.route('/ninth-grade-gpa', methods=["GET", "POST"])
def NinthGradeGPA():
    return process_grade_route('NinthGradeGPA', "ninth.html")

@app.route('/tenth-grade-gpa', methods=["GET", "POST"])
def tenthGradeGPA():
    return process_grade_route('tenthGradeGPA', "tenth.html")

@app.route('/eleventh-grade-gpa', methods=["GET", "POST"])
def eleventhGradeGPA():
    return process_grade_route('eleventhGradeGPA', "eleventh.html")

@app.route('/twelfth-grade-gpa', methods=["GET", "POST"])
def twelfthGradeGPA():
    return process_grade_route('twelfthGradeGPA', "twelfth.html")

@app.route('/about-us', methods=["GET", "POST"])
def AboutUs():
    return render_template('aboutus.html')





if __name__ == '__main__':
    app.run(debug=True)
