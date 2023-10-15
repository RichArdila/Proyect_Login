def user_register():
    print("User register")
    name = input("Enter your username? ").strip()
    pass_word = input("Enter your password? ").strip()
    usuarios[name] = pass_word
    print(f"Successful registration! {usuarios}")


usuarios = {}