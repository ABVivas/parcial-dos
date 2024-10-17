def calcular_bonificacion(salario_base, cargo, nivel_desempeño):
    bonificacion: int = 0

    if cargo.lower() == "directivo":
        if nivel_desempeño.lower() == "alto":
            bonificacion = salario_base * 0.20
        elif nivel_desempeño.lower() == "medio":
            bonificacion = salario_base * 0.10

    elif cargo.lower() == "operativo":
        if nivel_desempeño.lower() == "alto":
            bonificacion = salario_base * 0.15
        elif nivel_desempeño.lower() == "medio":
            bonificacion = salario_base * 0.05

    return bonificacion

def mostrar_resumen(salario_base, cargo, nivel_desempeño):
    bonificacion: int = calcular_bonificacion(salario_base, cargo, nivel_desempeño)
    total = salario_base + bonificacion
    print("-----Resumen del Pago-----")
    print(f"Cargo: {cargo.capitalize()}")
    print(f"Nivel de Desempeño: {nivel_desempeño.capitalize()}")
    print(f"Salario Base: ${salario_base}")
    print(f"Bonificación: ${bonificacion}")
    print(f"Total a Recibir: ${total}")
    print("------------------------------")

def main():
    try:
        salario_base = int(input("Salario base mensual $: "))
        cargo = input("Cargo empleado: ")
        nivel_desempeño = input("Nivel de desempeño: ")

        mostrar_resumen(salario_base, cargo, nivel_desempeño)

    except ValueError:
        print("Error: Ingrese un valor numérico válido para el salario base.")


if __name__ == "__main__":
    main()




