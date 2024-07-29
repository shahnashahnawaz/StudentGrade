import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Student Grade Tracker")
screen.setup(width=800, height=600)
screen.bgcolor("#af8260")

# Title
title_turtle = turtle.Turtle()
title_turtle.hideturtle()
title_turtle.penup()
title_turtle.color("maroon")
title_turtle.goto(0, 260)
title_turtle.write("Student Grade Tracker", align="center", font=("Arial", 24, "bold"))

# Input fields
input_turtle = turtle.Turtle()
input_turtle.hideturtle()
input_turtle.penup()
input_turtle.goto(-250, 200)
input_turtle.color("beige")

input_turtle.write("Enter Student Name: ", align="left", font=("Arial", 16, "normal"))

# Input student name
student_name = turtle.textinput("Input", "Enter Student Name:")

input_turtle.goto(-250, 150)
input_turtle.write("Enter Student Grade: ", align="left", font=("Arial", 16, "normal"))

# Input student grade
student_grade = turtle.textinput("Input", "Enter Student Grade:")

# Data storage
students = []

def add_student(name, grade):
    students.append((name, grade))

def display_students():
    display_turtle.clear()
    display_turtle.goto(-250, 50)
    display_turtle.write("Student List:", align="left", font=("Arial", 18, "bold"))
    
    y_offset = 0
    for i, (name, grade) in enumerate(students):
        y_offset -= 30
        display_turtle.goto(-250, 50 + y_offset)
        display_turtle.write(f"{i + 1}. {name} - {grade}", align="left", font=("Arial", 16, "normal"))

add_student(student_name, student_grade)

# Display students
display_turtle = turtle.Turtle()
display_turtle.hideturtle()
display_turtle.penup()
display_students()

# Exit on click
screen.exitonclick()
