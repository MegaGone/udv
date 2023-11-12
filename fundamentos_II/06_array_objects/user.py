class User:
    def __init__(self, name, lastName, age, marital_status):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.marital_status = marital_status
        self.programs = []

    def addProgram(self, program, domain, isCertificated):
        for program in self.programs:
            if program['nombre'] == program:
                print(f"Error: Ya ha seleccionado el programa {program}. Elija otro.")
                return
        self.programs.append({'nombre': program, 'dominio': domain, 'certificacion': isCertificated})
