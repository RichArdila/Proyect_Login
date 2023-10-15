# Una vez se cumpla la condicion del else debe abortar proceso o detenerse.
# Crear condiciones de password igual que el usuario, validar que sea correcta.
# Crear condicional regex
# Modificar que validacion de user and password debe ser en base de datos.

def main():
    login()


def login():
    print("Login")
    name = input("Enter your username: ").strip()
    pass_word = input("Enter your password: ").strip()
    print(f"Login Successful! {name},{pass_word}")


if __name__ == "__main__":
    main()


    