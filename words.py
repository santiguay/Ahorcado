from random import choice

def generar_palabra():
    # Función que devuelve una palabra secreta elegida al azar desde una lista predefinida.
    palabras = [
        "mango", "flora", "azote", "lucha", "talar",
        "cebra", "huevo", "manta", "lente", "pilar",
        "ducha", "jugar", "fruta", "balsa", "ronda",
        "chico", "sollo", "pargo", "sello", "rumba"
    ]
    return choice(palabras)

def comprobar_palabra(palabra_secreta, intento):
    # Función para verificar el intento del jugador y generar una lista de resultado.
    # Si la letra del intento coincide en la misma posición que la palabra secreta,
    # se agrega la letra al resultado, de lo contrario, se agrega un guion bajo.
    resultado = ['_' for _ in range(len(palabra_secreta))]

    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == intento[i]:
            resultado[i] = intento[i]
    return resultado

