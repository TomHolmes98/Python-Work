def final_grade(homework, assessment, exam):
 
    homework = float(homework / 25) *100
    assessment = float(assessment / 50) *100
    exam = float(exam / 100) *100
 
    return ((homework * 0.25) + (assessment * 0.5) + exam)/1.75
 
   
homework = int(input("What was your final homework score? "))
assessment = int(input("What was your final assessment score? "))
exam = int(input("What was your final Exam score? "))

print("Final grade is: " + str(final_grade(homework, assessment, exam)))

