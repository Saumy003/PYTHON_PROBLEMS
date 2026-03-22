# Itration Key Values in Dictonary Questions ->

# Q.1 Ask subject name and marks from the users and keep adding it to dictonary.

# marks = {}
# subject_count = int(input("Enter how many subjects:"))

# for _ in range(0 , subject_count):
#     subject_name = input("Enter the subject name:")
#     subject_marks = int(input(f"Enter marks for {subject_name}: "))
#     marks[subject_name] = subject_marks

# print(marks)

# Q.2 Convets two lists into dictonary. Make two list on your own if same length and convert them to dictonary.

# lst1 = ["python", "good", "done", "bye"]
# lst2 = [54, "wow", "anirudh", 99]

# result = {}

# for i in range(0 ,len(lst1) ):
#     result[lst1[i]] = lst2[i]

# print(result)

# Q.3 Write a program to sum of all the items in the dictonary.

subjects = {
    "physics" : 84,
    "chemistry": 83,
    "maths": 86,
}

sum_of_marks = 0

for v in subjects.values():
    sum_of_marks = sum_of_marks + v

print(sum_of_marks)      # print(sum(list(subjects.values()))) = 253

# Q. 4
"""
Ask a string from user. Display the dictonary where each key is a character
and value is the frequency of that character that comes in that string.
"""

my_string = input("Enter the string:")

freq = {}

for ch in my_string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
# Q. 5

"""
Store "name" of a student as Key, "list of 5 marks' of that student as a Value.
Store altest 5 students names. Print the sum and percentange of all the students.
"""
student_data = {
    "student1" : [85, 90, 78, 92, 88],
    "student2" : [75, 88, 92, 80, 87],
    "student3" : [90, 95, 89, 78, 93],
    "student4" : [80, 85, 88, 92, 87],
    "student5" : [92, 88, 95, 90, 85],
}

for name,marks in student_data.items():
    total = sum(marks)
    percentage = total / 500 * 100
    print(f"{name} has scored total {total} marks , percentange = {percentage : .2f}")
