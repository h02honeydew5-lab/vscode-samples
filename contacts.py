contacts = {
    'numbers': 4,
    'students':
        [
            {'name': 'Sarah Holderness', 'email': 'sarah@example.com'},
            {'name': 'Harry Potter', 'email': 'harry@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])
    
#pip --version
import requests
response = requests.get('http://api.open-notify.org/astros.json')

json = response.json()
print(json)
    