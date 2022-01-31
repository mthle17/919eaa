"""
Create a function that finds all free classrooms and returns its names.

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
['Classroom4', 'Classroom6', 'Classroom7']
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
    free_keys = []
    for key in classrooms:
        if(classrooms[key] == 1):
            free_keys.append(key)
    return free_keys

free_classrooms = find_free_classroom()
print(free_classrooms)
