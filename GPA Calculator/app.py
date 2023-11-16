from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


weightedTotalCredits = []
unweightedTotalCredits = []
weightedGpa9 = ""
unWeightedGpa9 = ""
weightedGpa10 = ""
unWeightedGpa10 = ""
weightedGpa11 = ""
unWeightedGpa11 = ""

@app.route('/')
def home():
    return redirect(url_for('NinthGradeGPA'))

@app.route('/ninth-grade-gpa', methods =["GET", "POST"])

def NinthGradeGPA():
    global weightedTotalCredits
    global unweightedTotalCredits
    global weightedGpa9
    global unWeightedGpa9
    if request.method == "POST":
        counter = int(request.form.get("counter"))
        
        classType = ""
        classGrade = 0
        grades = []
        classTypes = []
        weightedGrades = []
        unWeightedGrades = []
        for i in range(1, counter+1):
            classType = request.form.get("class-"+str(i)).lower() 
            try:
                classGrade = int(request.form.get("grade-"+str(i)))
            except:
                return render_template("ninth.html", error="Must enter a valid grade")
            if (classType != "" and classGrade != ""):
                if ((classType == "ap" or classType == "ib" or classType == "dual" or classType == "regular" or classType == "honors") and (classGrade >= 0 and classGrade <= 100)):
                    classTypes.append(classType)
                    grades.append(classGrade)
                
                else: 
                   return render_template("ninth.html", error="Invalid class type or invalid grade!")
            else:
                continue


        for i in range(0, len(grades)):
            if (classTypes[i] == "ap" or classTypes[i] == "ib" or classTypes[i] == "dual"):
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
            return render_template("ninth.html", error="You must enter atleast 2 grades to calculate!")

        weightedGpa9 = sum(weightedGrades)/len(weightedGrades)
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

        unWeightedGpa9 = sum(unWeightedGrades)/len(unWeightedGrades)
        unweightedTotalCredits = unweightedTotalCredits + unWeightedGrades
        CUgpa = sum(unweightedTotalCredits)/len(unweightedTotalCredits)
        return render_template("ninth.html", ninth=str(weightedGpa9) + " " + str(unWeightedGpa9), totalW=CWgpa, totalU = CUgpa)
    else:
        return render_template("ninth.html")

@app.route('/tenth-grade-gpa', methods =["GET", "POST"])
def tenthGradeGPA():
    global weightedTotalCredits
    global unweightedTotalCredits
    global weightedGpa9
    global unWeightedGpa9
    global weightedGpa10
    global unWeightedGpa10
    if request.method == "POST":
        counter = int(request.form.get("counter"))
        
        classType = ""
        classGrade = 0
        grades = []
        classTypes = []
        weightedGrades = []
        unWeightedGrades = []
        for i in range(1, counter+1):
            classType = request.form.get("class-"+str(i)).lower()
            try:
                classGrade = int(request.form.get("grade-"+str(i)))
            except:
                return render_template("ninth.html", error="Must enter a valid grade")
            if (classType != "" and classGrade != ""):
                if ((classType == "ap" or classType == "ib" or classType == "dual" or classType == "regular" or classType == "honors") and (classGrade >= 0 and classGrade <= 100)):
                    classTypes.append(classType)
                    grades.append(classGrade)
                
                else: 
                   return render_template("tenth.html", error="Invalid class type or invalid grade!")
            else:
                continue


        for i in range(0, len(grades)):
            if (classTypes[i] == "ap" or classTypes[i] == "ib" or classTypes[i] == "dual"):
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

        weightedGpa10 = sum(weightedGrades)/len(weightedGrades)
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

        unWeightedGpa10 = sum(unWeightedGrades)/len(unWeightedGrades)
        unweightedTotalCredits = unweightedTotalCredits + unWeightedGrades
        CUgpa = sum(unweightedTotalCredits)/len(unweightedTotalCredits)

        return render_template("tenth.html", ninth=str(weightedGpa9) + " " + str(unWeightedGpa9), tenth=str(weightedGpa10) + " " + str(unWeightedGpa10), totalW=CWgpa, totalU = CUgpa)
    else:
        return render_template("tenth.html")
    
    
