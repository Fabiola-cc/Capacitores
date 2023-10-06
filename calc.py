'''
Universidad del Valle de Guatemala
Parcial 1 - Física 3
Simulación de capacitancias
 ---> Cálculos

Fabiola Contreras 22787
María José Villafuerte 22129
'''

# Importamos las librerías necesarias para la simulación.
from tkinter import DoubleVar
import numpy as np # Libreria científica y matemática para Python.
from scipy import constants, integrate   # Librerias para integrar funciones en un intervalo dado.
'''
Diccionario: 


'''

k = 8.988*10**9 #Valor de 1/4π∈₀
e0= 8.85*10**(-12)
#ecuacion_general_CampoE = (k*Q)/(r**2)

'''Funciones de Capacitancia'''
#C₀ = ∈₀*A/d
def Capacitancia_PP(largo, ancho, separacion): #Placas Paralelas
    area = largo * ancho
    division = area / separacion
    return e0 * division

#C₀ = 4π∈₀*(rE*rI)/ln(rE/rI)
def Capacitancia_E(radioE, radioI): #Esfera
    inverso_k = 1/k
    radios = radioE*radioI/np.log(radioE/radioI)
    return inverso_k*radios

#C₀ = 2π∈₀L/ln(rE/rI)
def Capacitancia_C(largo, radioE, radioI): #Cilindro
    inverso_k = 2/k
    ln = 1/np.log(radioE/radioI)
    return inverso_k*largo*ln

'''Funciones de Carga'''
def Carga(capacitancia, voltaje):
    return capacitancia*voltaje

'''Funciones de Energía'''
#1/2(C)(V^2)
def energia(capacitancia, voltaje):
    return ((capacitancia/2)*(voltaje^2))

'''Funciones de Dieléctricos'''
def dielectrico(capacitancia_inicial, constante_dielectrica):
    return capacitancia_inicial*(constante_dielectrica+1)/2

def carga_libre_PP(Carga,largo, ancho):
    area = largo*ancho
    return (Carga/area)

def carga_libre_Esfera(Carga, radio):
    area = 4*np.pi*(radio^2)
    return (Carga/area)

def carga_libre_Cilindro(Carga, largo, radioE):
    area = 2*np.pi*radioE*(radioE+largo)
    return (Carga/area)

def carga_ligada(carga_libre, constante_dielectrica):
    return carga_libre(1-(1/constante_dielectrica))


