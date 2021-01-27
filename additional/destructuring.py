user = {
    'name': 'João Marcus',
    'lastname': 'Fernandes',
    'username': 'joaomarcuslf2',
    'domain': 'gmail.com'
}


def get_user_data():
    full_name = f"{user['name']} {user['lastname']}"
    email = f"{user['username']} {user['domain']}"

    return full_name, email


full_name, email = get_user_data()

# In Lists

people = [
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"),
    ("Harry", 32, "Lecturer")
]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")
