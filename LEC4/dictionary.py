# dictionaries are used to store data value in key:value pairs
# they are unordered , mutable(changeable) and dont allow duplicate keys
# list can be stored in dictionary because both  are mutable

# dict={
#     "key":"value",
#     "name":"Aayush",
#     "cgpa":8,
#     "marks":[20,25,24],
#     "eligible":True,
#     "subjects":("Python","Java")
# }
# print(dict)
# print(type(dict)) #<class 'dict'>
# dict['name']='Aayush Patel'
# print(dict['name'])

# Nested Dictionaries
# student={
#     "name":"Aayush",
#     "cgpa":8,
#     "score":{
#         "Python":62,
#         "Java":54
#     }
# }
# print(student['score']['Java'])

# Methods
# print(student.keys())
# convert it into list
# print(list(student.keys()))

# print(len(student))

# print(student.values())
# print(list(student.values()))

# it return all key value pairs
# print(student.items())
# pair=list(student.items())
# print(pair[1])
# print(list(student.items()))

# print(student.get('cgpa'))
# print(student.get('cgpa2')) #None
# print(student['cgpa2']) #error

# student.update({'city':'anklav'})
# print(student)
# student.update({'name':"Aayush Patel"})
# print(student)

