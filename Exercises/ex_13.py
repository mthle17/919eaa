"""
Create a function that finds first free classroom and returns its name.

Classroom structure is a dictionary, available in global scope:
classrooms = {
  "Classroom1": 0,
  "Classroom2": 0,
  "Classroom3": 0,
  "Classroom4": 1,
  "Classroom5": 0,
  "Classroom6": 1,
  "Classroom7": 1,
}
Free classrooms have value 1, and occupied ones have value 0.

When program is run, the function gets called.

*Example*
Classroom4
"""
classrooms = {
    "Classroom1": 0,
    "Classroom2": 0,
    "Classroom3": 0,
    "Classroom4": 1,
    "Classroom5": 0,
    "Classroom6": 1,
    "Classroom7": 1,
}

def find_free_classroom():
    for key in classrooms:
        if(classrooms[key] == 1):
            return key

free_classroom = find_free_classroom()
print(free_classroom)
