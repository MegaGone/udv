class Validators:
    @staticmethod
    def get_age():
        while True:
            try:
                age = int(input("Ingrese edad: "))
                return age
            except ValueError:
                print("Error: Ingrese un número válido para la edad.")

    @staticmethod
    def get_marital_status():
        allowed_options = {1: 'Soltero', 2: 'Casado', 3: 'Viudo', 4: 'Divorciado'}
        
        while True:
            print("Seleccione el estado civil:")
            for option, marital_status in allowed_options.items():
                print(f"{option}. {marital_status}")

            try:
                option_selected = int(input("Elija una opción: "))
                if option_selected in allowed_options:
                    return allowed_options[option_selected]
                else:
                    print("Error: Ingrese una opción válida.")
            except ValueError:
                print("Error: Ingrese un número válido.")

    @staticmethod
    def get_domain_level():
        allowed_options = {1: 'Nulo', 2: 'Básico', 3: 'Intermedio', 4: 'Avanzado', 5: 'Experto'}

        while True:
            print("Seleccione el dominio que posee:")
            for option, domain in allowed_options.items():
                print(f"{option}. {domain}")

            try:
                option_selected = int(input("Elija una opción: "))
                if option_selected in allowed_options:
                    return allowed_options[option_selected]
                else:
                    print("Error: Ingrese una opción válida.")
            except ValueError:
                print("Error: Ingrese un número válido.")

    @staticmethod
    def get_certification_status(program_name):
       while True:
            try:
                hasCertification = int(input(f"¿Posee certificación en {program_name}? (0 para No, 1 para Sí): "))
                if hasCertification in [0, 1]:
                    return bool(hasCertification)
                else:
                    print("Error: Ingrese 0 para No o 1 para Sí.")
            except ValueError:
                print("Error: Ingrese un número válido (0 para No, 1 para Sí).")