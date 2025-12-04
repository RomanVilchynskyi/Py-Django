users = {}

def add(user, password):
    if user in users:
        print("User already exists!")
    else:
        users[user] = password
        print("User added")

add("user1", '122142')
add("user2", '122142')
print(users)

def remove(user):
    if user in users:
        users.pop(user)
        print("User successfuly removed")

    else:
        print("User does not exist")

remove("user1")
print(users)

def change_pass(user, new_password):
    if user in users:
        if users[user] == new_password:
            print("Password is the same")
        else:
            users[user] = new_password
            print("Password changed successfuly")
    else:
        print("User does not exist")

change_pass("user2", '184563')
print(users)

def check_passwords():
    weak_pass = False

    for username, password in users.items():
        if len(password) < 6 or password.isalpha(): 
            print(f"{username}: weak - {password}")
            weak_pass = True

    if not weak_pass:
        print("Good passwords")

check_passwords()

def find_pass(user):
    if user in users:
        print(f"{user} - {users[user]}")
    else:
        print("User does not exist")

find_pass("user2")


with open("02_tuples/assets/words.txt", "a") as f:
    f.write(str(users))

file1 = open("02_tuples/assets/words.txt", "rt")

print(f"Content: {file1.read()}")

file1.close()