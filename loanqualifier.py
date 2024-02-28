# loanqualifier.py
# this program get input from user and determine acceptance or rejection of a loan application
import streamlit as st
st.title("load qualifier")

# set minimum salary and year or work
MINSALARY = 400000
MINYEAR = 5

# get input from user about salary and year
SALARY = float(st.number_input("please enter your annual salary: "))
YEAR = int(st.number_input("pkease enter your year of workz: "))

# determine whether the loan application is accepted or rejected
if st.button ("sumbit"):
    if SALARY > MINSALARY and YEAR > MINYEAR:
        st.write("Congrauation, your application has accepted")
    else:
        st.write ("sorry, your application has rejected")
else:
    st.write("please enter your information")