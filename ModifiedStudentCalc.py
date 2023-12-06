def get_student_info():
    global studentName, numOfSubs
    studentName = input("\nEnter student name: ")
    numOfSubs = int(input("Enter number of subjects: "))
def get_subject_scores():
    global scorelist
    scorelist = []
    for x in range(1,numOfSubs+1):
        score = int(input(f"Grade Score {x}: "))
        scorelist.append(score)
def Max_score(): return max(scorelist)
def Min_score(): return min(scorelist)
def Highest_to_Lowest():
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(scorelist) - 1):
            if scorelist[i] < scorelist[i + 1]:
                swapped = True
                scorelist[i], scorelist[i + 1] = scorelist[i + 1], scorelist[i]
    return scorelist
def calculate_average():
    global scoreAve
    scoreAve = (round(sum(scorelist) / len(scorelist), 2))
def display_result(studentName, scoreAve):
    print(f"Student Name: {studentName}\nAverage: {scoreAve}")
    print(f"Highest Score: {Max_score()}\nLowest Score: {Min_score()}")
    print(f"Sorted Scores (Highest to Lowest): {Highest_to_Lowest()}")
get_student_info()
get_subject_scores()
calculate_average()
for x in range(50): print("-",end="")
print("\n\t\t\t\t\tResults")
display_result(studentName, scoreAve)
for x in range(50): print("-",end="")
