'''
Universidad del Valle de Guatemala
Parcial 1 - Física 3
Simulación de capacitancias
 ---> Graficación de capacitores 

Fabiola Contreras 22787
María José Villafuerte 22129
'''
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as mlines

'''
Variables:
Ri = Radio interno
Re = Radio externo
Dielectrico =
    1. No tiene dieléctrico 
    2. El dieléctrico está en todo el capacitor
    3. El dieléctrico está en la mitad del capacitor
'''

# Crear una figura y un eje
figure, ax = plt.subplots()

def CapacitorPlacasParalelas(largo, separacion, Dielectrico):
    #Detalles
    distanciaSeparacion = mlines.Line2D([largo/2 +0.1, largo/2 +0.1], [-separacion/2 + 0.5, separacion/2], color='#74cc83', linewidth=1) 
    ax.add_line(distanciaSeparacion) #Distancia
    ax.annotate("d = " + str(separacion), xy=(largo/2 +0.15, 0.3), color='#74cc83', fontsize=8, fontname='Times New Roman')
    
    ancho = mlines.Line2D([-largo/2, largo/2], [-separacion/2 - 0.1, -separacion/2 - 0.1], color='#70a193', linewidth=1)
    ax.add_line(ancho) #Largo
    ax.annotate("largo = " + str(largo), xy=(-0.4, -separacion/2 - 0.25), color='#70a193', fontsize=8, fontname='Times New Roman')

    if Dielectrico == 1: #sin
        ax.annotate("Aire", xy=(-0.3,0.1), color='black', fontsize=12, fontname='Times New Roman')
    elif Dielectrico == 2: #completo
        dielectrico = patches.Rectangle((-largo/2,-separacion/2 + 0.3), largo, separacion-0.3, facecolor='#9999a1')
        ax.annotate("Plexiglás", xy=(-0.3,0.1), color='black', fontsize=12, fontname='Times New Roman')
        ax.add_patch(dielectrico)
    else: #mitad
        dielectrico = patches.Rectangle((-largo/2,-separacion/2 + 0.3), largo/2, separacion-0.3, facecolor='#9999a1', linewidth=1)
        ax.annotate("Aire", xy=(largo/4,0.1), color='black', fontsize=12, fontname='Times New Roman')
        ax.annotate("Plexiglás", xy=(-largo/3,0.1), color='black', fontsize=12, fontname='Times New Roman')
        ax.add_patch(dielectrico)

    rectangulo = patches.Rectangle((-largo/2,-separacion/2 + 0.3), largo, separacion-0.3, linewidth=1, edgecolor='black', fill=False)
    ax.add_patch(rectangulo)

    # Crear barras de carga
    BarraQ1 = patches.Rectangle((-largo/2,separacion/2), largo, 0.3, linewidth=1, edgecolor='red', facecolor='#f59399')
    BarraQ2 = patches.Rectangle((-largo/2,-separacion/2), largo, 0.3, linewidth=1, edgecolor='blue', facecolor='#9993f5')
    ax.add_patch(BarraQ1)
    ax.add_patch(BarraQ2)

    # Configurar los límites del eje
    ax.set_xlim(-largo, largo)
    ax.set_ylim(-separacion, separacion)

    plt.title('Capacitor de placas paralelas\ncorte transversal')
    plt.axis('equal')  # Para asegurarse de que la figura sea simétrica
    plt.show()
    

def CapacitorEsferico(Ri, Re, Dielectrico):
    # Dibujar el círculo externo
    circulo_externo = patches.Circle((0, 0), radius=Re, fill=False, edgecolor='black', linewidth=1.5)
    ax.add_patch(circulo_externo)

    if Dielectrico == 1:
        pass
    elif Dielectrico == 2:
        circulo_externo_fill = patches.Circle((0, 0), radius=Re, facecolor='#9999a1', alpha=0.5)
        ax.add_patch(circulo_externo_fill)
    else:
        # Rellenar la mitad del círculo externo con azul
        mitad_dielectrico = patches.Wedge(center=(0, 0), r=Re, theta1=180, theta2=360, facecolor='#9999a1', alpha=0.5)
        ax.add_patch(mitad_dielectrico)
    
    # Dibujar el círculo interno
    circulo_interno = patches.Circle((0, 0), radius=Ri, facecolor='white', edgecolor='black', linewidth=1)
    ax.add_patch(circulo_interno)

    # Representar los radios usando quiver
    ax.quiver(0, 0, 0, Re, angles='xy', scale_units='xy', scale=1, color='blue', label='Ri')
    ax.annotate("Re = " + str(Re), xy=(0.1, Re/2), xytext=(0.2, Re), textcoords='offset points', color='blue')
    ax.quiver(0, 0, Ri, 0, angles='xy', scale_units='xy', scale=1, color='red', label='Re')
    ax.annotate("Ri = " + str(Ri), xy=(Ri/3, 0.1), xytext=(0.2, -Ri), textcoords='offset points', color='red')

    plt.title('Capacitor esférico\ncorte transversal')
    # Configurar los límites del eje
    ax.set_xlim(-Re*2, Re*2)
    ax.set_ylim(-Re*2, Re*2)

    # Mostrar el gráfico
    plt.axis('equal')  # Para asegurarse de que el circulo sea circulo
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def CapacitorCilindrico(Ri, Re, largo, Dielectrico):
    #Detalles
    ax.add_line(mlines.Line2D([0, Re], [-largo/2 - 0.2, -largo/2 - 0.2], color='#74cc83', linewidth=2)) #Radio Externo
    ax.annotate("Re = " + str(Re), xy=(Re/2-0.1, -largo/2 - 0.5), color='#74cc83', fontsize=8, fontname='Times New Roman')
    
    ax.add_line(mlines.Line2D([-Ri, 0], [-largo/2 - 0.1, -largo/2 - 0.1], color='#70a193', linewidth=2))#Radio Interno
    ax.annotate("Ri = " + str(Ri), xy=(-Ri/2-0.1, -largo/2 - 0.4), color='#70a193', fontsize=8, fontname='Times New Roman')

    ax.add_line(mlines.Line2D([Re +0.2, Re +0.2], [-largo/2, largo/2], color='#f59399', linewidth=2)) #Largo
    ax.annotate("largo = " + str(largo), xy=(Re +0.3, 0), color='#f59399', fontsize=8, fontname='Times New Roman')

    if Dielectrico == 1: #sin
        ax.annotate("Aire", xy=(-0.3,0.1), color='black', fontsize=12, fontname='Times New Roman')
    elif Dielectrico == 2: #completo
        dielectrico = patches.Rectangle((-Re,-largo/2), Re*2, largo, edgecolor='black', facecolor='#9999a1')
        ax.annotate("Plexiglás", xy=(-0.6,0.1), color='black', fontsize=12, fontname='Times New Roman')
        ax.add_patch(dielectrico)
    else: #mitad
        dielectrico = patches.Rectangle((-Re,-largo/2), Re*2, largo/2, linewidth=0.5, edgecolor='black', facecolor='#9999a1')
        ax.annotate("Aire", xy=(-0.3,largo/4), color='black', fontsize=12, fontname='Times New Roman')
        ax.annotate("Plexiglás", xy=(-0.6,-largo/4), color='black', fontsize=12, fontname='Times New Roman')
        ax.add_patch(dielectrico)

    cilindroExterno = patches.Rectangle((-Re,-largo/2), Re*2, largo, linewidth=2, edgecolor='black', fill=False)
    ax.add_patch(cilindroExterno)
    cilindroInterno = patches.Rectangle((-Ri,-largo/2 + 0.1), Ri*2, (largo - 0.2), linewidth=2, edgecolor='#2d2d2e', fill=False)
    ax.add_patch(cilindroInterno)

    # Configurar los límites del eje
    ax.set_xlim(-Re*2, Re*2)
    ax.set_ylim(-largo, largo)

    plt.title('Capacitor cilíndrico\ncorte transversal')
    plt.axis('equal')  # Para asegurarse de que la figura sea simétrica
    plt.show()
