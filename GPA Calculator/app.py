from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def displayWeightedCalc():
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
                   return render_template("index.html")
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

        weightedGpa = sum(weightedGrades)/len(weightedGrades)


        for i in range(0, len(grades)):
            if (grades[i] >= 90):
                unweightedGrades.append(4)
            elif (grades[i] >= 80):
                unweightedGrades.append(3)
            elif (grades[i] >= 70):
                unweightedGrades.append(2)
            else:
                unweightedGrades.append(0)

        unweightedGpa = sum(unweightedGrades/len(unweightedGrades))
        
        return str(weightedGpa) + " " + str(unweightedGpa)
    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)