from random import randint
import oldmax

users = [

    {
        'name': 'Jack',
        'password': '0987654321',
        'age': 19
    },

    {
        'name': 'Helen',
        'password': '12345',
        'age': 20
    },
    {
        'name': 'Daniel',
        'password': 'qwerty',
        'age': 25
    }
]

print(oldmax.oldmax(users)['name'])
oldest_user = oldmax.oldmax((users))
print(oldest_user['name'])
for i in range(100):
    users.append({
        'name': oldmax.generate_name(),
        'password': oldmax.generate_name(),
        'age': randint(18, 40)
    })

print(users)
print(oldmax.oldmax(users)['name'])