from user import User
from register_user import RegisterUsers
from validators import Validators

def main():
    users_register = RegisterUsers()

    name = input("Ingrese nombre: ")
    lastName = input("Ingrese apellido: ")
    age = Validators.get_age()
    marital_status = Validators.get_marital_status()

    user = User(name, lastName, age, marital_status)

    for _ in range(4):
        program_name = input("Nombre del programa (Word/Excel/PowerPoint/Access): ")
        domain = Validators.get_domain_level()
        hasCertification = Validators.get_certification_status(program_name)

        user.addProgram(program_name, domain, hasCertification)

    users_register.addUser(user)
    users_register.print()


if __name__ == "__main__":
    main()

## Jimmy Martínez - Carné No. 202302745
## Repo - https://github.com/MegaGone/udv/blob/develop/fundamentos_II/06_array_objects/