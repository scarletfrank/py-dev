person = {'name':'duck','age':'32', 'sex':'female'}

def describe_person(person):
    print('Description of', person['name'])
    print('Sex:', person['sex'])
    try:
        print('Occupation', person['occupation'])
    except KeyError as e:
        print('Invalid Key: ', e)
    finally:
        print('Age:', person['age'])

describe_person(person)