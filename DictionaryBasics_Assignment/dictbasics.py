

# person = {}
# person['name']='Holly'
# person['age'] = '27'
# person['countryOfBirth'] = 'USA'
# person['favoriteLanguage'] = 'Python'

# print person


person = {
    "name": "Holly",
    "age": "27", 
    "country":"USA",
    "FavLang":"Python"
    }
# print person.items()
# print person.keys()
# print person.values()

def dict_me(person):
    for key, data in person.iteritems():
        print "My", key, "is" ,data
dict_me(person)