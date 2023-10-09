'''
Universidad del Valle de Guatemala
Parcial 1 - Física 3
Simulación de capacitancias
 ---> Cálculos

Fabiola Contreras 22787
María José Villafuerte 22129
'''
import numpy as np # Libreria científica y matemática para Python.

k = 8.988*10**9 #Valor de 1/4π∈₀
e0= 8.85*10**(-12)

'''Funciones de Capacitancia'''
#C₀ = ∈₀*A/d
def Capacitancia_PP(largo, ancho, separacion): #Placas Paralelas
    area = largo * ancho
    if separacion == 0:
        return 0
    else:
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


'''Función de Carga''' #C*V, misma para todos
def Carga(capacitancia, voltaje):

    return capacitancia*voltaje

'''Función de Energía''' #1/2(C)(V^2), misma para todos
def energia(capacitancia, voltaje):
    return ((capacitancia/2)*(voltaje**2))

'''Funciones de Dieléctricos'''
def dielectrico_lleno(capacitancia_inicial, constante_dielectrica):
    return capacitancia_inicial*(constante_dielectrica)

def dielectrico_mitad(capacitancia_inicial, constante_dielectrica):
    return capacitancia_inicial*(constante_dielectrica+1)/2

#Cargas libre Placas 
#Lleno
    #

#Mitad
    #
    #


#Cargas libre Esfera 
#Lleno
    #
    #

#Mitad
    #
    #
    #
    #

#Cargas libre Cilindro 
#Lleno
    #
    #

#Mitad
    #
    #
    #
    #
    
def carga_libre_PP(Carga,largo, ancho):
    area = largo*ancho
    if area == 0:
        return 0
    else:
        return (Carga/area)

def carga_libre_Esfera(Carga, radio):
    area = 4*np.pi*(radio^2)
    return (Carga/area)

def carga_libre_Cilindro(Carga, largo, radioE):
    area = 2*np.pi*radioE*(radioE+largo)
    return (Carga/area)

def carga_ligada(carga_libre, constante_dielectrica):
    return carga_libre*(1-(1/constante_dielectrica))