@app.route('/eleventh-grade-gpa', methods =["GET", "POST"])
def eleventhGradeGPA():
    global weightedTotalCredits
    global unweightedTotalCredits
    global weightedGpa9
    global unWeightedGpa9
    global weightedGpa10
    global unWeightedGpa10
    global weightedGpa11
    global unWeightedGpa11

    if request.method == "POST":
        counter = int(request.form.get("counter"))
        
        classType = ""
        classGrade = 0
        grades = []
        classTypes = []
        weightedGrades = []
        unWeightedGrades = []
        for i in range(1, counter+1):
            classType = request.form.get("class-"+str(i)).lower()
            try:
                classGrade = int(request.form.get("grade-"+str(i)))
            except:
                return render_template("ninth.html", error="Must enter a valid grade")
            if (classType != "" and classGrade != ""):
                if ((classType == "ap" or classType == "ib" or classType == "dual" or classType == "regular" or classType == "honors") and (classGrade >= 0 and classGrade <= 100)):
                    classTypes.append(classType)
                    grades.append(classGrade)
                
                else: 
                   return render_template("eleventh.html", error="Invalid class type or invalid grade!")
            else:
                continue


        for i in range(0, len(grades)):
            if (classTypes[i] == "ap" or classTypes[i] == "ib" or classTypes[i] == "dual"):
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

        weightedGpa11 = sum(weightedGrades)/len(weightedGrades)
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

        unWeightedGpa11 = sum(unWeightedGrades)/len(unWeightedGrades)
        unweightedTotalCredits = unweightedTotalCredits + unWeightedGrades
        CUgpa = sum(unweightedTotalCredits)/len(unweightedTotalCredits)
        

        return render_template("eleventh.html", ninth=str(weightedGpa9) + " " + str(unWeightedGpa9), tenth=str(weightedGpa10) + " " + str(unWeightedGpa10), eleventh = str(weightedGpa11) + " " + str(unWeightedGpa11), totalW=CWgpa, totalU = CUgpa)
    else:
        return render_template("eleventh.html")

@app.route('/twelfth-grade-gpa', methods =["GET", "POST"])
def twelfthGradeGPA():
    global weightedTotalCredits
    global unweightedTotalCredits
    global weightedGpa9
    global unWeightedGpa9
    global weightedGpa10
    global unWeightedGpa10
    global weightedGpa11
    global unWeightedGpa11

    if request.method == "POST":
        counter = int(request.form.get("counter"))
        
        classType = ""
        classGrade = 0
        grades = []
        classTypes = []
        weightedGrades = []
        unWeightedGrades = []
        for i in range(1, counter+1):
            classType = request.form.get("class-"+str(i)).lower()
            try:
                classGrade = int(request.form.get("grade-"+str(i)))
            except:
                return render_template("ninth.html", error="Must enter a valid grade")
            if (classType != "" and classGrade != ""):
                if ((classType == "ap" or classType == "ib" or classType == "dual" or classType == "regular" or classType == "honors") and (classGrade >= 0 and classGrade <= 100)):
                    classTypes.append(classType)
                    grades.append(classGrade)
                
                else: 
                   return render_template("twelfth.html", error="Invalid class type or invalid grade!")
            else:
                continue


        for i in range(0, len(grades)):
            if (classTypes[i] == "ap" or classTypes[i] == "ib" or classTypes[i] == "dual"):
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
        
        weightedGpa12 = sum(weightedGrades)/len(weightedGrades)
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

        unWeightedGpa12 = sum(unWeightedGrades)/len(unWeightedGrades)
        unweightedTotalCredits = unweightedTotalCredits + unWeightedGrades
        CUgpa = sum(unweightedTotalCredits)/len(unweightedTotalCredits)
        

        return render_template("twelfth.html", ninth=str(weightedGpa9) + " " + str(unWeightedGpa9), tenth=str(weightedGpa10) + " " + str(unWeightedGpa10), eleventh = str(weightedGpa11) + " " + str(unWeightedGpa11), twelfth = str(weightedGpa12) + " " + str(unWeightedGpa12), totalW=CWgpa, totalU = CUgpa)
    else:
        return render_template("twelfth.html")


if __name__ == '__main__':
    app.run(debug=True)
