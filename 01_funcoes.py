"""
    Função para calcular o Índice de Massa Corpórea
    de uma pessoa, dados o seu peso e sua altura
"""
def imc(peso, altura):
    # Peso dividido pela altura, elevada ao quadrado
    return peso / altura ** 2

resultado = imc(62, 1.78)

print("O resultado do IMC é ", resultado)

####################################################

from math import pi

def calcularArea(base, altura, tipo):
    if tipo == "R":   #Retângulo
        return base * altura   #Triângulo
    elif tipo == "T":
        return base * altura / 2
    elif tipo == "E":   #Elipse ou Círculo
        return (base / 2) * (altura / 2) * pi
    else:
        return None