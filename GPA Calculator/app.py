from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global variables for storing cumulative data
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
    # Redirect to the NinthGradeGPA route when accessing the root URL
    return redirect(url_for('NinthGradeGPA'))

@app.route('/ninth-grade-gpa', methods=["GET", "POST"])
def NinthGradeGPA():
    # Global variables to store cumulative data
    global weightedTotalCredits
    global unweightedTotalCredits
    global weightedGpa9
    global unWeightedGpa9

    if request.method == "POST":
        # Process form data for Ninth Grade GPA calculation
        counter = int(request.form.get("counter"))
        
        classType = ""
        classGrade = 0
        grades = []
        classTypes = []
        weightedGrades = []
        unWeightedGrades = []

        for i in range(1, counter+1):
            # Extract class type and grade from the form
            classType = request.form.get("class-"+str(i)).lower() 
            try:
                classGrade = int(request.form.get("grade-"+str(i)))
            except:
                # Handle invalid grade input
                return render_template("ninth.html", error="Must enter a valid grade")

            if (classType != "" and classGrade != ""):
                # Validate class type and grade input
                if ((classType == "ap" or classType == "ib" or classType == "dual" or classType == "regular" or classType == "honors") and (classGrade >= 0 and classGrade <= 100)):
                    classTypes.append(classType)
                    grades.append(classGrade)
                else:
                    # Handle invalid class type or grade input
                    return render_template("ninth.html", error="Invalid class type or invalid grade!")
            else:
                continue

        # Calculate weighted and unweighted GPAs
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
            # Handle case where at least 2 grades are required for calculation
            return render_template("ninth.html", error="You must enter at least 2 grades to calculate!")

        # Update global variables with calculated values
        weightedGpa9 = sum(weightedGrades) / len(weightedGrades)
        weightedTotalCredits = weightedTotalCredits + weightedGrades
        CWgpa = sum(weightedTotalCredits) / len(weightedTotalCredits)

        for i in range(0, len(grades)):
            if (grades[i] >= 90):
                unWeightedGrades.append(4)
            elif (grades[i] >= 80):
                unWeightedGrades.append(3)
            elif (grades[i] >= 70):
                unWeightedGrades.append(2)
            else:
                unWeightedGrades.append(0)

        # Calculate unweighted GPA
        unWeightedGpa9 = sum(unWeightedGrades) / len(unWeightedGrades)
        unweightedTotalCredits = unweightedTotalCredits + unWeightedGrades
        CUgpa = sum(unweightedTotalCredits) / len(unweightedTotalCredits)

        # Render template with calculated GPAs
        return render_template("ninth.html", ninth=str(weightedGpa9) + " " + str(unWeightedGpa9), totalW=CWgpa, totalU=CUgpa)
    else:
        # Render the initial template for Ninth Grade GPA input
        return render_template("ninth.html")

# Similar patterns are followed for other grade levels (tenth, eleventh, twelfth)

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app
