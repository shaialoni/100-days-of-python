# List Comprehension

# new_list = [new_item for item in list]

# numbers = [1, 2, 3]
# new_list_1 = []

# for n in numbers:
#     add_1 = n + 1
#     new_list_1.append(add_1)

# new_list_2 = [n + 1 for n in numbers]

# print(new_list_1)
# print(new_list_2)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# range(1,5)
# new_list = [number * 2 for number in range(1,5) ]
# print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
name_list = [name.upper() for name in names if len(name) > 4]
# print(name_list)

# Dictionary comprehension
import random
#new_dict = {new_key:new_value for (key, value) in dict.items() if test}
student_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

student_DF = pandas.DataFrame(student_dict)
print(student_DF)

#Loop through a dataframe

# for (key, value) in student_DF.items():
#     print(value)

# Loop through rows of data frame
for (index, row) in student_DF.iterrows():
    if row.student == "Angela":
        print(row.score)