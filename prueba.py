import numpy as np
import matplotlib.pyplot as plt

def obtener_parametros():
    def obtener_dato_con_mensaje(mensaje, valor_predeterminado):
        entrada = input(mensaje)
        if entrada.lower() == "no":
            return valor_predeterminado
        try:
            return float(entrada)
        except ValueError:
            print("Entrada no válida. Usando valor predeterminado.")
            return valor_predeterminado
    
    parametros = {
        "amplitud": obtener_dato_con_mensaje("Introduce la amplitud (o 'no' para usar valor 1): ", 1),
        "frecuencia": obtener_dato_con_mensaje("Introduce la frecuencia en Hz (o 'no' para usar 1 Hz): ", 1),
        "longitud_onda": obtener_dato_con_mensaje("Introduce la longitud de onda (o 'no' para usar 1 m): ", 1),
        "longitud_cuerda": obtener_dato_con_mensaje("Introduce la longitud de la cuerda (o 'no' para usar 1): ", 1),
        "n": int(obtener_dato_con_mensaje("Introduce el valor entero de n (>0, usar 1 si no cumple): ", 1))
    }
    
    if parametros["n"] <= 0:
        parametros["n"] = 1
    
    return parametros

def calcular_onda(parametros):
    x = np.linspace(0, parametros['longitud_cuerda'], 1000)
    t = np.linspace(0, 2, 1000)
    
    numero_de_onda = parametros['n'] * np.pi / parametros['longitud_cuerda']
    frecuencia_angular = 2 * np.pi * parametros['frecuencia']
    
    onda_estacionaria = 2 * parametros['amplitud'] * np.sin(numero_de_onda * x[:, None]) * np.cos(frecuencia_angular * t)
    return x, t, onda_estacionaria

def graficar_onda(x, t, onda_estacionaria):
    plt.figure(figsize=(10, 6))
    for i in range(0, len(t), 150):  
        plt.plot(x, onda_estacionaria[:, i], label=f't = {t[i]:.2f} s')

    plt.title("Simulación de Onda Estacionaria")
    plt.xlabel("Posición (x)")
    plt.ylabel("Desplazamiento (ψ)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    parametros = obtener_parametros()
    x, t, onda_estacionaria = calcular_onda(parametros)
    graficar_onda(x, t, onda_estacionaria)