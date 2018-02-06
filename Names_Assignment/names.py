'''
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def dict_students(students):
   for pupil in students:
       print pupil['first_name'], pupil['last_name']

dict_students(students)
'''

users = {
 'Students': [ #keys/titles
    #data/lists
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [ #keys/titles
    #data/lists
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def dict_users(users):
    for titles, lists in users.iteritems():
        print titles
        count = 0
        for names in lists:
            count += 1
            firstNameLen = len(names['first_name'])
            lastNameLen = len(names['last_name'])
            totalName = firstNameLen + lastNameLen
            print count, names['first_name'], names['last_name'], totalName
dict_users(users)














# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel
