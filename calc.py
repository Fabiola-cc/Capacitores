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

#C₀ = 4π∈₀*(rE*rI)/(rE-rI)
def Capacitancia_E(radioE, radioI): #Esfera
    if radioI == 0:
        return 0  
    
    inverso_k = 1/k #4π∈₀
    radios = radioE / radioI

    if radios == 1: # Evitar logaritmo igual a cero
        return 0

    div = radioE*radioI/(radioE-radioI)#(rE*rI)/ln(rE/rI)
    return inverso_k*div

#C₀ = 2π∈₀*L/ln(rE/rI)
def Capacitancia_C(largo, radioE, radioI): #Cilindro
    if radioI == 0:
        return 0  
    
    inverso_k = 2*np.pi*e0 #2π∈₀
    radios = radioE / radioI

    if radios == 1: # Evitar logaritmo igual a cero
        return 0

    ln = largo / np.log(radios) #L/ln(rE/rI)
    return inverso_k * ln


'''Función de Carga''' #C*V, misma para todos
def Carga(capacitancia, voltaje):
    return capacitancia*voltaje

'''Función de Energía''' #1/2(C)(V^2), misma para todos
def energia(capacitancia, voltaje):
    return ((capacitancia/2)*(voltaje**2))

'''Funciones de Dieléctricos''' 
#C =C₀*K
def dielectrico_lleno(capacitancia_inicial, constante_dielectrica):
    return capacitancia_inicial*(constante_dielectrica)

#C =C₀/2 *(1 + K)
def dielectrico_mitad(capacitancia_inicial, constante_dielectrica):
    return capacitancia_inicial*(constante_dielectrica+1)/2

#Cargas libre Placas ---> σ₀ = Carga*constante/largo*ancho
# Dielectrico
    # 1. El dieléctrico está en todo el capacitor 
    # 2. El dieléctrico está en la mitad del capacitor
def carga_libre_PP(Carga, largo, ancho, Dielectrico, constante):
    area = largo*ancho
    Densidades = [0,0] #[0] Aire, [1] Plexiglás
    if area == 0: #Retorna valores de 0, evitando errores
        pass
    else:
        if Dielectrico == 2:
            area = area*(constante + 1)/2
        Densidades[0] = Carga/area
        Densidades[1] = Densidades[0]*constante
        
    return Densidades       

#Cargas libre Esfera ---> σ₀ = Carga*constante/4πr^2
# Dielectrico
    # 1. El dieléctrico está en todo el capacitor
    # 2. El dieléctrico está en la mitad del capacitor
def carga_libre_Esfera(Carga, radioI, radioE, Dielectrico, constante):
    areaI = 4*np.pi*(radioI**2)
    areaE = 4*np.pi*(radioE**2)
    #[0] Aire Interno, [1] Aire Externo, [2] Plexiglás Interno, [3] Plexiglás Externo
    Densidades = [0,0,0,0] 

    if areaI == 0: #Retorna valores de 0, evitando errores
        pass
    else:
        if Dielectrico == 2:
            divisorE = areaE*(1 + constante)/2 #2πre^2*(1+K)
            divisorI = areaI*(1 + constante)/2 #2πri^2*(1+K)

            Densidades[0] = Carga/divisorI
            Densidades[1] = Carga/divisorE
        else:
            Densidades[0] = Carga/areaI
            Densidades[1] = Carga/areaE

        Densidades[2] = Densidades[0]*constante
        Densidades[3] = Densidades[1]*constante

    return Densidades

#Cargas libre Cilindro ---> σ₀ = Carga*constante/4πr^2*largo
# Dielectrico
    # 1. El dieléctrico está en todo el capacitor
    # 2. El dieléctrico está en la mitad del capacitor
def carga_libre_Cilindro(Carga, largo, radioE, radioI, Dielectrico, constante):
    areaI = 2*np.pi*radioI*largo
    areaE = 2*np.pi*radioE*largo
    #[0] Aire Interno, [1] Aire Externo, [2] Plexiglás Interno, [3] Plexiglás Externo
    Densidades = [0,0,0,0] 

    if areaI == 0: #Retorna valores de 0, evitando errores
            pass
    else:
        if Dielectrico == 2:
            divisorE = areaE*(1 + constante)/2 #πre*(1+K)
            divisorI = areaI*(1 + constante)/2 #πri*(1+K)

            Densidades[0] = Carga/divisorI
            Densidades[1] = Carga/divisorE
        else:
            Densidades[0] = Carga/areaI
            Densidades[1] = Carga/areaE

        Densidades[2] = Densidades[0]*3.40
        Densidades[3] = Densidades[1]*3.40

    return Densidades

#Carga ligada Cilindro 
def carga_ligada_PP(carga_libre, constante_dielectrica):
    result = (1-1/constante_dielectrica)
    return carga_libre*result

#Carga ligada de esfera
def carga_ligada_EC(carga_libre, constante_dielectrica): 
    carga_ligada = [0,0]
    carga_ligada[0] = carga_libre[0]*(1-1/constante_dielectrica) #Radio interno
    carga_ligada[1] = carga_libre[1]*(1-1/constante_dielectrica) #Radio externo
    return carga_ligada
