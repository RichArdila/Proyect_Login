class User:
    def __init__(self, nom, pwd):
        self.nom = nom
        self.pwd = pwd

u1 = User("jose", "123")
u2 = User("marina","123")

Users = [u1,u2] # lista de usuarios

name = input("Enter your user: ")
pass_word = input("Enter your password: ")

Val = 0

for i in range(len(Users)):
    if Users[i].nom == name and Users[i].pwd == pass_word:
        print(Users[i].nom, "- Welcome to the program")
        Val = 1
        break

if Val == 0:
    print("Try again!")




