#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
         language that combines remarkable power with very clear syntax"
print(f'{str.split(",")[2].strip()[:str.split(",")[2].find ("      ")]}with Python')
