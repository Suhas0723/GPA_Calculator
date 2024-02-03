from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask application
app = Flask(__name__)

# Lists to hold total credits for weighted and unweighted GPAs
weightedTotalCredits = []
unweightedTotalCredits = []

@app.route('/')
def home():
    #Redirect from home page to the ninth-grade GPA calculator page
    return redirect(url_for('NinthGradeGPA'))

@app.route('/ninth-grade-gpa', methods =["GET", "POST"])
def NinthGradeGPA():
    #Declare global variables to modify them within the function
    global weightedTotalCredits
    global unweightedTotalCredits

    if request.method == "POST":
        #Number of classes
        counter = int(request.form.get("counter"))
        #Initialize local variables for processing form data
        classType = ""
        classGrade = 0
        grades = [] #Store numerical grades
        classTypes = [] #Store types of classes
        weightedGrades = [] #Calculated weighted grades
        unWeightedGrades = [] #Calculated unweighted grades

        #Iterate over the classes based on the counter provided
        for i in range(1, counter+1):
            classType = str(request.form.get("class-"+str(i)))
            try:
                classGrade = int(request.form.get("grade-"+str(i)))
            except:
                #Return error if grade is not a valid number
                return render_template("ninth.html", error="Must enter a valid grade")
            #Validate grade and class type
            if (classType != "" and classGrade != ""):
                if (classGrade >= 0 and classGrade <= 100):
                    classTypes.append(classType)
                    grades.append(classGrade)
                else: 
                   return render_template("ninth.html", error="Grade must be between 0 - 100!")
            else:
                continue
        #Calculate weighted grades based on class type and grade
        for i in range(0, len(grades)):
            if (classTypes[i] == "credit5"):
                if (grades[i] >= 90):
                    weightedGrades.append(5)
                elif (grades[i] >= 80):
                    weightedGrades.append(4)
                elif (grades[i] >= 70):
                    weightedGrades.append(3)
                else:
                    weightedGrades.append(0)
            else:
                if (grades[i] >= 90):
                    weightedGrades.append(4)
                elif (grades[i] >= 80):
                    weightedGrades.append(3)
                elif (grades[i] >= 70):
                    weightedGrades.append(2)
                else:
                    weightedGrades.append(0)
                    
        #Ensure there are grades to calculate GPA
        if len(weightedGrades) == 0:
            return render_template("ninth.html", error="You must enter atleast 2 grades to calculate!")
        #Update and calculate cumulative weighted GPA
        weightedTotalCredits = weightedTotalCredits + weightedGrades
        CWgpa = sum(weightedTotalCredits)/len(weightedTotalCredits)
        
#Loop through each grade in the 'grades' list to calculate unweighted GPA scores
        for i in range(0, len(grades)):
            if (grades[i] >= 90):
                unWeightedGrades.append(4)
            elif (grades[i] >= 80):
                unWeightedGrades.append(3)
            elif (grades[i] >= 70):
                unWeightedGrades.append(2)
            else:
                unWeightedGrades.append(0)
                
#Calculate the Cumulative Unweighted GPA
        unweightedTotalCredits = unweightedTotalCredits + unWeightedGrades
        CUgpa = sum(unweightedTotalCredits)/len(unweightedTotalCredits)

        return render_template("ninth.html", totalW=CWgpa, totalU = CUgpa)
    else:
        return render_template("ninth.html")

@app.route('/tenth-grade-gpa', methods =["GET", "POST"])
def tenthGradeGPA():
    global weightedTotalCredits
    global unweightedTotalCredits

    if request.method == "POST":
        counter = int(request.form.get("counter"))
        classType = ""
        classGrade = 0
        grades = []
        classTypes = []
        weightedGrades = []
        unWeightedGrades = []
        for i in range(1, counter+1):
            classType = str(request.form.get("class-"+str(i)))
            try:
                classGrade = int(request.form.get("grade-"+str(i)))
            except:
                return render_template("tenth.html", error="Must enter a valid grade")
            if (classType != "" and classGrade != ""):
                if (classGrade >= 0 and classGrade <= 100):
                    classTypes.append(classType)
                    grades.append(classGrade)
                else: 
                   return render_template("tenth.html", error="Grade must be between 0 - 100!")
            else:
                continue
        for i in range(0, len(grades)):
            if (classTypes[i] == "credit5"):
                if (grades[i] >= 90):
                    weightedGrades.append(5)
                elif (grades[i] >= 80):
                    weightedGrades.append(4)
                elif (grades[i] >= 70):
                    weightedGrades.append(3)
                else:
                    weightedGrades.append(0)
            else:
                if (grades[i] >= 90):
                    weightedGrades.append(4)
                elif (grades[i] >= 80):
                    weightedGrades.append(3)
                elif (grades[i] >= 70):
                    weightedGrades.append(2)
                else:
                    weightedGrades.append(0)

        if len(weightedGrades) == 0:
            return render_template("tenth.html", error="You must enter atleast 2 grades to calculate!")

        weightedTotalCredits = weightedTotalCredits + weightedGrades
        CWgpa = sum(weightedTotalCredits)/len(weightedTotalCredits)

        for i in range(0, len(grades)):
            if (grades[i] >= 90):
                unWeightedGrades.append(4)
            elif (grades[i] >= 80):
                unWeightedGrades.append(3)
            elif (grades[i] >= 70):
                unWeightedGrades.append(2)
            else:
                unWeightedGrades.append(0)

        unweightedTotalCredits = unweightedTotalCredits + unWeightedGrades
        CUgpa = sum(unweightedTotalCredits)/len(unweightedTotalCredits)

        return render_template("tenth.html", totalW=CWgpa, totalU = CUgpa)
    else:
        return render_template("tenth.html")

    
    
