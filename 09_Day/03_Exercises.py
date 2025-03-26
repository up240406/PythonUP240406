profile ={
    'first_name': 'Erika',
    'last_name': 'Diaz de la vega',
    'age': 18,
    'country': 'German',
    'is_married': True,
    'skills': ['JavaScript', 'German', 'Horse Riding', 'Python', 'Painting'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#1 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in profile:
    print(profile['skills']
          [len(profile['skills'])//2])

#2 Check if the person dictionary has skills key, if so check if the person has 'Python' skill 
#and print out the result.
if 'skills' in profile:
    if 'Python' in profile['skills']:
        print['skills']

#3  If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in profile:
    sk = profile['skills']
    if 'JavaScript'in sk or 'React' in sk:
        print('He is a front end developer')
    elif 'Node'in sk or 'Python' in sk or 'MongoDB'in sk:
        print('He is a backend developer')
    elif 'Node'in sk or 'React'in sk or 'MongoDB'in sk:
        print('He is a fullstack developer')
    else:
        print('unknown title')

#4 If the person is married and if he lives in Finland, print the information in the following format:
#Asabeneh Yetayeh lives in Finland. He is married.