from words import comprobar_palabra, generar_palabra

def main():
    palabra_secreta = generar_palabra()
    intentos_restantes = 5
    victoria = False

    while intentos_restantes > 0 and not victoria:
        intento = input(f"Intentos restantes: {intentos_restantes}\nIngresa una palabra de 5 letras: ").lower()
        
        if len(intento) != 5:
            print("La palabra debe tener 5 letras.")
            

        resultado = comprobar_palabra(palabra_secreta, intento)

        if resultado == list(palabra_secreta):
            victoria = True
        else:
            print(f"No es correcto. Resultado: {' '.join(resultado)}")
            intentos_restantes -= 1

    mensaje = f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}" if victoria else f"Perdiste. La palabra era: {palabra_secreta}"
    print(mensaje)
if __name__ == "__main__":
    main()


