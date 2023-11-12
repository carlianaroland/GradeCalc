import copy
print('Carliana Roland, COMP163, 4/30/23, GradeCalc', '\n')


class Comp163Cat:  # suggestion: name your class the same name as your file
    file = "ccroland_textfile_weights.txt"  # THIS IS A CONSTANT / WHEN YOU SEE A VARIABLE IN ALL CAPS IT CAN'T BE CHANGED IN
    # EVERYTHING BUT PYTHON / STATIC
    work_category = ['Homework', 'Assignments', 'Labs', 'Assessments', 'Midterm', 'Final']
    _WorkWeight = dict()  # the underscore lets the program know its private (encapsulated) and when this is present
    # you do# getters and setters down below

    def __init__(self):  # you don't accept any arguments in an uml for the class __init__ constructor
        self._WorkWeight = dict()
        try:
            self.readWeight()
        except FileNotFoundError:  # if this is the reason it doesn't work it will set the weight for you this the base
            # exception for all exceptions
            self.setWeight()
        except Exception:  # the first exception that handles is the one it's going to take
            print("Unknown, try again")
        finally:
            print("Categories all set!")

    def setWeight(self):
        self._WorkWeight.clear()
        for work in self.work_category:
            weight = int(input(f"Enter {work} weight: "))
            self._WorkWeight.update({work: weight})

    def getWeight(self): return self._WorkWeight

    def readWeight(self):  # assume there's a file here
        self._WorkWeight.clear()
        f = open(self.file, 'r')  # you can open a file to read, write, and append, 'r' signifies to read the file
        lines = f.readlines()  # this functions reads the lines inside the file
        for lne in lines:
            obj = lne.split(',')  # the comma would represent as a delimiter / you've created a list called item you
            # want to add this to your _weights dict
            self._WorkWeight.update({obj[0]: float(obj[1])})
        f.close()  # be sure to always close your file
    def writeWeight(self):  # put 'pass' when you are not ready to read the defined variable
        f = open(self.file, 'w')
        for k, v in self._WorkWeight.items():
            f.write(k+','+str(v)+'\n')
        f.close()

    def __str__(self):  # the circle and arrow beside this def function overrides this function
        v = ""
        for work, weight in self._WorkWeight.items():  # displays the weights in strings
            v += work + " : "+str(weight)+"\n"
        return v

    def display(self):
        v = 1
        for work, weight in self._WorkWeight.items():
            print(str(v)+") " + work + " : "+str(weight)+"\n")
            v += 1  # appends the next option to display

    def edit(self, work, weight):
        self._WorkWeight.update({work: weight})

import copy
print('Carliana Roland, COMP163, Calculating weight and grades')
  # WRITE EVERYTHING TO THE FILE FIRST
class myGradeCalc(Comp163Cat):
    file = "ccroland_CalcGrades.txt"
    work_category = ['Homework', 'Assignments', 'Labs', 'Assessments', 'Midterm', 'Final']
    myGrades = []  # you will be able to add grades in this list along with finding the average
    _dict_grades = dict()
    ave_grades = {}
    FinalGrade = {}
# 'A': 94, 'A-': 90 or 93, 'B+': 89 or 87, 'B': 86 or 84, 'B-': 83 or 80, 'C+': 79 or 77, 'C': 76 or 74,
    #                   'C-': 73 or 70, 'D+': 69 or 67, 'D': 66 or 64, 'F': 63 or 0
    def __init__(self):
        self.myGrades = []
        self.dict_grades = dict()
        self.ave_grades = {}
        self.work_category = ['Homework', 'Assignments', 'Labs', 'Assessments', 'Midterm', 'Final']
        try:
            self.readGrades()
        except FileNotFoundError:
            self.setGrades()
        except Exception:
            print("Unknown, try again")
        finally:
            print("Choose an option below to your liking.")

    def setGrades(self):
        for work in self.work_category:
             grade = int(input(f"Enter {work} weight: "))
             self.dict_grades.update({work: grade})

    def getGrades(self): return self.dict_grades

    def readGrades(self):
        self.dict_grades.clear()
        f = open(self.file, 'r')  # you can open a file to read, write, and append, 'r' signifies to read the file
        gradelines = f.readlines()  # this functions reads the lines inside the file
        for lne in gradelines:
            obj = lne.split(',')  # the comma would represent as a delimiter / you've created a list called item you
            # want to add this to your _weights dict
            self.dict_grades.update({obj[0]: float(obj[1])})
        f.close()

    def writeGrades(self):
        f = open(self.file, 'w')
        for k, v in self.dict_grades.items():
            f.write(k + ',' + str(v) + '\n')
        f.close()

    def editGrades(self, work, grade):
        self.dict_grades.update({work: grade})

    def __str__(self):  # the circle and arrow beside this def function overrides this function
        v = ""
        for work, grade in self.dict_grades.items():  # displays the weights in strings
            v += work + " : " + str(grade) + "\n"
        return v

    def calcGrade(self):
        for work, grade in self.dict_grades:
            self.myGrades.append(self.dict_grades[grade])  # adding grade values in to grades list for calculation
            average = sum(self.myGrades) / len(self.myGrades)  # calculating final grades
            self.ave_grades.update({work: copy.deepcopy(average)})
        FinalGrade = {work: self.ave_grades[grade] * self.dict_grades[grade] for grade in self.ave_grades.values()}
        print(f'your final grade in the class is {FinalGrade} % !')
    def displayGrades(self):
        v = 1
        for work, grade in self.dict_grades.items():
            print(str(v) + ") " + work + " : " + str(grade) + "\n")
            v += 1


if __name__ == "__main__":
    while True:
        myGrade = myGradeCalc()
        print(myGrade)

        opt = input("(D)isplay (C)alculate (R)ead (W)rite (E)dit (DW)isplay Weights (RW)ead Weights (WW)rite Weights "
                    "(EW)dit Weights(Q)uite: ").upper()
        if opt == "W":
            myGrade.writeGrades()
        elif opt == "R":
            myGrade.readGrades()
        elif opt == "D":
            myGrade.displayGrades()
        elif opt == "C":
            myGrade.calcGrade()
        elif opt == "E":
            print('1) Homework')
            print('2) Assignments')
            print('3) Labs')
            print('4) Assessments')
            print('5) Midterm')
            print('6) Final')
            work = int(input("Enter category to edit: "))
            work -= 1
            wght = int(input("Enter new grade for "+myGrade.dict_grades[work]+" : "))
            myGrade.editGrades(myGrade.dict_grades[work], wght)
        elif opt == "DW":
            myGrade.display()
        elif opt == "RW":
            myGrade.readWeight()
        elif opt == "WW":
            myGrade.writeWeight()
        elif opt == "EW":
            print('1) Homework')
            print('2) Assignments')
            print('3) Labs')
            print('4) Assessments')
            print('5) Midterm')
            print('6) Final')
            work = int(input("Enter category to edit: "))
            work -= 1
            wght = float(input("Enter new weight for "+myGrade.work_category[work]+" : "))
            myGrade.edit(myGrade.work_category[work], wght)
        elif opt == "Q":
            break
        else:
            print("Invalid Option")