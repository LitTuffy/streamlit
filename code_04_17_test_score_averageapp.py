#This program average teat scores, It asks the users for the number of the students and the number of test scores per students

#Add input validation: students and test number can not be exceed 11. The number of exam score should be 0 to 100
#! input validation for num_students [finished]
#! input validation for quiz [finished]
#! Calculate the average exams score of the all students [finished]
#! (EXTRA POINT) Make it as streamlit web application 
#! (EXTRA POINT) Deploy your application to the github and stream.io (leave your app address with "#" at the top of the program)

import streamlit as st

#Get the number of the students
num_student = int(st.number_input("How many students do you have: "))
#! input validation for num_students
while num_student <= 0 or num_student > 11:
    st.write("The number is wrong, please enter again!")
    num_student = int(st.number_input("How many students do you have: "))
#Get the number of the test scores of per students
num_test_score = int(st.number_input("How many quiz are you run per student: "))
#! input validation for quiz
while num_test_score <= 0 or num_test_score > 11:
    st.write("Sorry the number is wrong, please enter again!")
    num_test_score = int(st.number_input("How many quiz are you run per student: "))
#! Calculate the average exams score of the all students
total_average_score = 0.0
#Deterine each student's average test score
for student in range (num_student):
    #Initialize an accumlator for test score
    total = 0.0
    #Get a students' test score
    st.write('Student number', student + 1)
    st.write('------------------------------')
    for test_num in range (num_test_score):
        st.write("test number", test_num + 1)
        score = float(st.number_input("score: "))
        #! input validation for score
        while score < 0 or score > 100:
            st.write("Sorry, the number is wrong, please enter again!")
            score = float(st.number_input("score: "))
        total = total + score #total += score
#Calculate the average test score for this students
    average = total / num_test_score
    total_average_score = total_average_score + total
#Display the average
    st.write('The average for student number', student + 1, 'is', average)
    st.write()
result = total_average_score / (num_student * num_test_score)
st.write(f"The average score of the all students' score is: {result}")