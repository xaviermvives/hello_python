# os.system
# subprocess.run  version mejorada de os.system (que se conserva), más funciones, más seguro

# funcion para añadir un usuario al sistema
import os

def add_user():
    username = input("Enter name of user to add")

    check_user = os.system(f"getent passwd {username}") # comprueba si el username existe o no en el sistema (en comando bash)

    if check_user == 0:
        print(f"The username '{username}' already exists")
        return # salir de la ejecución, ya que el user ya existe
    
    confirm = input(f"Do you want to add {username} to the system? (y/n)").lower()

    if confirm == 'y':
        result = os.system(f"sudo useradd -m {username}") # añadimos ususario al sistema (en bash)

        if result == 0:
            print(f"User {username} added susccessfully!")
        else:
            print(f"Failed to add user {username}")
    else:
        print("User addition cacelled")


if __name__ == "__main__":  # fa que s'executi des del principi aquí , no com a modul, des de fora no s'executarà
    add_user()