@app.route('/eleventh-grade-gpa', methods =["GET", "POST"])
def eleventhGradeGPA():
    global weightedTotalCredits
    global unweightedTotalCredits

    if request.method == "POST":
        counter = int(request.form.get("counter"))
        classType = ""
        classGrade = 0
        grades = []
        classTypes = []
        weightedGrades = []
        unWeightedGrades = []
        for i in range(1, counter+1):
            classType = str(request.form.get("class-"+str(i)))
            try:
                classGrade = int(request.form.get("grade-"+str(i)))
            except:
                return render_template("eleventh.html", error="Must enter a valid grade")
            if (classType != "" and classGrade != ""):
                if (classGrade >= 0 and classGrade <= 100):
                    classTypes.append(classType)
                    grades.append(classGrade)
                else: 
                   return render_template("eleventh.html", error="Grade must be between 0 - 100!")
            else:
                continue
        for i in range(0, len(grades)):
            if (classTypes[i] == "credit5"):
                if (grades[i] >= 90):
                    weightedGrades.append(5)
                elif (grades[i] >= 80):
                    weightedGrades.append(4)
                elif (grades[i] >= 70):
                    weightedGrades.append(3)
                else:
                    weightedGrades.append(0)
            else:
                if (grades[i] >= 90):
                    weightedGrades.append(4)
                elif (grades[i] >= 80):
                    weightedGrades.append(3)
                elif (grades[i] >= 70):
                    weightedGrades.append(2)
                else:
                    weightedGrades.append(0)

        if len(weightedGrades) == 0:
            return render_template("eleventh.html", error="You must enter atleast 2 grades to calculate!")

        weightedTotalCredits = weightedTotalCredits + weightedGrades
        CWgpa = sum(weightedTotalCredits)/len(weightedTotalCredits)

        for i in range(0, len(grades)):
            if (grades[i] >= 90):
                unWeightedGrades.append(4)
            elif (grades[i] >= 80):
                unWeightedGrades.append(3)
            elif (grades[i] >= 70):
                unWeightedGrades.append(2)
            else:
                unWeightedGrades.append(0)

        unweightedTotalCredits = unweightedTotalCredits + unWeightedGrades
        CUgpa = sum(unweightedTotalCredits)/len(unweightedTotalCredits)

        return render_template("eleventh.html", totalW=CWgpa, totalU = CUgpa)
    else:
        return render_template("eleventh.html")

@app.route('/twelfth-grade-gpa', methods =["GET", "POST"])
def twelfthGradeGPA():
    global weightedTotalCredits
    global unweightedTotalCredits

    if request.method == "POST":
        counter = int(request.form.get("counter"))
        classType = ""
        classGrade = 0
        grades = []
        classTypes = []
        weightedGrades = []
        unWeightedGrades = []
        for i in range(1, counter+1):
            classType = str(request.form.get("class-"+str(i)))
            try:
                classGrade = int(request.form.get("grade-"+str(i)))
            except:
                return render_template("twelfth.html", error="Must enter a valid grade")
            if (classType != "" and classGrade != ""):
                if (classGrade >= 0 and classGrade <= 100):
                    classTypes.append(classType)
                    grades.append(classGrade)
                else: 
                   return render_template("twelfth.html", error="Grade must be between 0 - 100!")
            else:
                continue
            
        for i in range(0, len(grades)):
            if (classTypes[i] == "credit5"):
                if (grades[i] >= 90):
                    weightedGrades.append(5)
                elif (grades[i] >= 80):
                    weightedGrades.append(4)
                elif (grades[i] >= 70):
                    weightedGrades.append(3)
                else:
                    weightedGrades.append(0)
            else:
                if (grades[i] >= 90):
                    weightedGrades.append(4)
                elif (grades[i] >= 80):
                    weightedGrades.append(3)
                elif (grades[i] >= 70):
                    weightedGrades.append(2)
                else:
                    weightedGrades.append(0)

        if len(weightedGrades) == 0:
            return render_template("twelfth.html", error="You must enter atleast 2 grades to calculate!")

        weightedTotalCredits = weightedTotalCredits + weightedGrades
        CWgpa = sum(weightedTotalCredits)/len(weightedTotalCredits)

        for i in range(0, len(grades)):
            if (grades[i] >= 90):
                unWeightedGrades.append(4)
            elif (grades[i] >= 80):
                unWeightedGrades.append(3)
            elif (grades[i] >= 70):
                unWeightedGrades.append(2)
            else:
                unWeightedGrades.append(0)

        unweightedTotalCredits = unweightedTotalCredits + unWeightedGrades
        CUgpa = sum(unweightedTotalCredits)/len(unweightedTotalCredits)

        return render_template("twelfth.html", totalW=CWgpa, totalU = CUgpa)
    else:
        return render_template("twelfth.html")


if __name__ == '__main__':
    app.run(debug=True)
