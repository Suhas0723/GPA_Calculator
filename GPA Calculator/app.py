from flask import Flask, render_template, request


app = Flask(__name__)

CWgpa = []
CUgpa = []
weightedGpa9 = ""
unWeightedGpa9 = ""
weightedGpa10 = ""
unWeightedGpa10 = ""
weightedGpa11 = ""
unWeightedGpa11 = ""

@app.route('/ninth-grade-gpa', methods =["GET", "POST"])
def NinthGradeGPA():
    global CWgpa
    global CUgpa
    global weightedGpa9
    global unWeightedGpa9
    if request.method == "POST":
        counter = int(request.form.get("counter"))
        
        classType = ""
        classGrade = 0
        grades = []
        classTypes = []
        weightedGrades = []
        unweightedGrades = []
        for i in range(1, counter+1):
            classType = request.form.get("class-"+str(i)).lower()
            classGrade = int(request.form.get("grade-"+str(i)))
            if (classType != "" and classGrade != ""):
                if ((classType == "ap" or classType == "ib" or classType == "dual" or classType == "regular" or classType == "honors") and (classGrade >= 0 and classGrade <= 100)):
                    classTypes.append(classType)
                    grades.append(classGrade)
                
                else: 
                   return render_template("ninth.html", error="Invalid class type!")
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
        CWgpa.append(weightedGpa9)


        for i in range(0, len(grades)):
            if (grades[i] >= 90):
                unweightedGrades.append(4)
            elif (grades[i] >= 80):
                unweightedGrades.append(3)
            elif (grades[i] >= 70):
                unweightedGrades.append(2)
            else:
                unweightedGrades.append(0)

        unWeightedGpa9 = sum(unweightedGrades)/len(unweightedGrades)
        CUgpa.append(unWeightedGpa9)
        return render_template("ninth.html", ninth=str(weightedGpa9) + " " + str(unWeightedGpa9))
    else:
        return render_template("ninth.html")

@app.route('/tenth-grade-gpa', methods =["GET", "POST"])
def tenthGradeGPA():
    global CWgpa
    global CUgpa
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
        unweightedGrades = []
        for i in range(1, counter+1):
            classType = request.form.get("class-"+str(i)).lower()
            classGrade = int(request.form.get("grade-"+str(i)))
            if (classType != "" and classGrade != ""):
                if ((classType == "ap" or classType == "ib" or classType == "dual" or classType == "regular" or classType == "honors") and (classGrade >= 0 and classGrade <= 100)):
                    classTypes.append(classType)
                    grades.append(classGrade)
                
                else: 
                   return render_template("tenth.html", error="Invalid class type!")
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

        weightedGpa10 = sum(weightedGrades)/len(weightedGrades)
        CWgpa.append(weightedGpa10)


        for i in range(0, len(grades)):
            if (grades[i] >= 90):
                unweightedGrades.append(4)
            elif (grades[i] >= 80):
                unweightedGrades.append(3)
            elif (grades[i] >= 70):
                unweightedGrades.append(2)
            else:
                unweightedGrades.append(0)

        unWeightedGpa10 = sum(unweightedGrades)/len(unweightedGrades)
        CUgpa.append(unWeightedGpa10)

        CWGpaTotal = sum(CWgpa)/2
        CUGpaTotal = sum(CUgpa)/2
        print(weightedGpa9, weightedGpa10)
        print(unWeightedGpa9, unWeightedGpa10)
        print(CUGpaTotal, CWGpaTotal)
        

        return render_template("tenth.html", ninth=str(weightedGpa9) + " " + str(unWeightedGpa9), tenth=str(weightedGpa10) + " " + str(unWeightedGpa10), totalW=CWGpaTotal, totalU = CUGpaTotal)
    else:
        return render_template("tenth.html")
    
    
