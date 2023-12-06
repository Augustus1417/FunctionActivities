def get_student_info(info):
    if info == "name": return input("\nEnter student name: ")
    elif info == "subjects": return int(input("Enter number of subjects: "))
def get_subject_scores(numOfSubs):
    scorelist = []
    for x in range(1,numOfSubs+1):
        score = int(input(f"Grade Score {x}: "))
        scorelist.append(score)
    return scorelist
def calculate_average(scores): return (round(sum(scores)/len(scores),2))
def display_result(studentName, scoreAve): return print(f"\nStudent Name: {studentName}\nAverage: {scoreAve}")
studentName = get_student_info("name")
numOfSubs = get_student_info("subjects")
scores = get_subject_scores(numOfSubs)
scoreAve = calculate_average(scores)
display_result(studentName, scoreAve)
