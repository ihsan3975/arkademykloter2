import json
my_identities = {"name":'Maulana Ihsan',
                'age': 22,
                'address': 'Jalan Idris, Jakbar',
                'hobbies': ['Tidur', 'Jalan-jalan'],
                'is_married': False,
                'list_school': ['year_in : 2003, year_out : 2009, major : null',
                                'year_in : 2009, year_out : 2012, major : null',
                                'year_in : 2012, year_out : 2015, major : Science',
                                'year_in : 2015, year_out : 2019, major : Physics'],
                 'skills' : ['skill name : python, level : beginner',
                             'skill name : matlab, level : beginner',
                             'skill name : machine learning, level : beginner'],
                 'interest_in_coding': True
                }
with open('no_1.json', 'w') as json_file:  
    json.dump(my_identities, json_file)