@app.route('/eleventh-grade-gpa', methods =["GET", "POST"])
def eleventhGradeGPA():
    global CWgpa
    global CUgpa
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
        unweightedGrades = []
        for i in range(1, counter+1):
            classType = request.form.get("class-"+str(i)).lower()
            classGrade = int(request.form.get("grade-"+str(i)))
            if (classType != "" and classGrade != ""):
                if ((classType == "ap" or classType == "ib" or classType == "dual" or classType == "regular" or classType == "honors") and (classGrade >= 0 and classGrade <= 100)):
                    classTypes.append(classType)
                    grades.append(classGrade)
                
                else: 
                   return render_template("eleventh.html", error="Invalid class type!")
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

        weightedGpa11 = sum(weightedGrades)/len(weightedGrades)
        CWgpa.append(weightedGpa11)


        for i in range(0, len(grades)):
            if (grades[i] >= 90):
                unweightedGrades.append(4)
            elif (grades[i] >= 80):
                unweightedGrades.append(3)
            elif (grades[i] >= 70):
                unweightedGrades.append(2)
            else:
                unweightedGrades.append(0)

        unWeightedGpa11 = sum(unweightedGrades)/len(unweightedGrades)
        CUgpa.append(unWeightedGpa11)

        CWGpaTotal = sum(CWgpa)/3
        CUGpaTotal = sum(CUgpa)/3
        print(weightedGpa9, weightedGpa10, weightedGpa11)
        print(unWeightedGpa9, unWeightedGpa10, unWeightedGpa11)
        print(CUGpaTotal, CWGpaTotal)
        

        return render_template("eleventh.html", ninth=str(weightedGpa9) + " " + str(unWeightedGpa9), tenth=str(weightedGpa10) + " " + str(unWeightedGpa10), eleventh = str(weightedGpa11) + " " + str(unWeightedGpa11), totalW=CWGpaTotal, totalU = CUGpaTotal)
    else:
        return render_template("eleventh.html")

@app.route('/twelfth-grade-gpa', methods =["GET", "POST"])
def twelfthGradeGPA():
    global CWgpa
    global CUgpa
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
        unweightedGrades = []
        for i in range(1, counter+1):
            classType = request.form.get("class-"+str(i)).lower()
            classGrade = int(request.form.get("grade-"+str(i)))
            if (classType != "" and classGrade != ""):
                if ((classType == "ap" or classType == "ib" or classType == "dual" or classType == "regular" or classType == "honors") and (classGrade >= 0 and classGrade <= 100)):
                    classTypes.append(classType)
                    grades.append(classGrade)
                
                else: 
                   return render_template("twelfth.html", error="Invalid class type!")
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

        weightedGpa12 = sum(weightedGrades)/len(weightedGrades)
        CWgpa.append(weightedGpa12)


        for i in range(0, len(grades)):
            if (grades[i] >= 90):
                unweightedGrades.append(4)
            elif (grades[i] >= 80):
                unweightedGrades.append(3)
            elif (grades[i] >= 70):
                unweightedGrades.append(2)
            else:
                unweightedGrades.append(0)

        unWeightedGpa12 = sum(unweightedGrades)/len(unweightedGrades)
        CUgpa.append(unWeightedGpa12)

        CWGpaTotal = sum(CWgpa)/3
        CUGpaTotal = sum(CUgpa)/3
        print(weightedGpa9, weightedGpa10, weightedGpa11, weightedGpa12)
        print(unWeightedGpa9, unWeightedGpa10, unWeightedGpa11, unWeightedGpa12)
        print(CUGpaTotal, CWGpaTotal)
        

        return render_template("twelfth.html", ninth=str(weightedGpa9) + " " + str(unWeightedGpa9), tenth=str(weightedGpa10) + " " + str(unWeightedGpa10), eleventh = str(weightedGpa11) + " " + str(unWeightedGpa11), twelfth = str(weightedGpa12) + " " + str(unWeightedGpa12), totalW=CWGpaTotal, totalU = CUGpaTotal)
    else:
        return render_template("twelfth.html")


if __name__ == '__main__':
    app.run(debug=True)