print("\nExclusive Computer Network\n")
print("Only for members\n")

security = 0

username = ""
while not username:
    username = input("User: ")

password = ""
while not password:
    password = input("Password: ")

if username == "admin" and password == "admin":
    print("\nWelcome, " + username)
    security = 5
elif username == "test" and password == "test":
    print("\nWelcome, " + username)
    security = 4
elif username == "test1" and password == "test1":
    print("\nWelcome, " + username)
    security = 3
elif username == "test2" and password == "test2":
    print("\nWelcome, " + username)
    security = 2
elif username == "Guest" or password == "Guest":
    print("\nWelcome, " + username)
    security = 1
else:
    print("Access denied. Try again later")

input("\nPress Enter to exit\n")
