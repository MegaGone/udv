class RegisterUsers:
    def __init__(self):
        self.users = []

    def addUser(self, persona):
        self.users.append(persona)

    def print(self):
        for user in self.users:
            print(f"\nNombre: {user.name}, Apellido: {user.lastName}, Edad: {user.age}, Estado civil: {user.marital_status}")
            print("Programas:")
            for program in user.programs:
                print(f"  - Nombre del programa: {program['nombre']}, Dominio: {program['dominio']}, Certificación: {program['certificacion']}")