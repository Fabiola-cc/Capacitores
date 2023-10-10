'''
Universidad del Valle de Guatemala
Parcial 1 - Física 3
Simulación de capacitores
 ---> Menú principal

Fabiola Contreras 22787
María José Villafuerte 22129
'''

import tkinter as tk # Libreria para creacion de interfaz grafica
from tkinter import ttk
import calc
import graficas

def clear_frame():
    for widgets in Main_page.winfo_children():
        widgets.destroy()

def main():
    clear_frame()
    tk.Label(Main_page, text = "\nEjercicio 5 - Parcial 2 - Física 3", font="Times 10 ").pack()
    tk.Label(Main_page, text = "Fabiola Contreras 22787\tMaría José Villafuerte 22129\n", font="Times 10 ").pack()
    tk.Label(Main_page, text = "¿Qué tipo de capacitor deseas calcular?", font="Times 15 ").pack()

    tk.Label(Main_page, text = "\tPlacas paralelas", font="Times 15").place(x=50, y=130)
    ttk.Button(text ="▷", command= calculo_PP).place(x=285, y=128)

    tk.Label(Main_page, text = "\tEsférico", font="Times 15").place(x=50, y=160)
    ttk.Button(text ="▷", command = calculo_E).place(x=285, y=158)

    tk.Label(Main_page, text = "\tCilíndrico", font="Times 15").place(x=50, y=190)
    ttk.Button(text ="▷", command = calculo_Cl).place(x=285, y=188)

def calculo_PP(): #Placas paralelas
    clear_frame()
    tk.Label(Main_page, text = "\n Capacitor de Placas Paralelas", font="Times 20").pack() #Titulo

    #----------------------------------Solicitud de datos-------------------------------------------------
    tk.Label(Main_page, text = "Ingresa el largo de la placa", font="Times 8").place(x=160, y=90) 
    Input_Largo_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_Largo_placa).place(x=162,y=110)
    
    tk.Label(Main_page, text = "Ingresa el ancho de la placa", font="Times 8").place(x=160, y=130)
    Input_ancho_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_ancho_placa).place(x=162,y=150)

    tk.Label(Main_page, text = "Ingresa la separación entre placas", font="Times 8").place(x=310, y=90)
    Input_separacion_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_separacion_placa).place(x=312,y=110)

    tk.Label(Main_page, text = "Ingresa el voltaje", font="Times 8").place(x=310, y=130)
    Input_Voltaje_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_Voltaje_placa).place(x=312,y=150)
    #------------------------------------------------------------------------------------------------------

    #----------------------------------Funciones de botones------------------------------------------------
    def Calculos_PP():
        largo = float(Input_Largo_placa.get())
        ancho = float(Input_ancho_placa.get())
        separacion = float(Input_separacion_placa.get())
        voltaje = float(Input_Voltaje_placa.get())

        capacitancia = calc.Capacitancia_PP(largo, ancho, separacion)
        energia = calc.energia(float(capacitancia), voltaje)
        carga = calc.Carga(float(capacitancia), voltaje)
        tk.Label(Main_page, text = "Capacitancia:  " + "{:.2e}".format(capacitancia) + " F", font="Times 8").place(x=150, y=370)
        tk.Label(Main_page, text = "Carga:  "+ "{:.2e}".format(carga) + " C", font="Times 8").place(x=150, y=400)
        tk.Label(Main_page, text = "Energía:  " + "{:.2e}".format(energia) + " J", font="Times 8").place(x=150, y=430)
        graficas.CapacitorPlacasParalelas(largo,separacion,1,Main_page)

    def Call_dec_lleno():
        largo = float(Input_Largo_placa.get())
        ancho = float(Input_ancho_placa.get())
        separacion = float(Input_separacion_placa.get())
        voltaje = float(Input_Voltaje_placa.get())

        capacitancia_total = calc.Capacitancia_PP(largo,ancho,separacion)
        carga_total = calc.Carga(capacitancia_total, voltaje)
        capacitancia_diec = calc.dielectrico_lleno(capacitancia_total,  3.40)
        carga_libre = calc.carga_libre_PP(carga_total,largo, ancho, 1, 3.40)
        carga_ligada = calc.carga_ligada_PP(carga_libre[0], 3.40)
        energia = calc.energia_full_dielectricos(capacitancia_diec,3.40,voltaje)
        tk.Label(Main_page, text = "Energía:  " + "{:.2e}".format(energia) + " J", font="Times 8").place(x=330, y=400)
        tk.Label(Main_page, text = "Capacitancia con dieléctrico: "+ "{:.2e}".format(capacitancia_diec) + " F", font="Times 8").place(x=330, y=370)
        tk.Label(Main_page, text = "Densidad de Carga Libre: "+ "{:.2e}".format(carga_libre[0]) + " C/m^2" , font="Times 8").place(x=330, y=430)
        tk.Label(Main_page, text = "Densidad de Carga Ligada: " + "{:.2e}".format(carga_ligada) + " C/m^2", font="Times 8").place(x=330, y=460)
        tk.Label(Main_page, text = "Carga:  "+ "{:.2e}".format(carga_total) + " C", font="Times 8").place(x=330, y=490)
        graficas.CapacitorPlacasParalelas(largo,separacion,2,Main_page)

    def Call_dec_mitad():
        largo = float(Input_Largo_placa.get())
        ancho = float(Input_ancho_placa.get())
        separacion = float(Input_separacion_placa.get())
        voltaje = float(Input_Voltaje_placa.get())
    
        capacitancia_total = calc.Capacitancia_PP(largo,ancho,separacion)
        carga_total = calc.Carga(capacitancia_total, voltaje)
        capacitancia_diec = calc.dielectrico_mitad(capacitancia_total, 3.40)
        carga_libre = calc.carga_libre_PP(carga_total, largo, ancho, 2, 3.40)
        carga_ligada = calc.carga_ligada_PP(carga_libre[1], 3.40)
        energia = calc.energia_mitad_dielectricos(capacitancia_diec,capacitancia_total, 3.4, voltaje)
        tk.Label(Main_page, text = "Energía:  " + "{:.2e}".format(energia) + " J", font="Times 8").place(x=330, y=370)
        tk.Label(Main_page, text = "Capacitancia con dieléctrico: "+ "{:.2e}".format(capacitancia_diec) + " F", font="Times 8").place(x=330, y=400)
        tk.Label(Main_page, text = "Densidad de Carga Libre -Aire: "+ "{:.2e}".format(carga_libre[0]) + " C/m^2", font="Times 8").place(x=330, y=430)
        tk.Label(Main_page, text = "Densidad de Carga Libre -Plexiglas: "+ "{:.2e}".format(carga_libre[1]) + " C/m^2", font="Times 8").place(x=330, y=460)
        tk.Label(Main_page, text = "Densidad de Carga Ligada: " + "{:.2e}".format(carga_ligada) + " C/m^2", font="Times 8").place(x=330, y=490)
        tk.Label(Main_page, text = "Carga:  "+ "{:.2e}".format(carga_total) + " C", font="Times 8").place(x=330, y=510)
        graficas.CapacitorPlacasParalelas(largo,separacion,3,Main_page)
    #------------------------------------------------------------------------------------------------------

    #----------------------------------Botones de resultados------------------------------------------------
    Clc_posibles=tk.Label(Main_page, text = "Cálculos:", font="Times 15 ")
    Clc_posibles.place(x=150, y=230)

    ttk.Button(text ="Resultados", command= Calculos_PP).place(x=150, y=270)
    tk.Label(Main_page, text = "Dieléctricos:", font="Times 15 ").place(x=330, y=230)
    ttk.Button(text ="Lleno", command= Call_dec_lleno).place(x=330, y=270)
    ttk.Button(text ="Medio lleno", command= Call_dec_mitad).place(x=330, y=310)

    Boton_atras = ttk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=10, y=10)
    #-------------------------------------------------------------------------------------------------------

def calculo_E(): #esfera
    clear_frame()
    tk.Label(Main_page, text = "\n Capacitor Esférico", font="Times 20").pack() #Titulo

    #----------------------------------Solicitud de datos-------------------------------------------------
    tk.Label(Main_page, text = "Ingresa el radio exterior", font="Times 8").place(x=160, y=90) 
    Input_Radio_Exterior = tk.DoubleVar()
    tk.Entry(textvariable=Input_Radio_Exterior).place(x=162,y=110)

    tk.Label(Main_page, text = "Ingresa el radio interior", font="Times 8").place(x=160, y=130)
    Input_Radio_Interior= tk.DoubleVar()
    tk.Entry(textvariable=Input_Radio_Interior).place(x=162,y=150)

    tk.Label(Main_page, text = "Ingresa el voltaje", font="Times 8").place(x=160, y=170)
    Input_Voltaje_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_Voltaje_placa).place(x=162,y=190)
    #------------------------------------------------------------------------------------------------------

    #----------------------------------Funciones de botones------------------------------------------------
    def Call_capacitancia():
        RadioE = float(Input_Radio_Exterior.get())
        RadioI = float(Input_Radio_Interior.get())
        Voltaje = float(Input_Voltaje_placa.get())

        capacitancia = calc.Capacitancia_E(RadioE,RadioI)
        energia = calc.energia(float(capacitancia), Voltaje)
        carga = calc.Carga(float(capacitancia), Voltaje)
        tk.Label(Main_page, text = "Capacitancia:  " + "{:.2e}".format(capacitancia) + " F", font="Times 8").place(x=150, y=370)
        tk.Label(Main_page, text = "Carga:  "+ "{:.2e}".format(carga) + " C", font="Times 8").place(x=150, y=400)
        tk.Label(Main_page, text = "Energía:  " + "{:.2e}".format(energia) + "J", font="Times 8").place(x=150, y=430)
        graficas.CapacitorEsferico(RadioI,RadioE,1,Main_page)

    def Call_dec_lleno():
        RadioE = float(Input_Radio_Exterior.get())
        RadioI = float(Input_Radio_Interior.get())
        Voltaje = float(Input_Voltaje_placa.get())

        capacitancia = calc.Capacitancia_E(RadioE,RadioI)
        carga = calc.Carga(float(capacitancia), Voltaje)
        capacitancia_diec = calc.dielectrico_lleno(capacitancia,  3.40)
        carga_libre = calc.carga_libre_Esfera(carga, RadioI, RadioE, 1, 3.40)
        carga_ligada = calc.carga_ligada_EC_lleno(carga_libre, 3.40)
        energia = calc.energia_full_dielectricos(capacitancia_diec,3.40,Voltaje)
        tk.Label(Main_page, text = "Energía:  " + "{:.2e}".format(energia) + " J", font="Times 8").place(x=330, y=400)
        tk.Label(Main_page, text = "Capacitancia con dieléctrico: "+ "{:.2e}".format(capacitancia_diec)+ " F", font="Times 8").place(x=330, y=370)
        tk.Label(Main_page, text = "Densidad de Carga Libre Ri: "+ "{:.2e}".format(carga_libre[0]) + " C/m^2", font="Times 8").place(x=330, y=430)
        tk.Label(Main_page, text = "Densidad de Carga Libre Re: "+ "{:.2e}".format(carga_libre[1]) + " C/m^2", font="Times 8").place(x=330, y=460)
        tk.Label(Main_page, text = "Densidad de Carga Ligada Ri: " + "{:.2e}".format(carga_ligada[0])+ " C/m^2", font="Times 8").place(x=330, y=490)
        tk.Label(Main_page, text = "Densidad de Carga Ligada Re: " + "{:.2e}".format(carga_ligada[1])+ " C/m^2", font="Times 8").place(x=330, y=520)
        tk.Label(Main_page, text = "Carga:  "+ "{:.2e}".format(carga) + " C", font="Times 8").place(x=330, y=550)
        graficas.CapacitorEsferico(RadioI,RadioE,2,Main_page)

    def Call_dec_mitad():
        RadioE = float(Input_Radio_Exterior.get())
        RadioI = float(Input_Radio_Interior.get())
        Voltaje = float(Input_Voltaje_placa.get())

        capacitancia = calc.Capacitancia_E(RadioE,RadioI)
        carga = calc.Carga(capacitancia, Voltaje)
        carga_libre = calc.carga_libre_Esfera(carga, RadioI, RadioE, 2, 3.40)
        carga_ligada = calc.carga_ligada_EC_medio(carga_libre, 3.40)
        capacitancia_diec = calc.dielectrico_mitad(capacitancia, 3.40)
        energia = calc.energia_mitad_dielectricos(capacitancia_diec,capacitancia, 3.4, Voltaje)
        tk.Label(Main_page, text = "Energía:  " + "{:.2e}".format(energia) + " J", font="Times 8").place(x=330, y=370)
        tk.Label(Main_page, text = "Capacitancia con dieléctrico: "+ "{:.2e}".format(capacitancia_diec) + " F", font="Times 8").place(x=330, y=400)
        tk.Label(Main_page, text = "Densidad de Carga Libre Ri -> Aire: "+ "{:.2e}".format(carga_libre[0])+ " C/m^2", font="Times 8").place(x=330, y=430)
        tk.Label(Main_page, text = "Densidad de Carga Libre Re -> Aire: "+ "{:.2e}".format(carga_libre[1])+ " C/m^2", font="Times 8").place(x=330, y=460)
        tk.Label(Main_page, text = "Densidad de Carga Libre Ri -> Plexiglas: "+ "{:.2e}".format(carga_libre[2])+ " C/m^2", font="Times 8").place(x=330, y=490)
        tk.Label(Main_page, text = "Densidad de Carga Libre Re -> Plexiglas: "+ "{:.2e}".format(carga_libre[3])+ " C/m^2", font="Times 8").place(x=330, y=520)
        tk.Label(Main_page, text = "Densidad de Carga Ligada Ri: " + "{:.2e}".format(carga_ligada[0])+ " C/m^2", font="Times 8").place(x=330, y=550)
        tk.Label(Main_page, text = "Densidad de Carga Ligada Re: " + "{:.2e}".format(carga_ligada[1])+ " C/m^2", font="Times 8").place(x=330, y=580)
        tk.Label(Main_page, text = "Carga:  "+ "{:.2e}".format(carga) + " C", font="Times 8").place(x=330, y=610)
        graficas.CapacitorEsferico(RadioI,RadioE,3,Main_page)

    #------------------------------------------------------------------------------------------------------

    #----------------------------------Botones de resultados------------------------------------------------
    Clc_posibles=tk.Label(Main_page, text = "Cálculos:", font="Times 15")
    Clc_posibles.place(x=150, y=230)

    ttk.Button(text ="Resultados", command= Call_capacitancia).place(x=150, y=270)
    tk.Label(Main_page, text = "Dieléctricos:", font="Times 15").place(x=330, y=230)
    ttk.Button(text ="Lleno", command= Call_dec_lleno).place(x=330, y=270)
    ttk.Button(text ="Medio lleno", command= Call_dec_mitad).place(x=330, y=310)

    Boton_atras = ttk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=10, y=10)

def calculo_Cl(): #Placas paralelas
    clear_frame()
    tk.Label(Main_page, text = "\n Capacitor Cilíndrico", font="Times 20").pack() #Titulo

    #----------------------------------Solicitud de datos-------------------------------------------------
    tk.Label(Main_page, text = "Ingresa el radio exterior", font="Times 8").place(x=160, y=90) 
    Input_Radio_Exterior = tk.DoubleVar()
    tk.Entry(textvariable=Input_Radio_Exterior).place(x=162,y=110)

    tk.Label(Main_page, text = "Ingresa el radio interior", font="Times 8").place(x=160, y=130)
    Input_Radio_Interior= tk.DoubleVar()
    tk.Entry(textvariable=Input_Radio_Interior).place(x=162,y=150)

    tk.Label(Main_page, text = "Ingresa el largo", font="Times 8").place(x=310, y=90)
    Input_Largo = tk.DoubleVar()
    tk.Entry(textvariable=Input_Largo).place(x=312,y=110)

    tk.Label(Main_page, text = "Ingresa el voltaje", font="Times 8").place(x=310, y=130)
    Input_Voltaje_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_Voltaje_placa).place(x=312,y=150)
    #------------------------------------------------------------------------------------------------------

    #----------------------------------Funciones de botones------------------------------------------------
    def Call_capacitancia_PP():
        RadioE = float(Input_Radio_Exterior.get())
        RadioI = float(Input_Radio_Interior.get())
        Largo = float(Input_Largo.get())
        Voltaje = float(Input_Voltaje_placa.get())

        capacitancia = calc.Capacitancia_C(Largo, RadioE, RadioI)
        energia = calc.energia(float(capacitancia), Voltaje)
        carga = calc.Carga(float(capacitancia), Voltaje)
        tk.Label(Main_page, text = "Capacitancia:  " + "{:.2e}".format(capacitancia)+" F", font="Times 8").place(x=150, y=370)
        tk.Label(Main_page, text = "Carga:  "+ "{:.2e}".format(carga)+ " C", font="Times 8").place(x=150, y=400)
        tk.Label(Main_page, text = "Energía:  " + "{:.2e}".format(energia)+ " J", font="Times 8").place(x=150, y=430)
        graficas.CapacitorCilindrico(RadioI,RadioE,Largo,1,Main_page)

    def Call_dec_lleno():
        RadioE = float(Input_Radio_Exterior.get())
        RadioI = float(Input_Radio_Interior.get())
        Largo = float(Input_Largo.get())
        Voltaje = float(Input_Voltaje_placa.get())

        capacitancia = calc.Capacitancia_C(Largo, RadioE, RadioI)
        carga_total = calc.Carga(capacitancia, Voltaje)
        capacitancia_diec = calc.dielectrico_lleno(capacitancia,  3.40)
        carga_libre = calc.carga_libre_Cilindro(carga_total, Largo, RadioE, RadioI, 1, 3.40)
        carga_ligada = calc.carga_ligada_EC_lleno(carga_libre, 3.40)
        energia = calc.energia_full_dielectricos(capacitancia_diec,3.40,Voltaje)
        tk.Label(Main_page, text = "Energía:  " + "{:.2e}".format(energia) + " J", font="Times 8").place(x=330, y=370)
        tk.Label(Main_page, text = "Capacitancia con dieléctrico: "+ "{:.2e}".format(capacitancia_diec)+ " F", font="Times 8").place(x=330, y=400)
        tk.Label(Main_page, text = "Densidad de Carga Libre Ri: "+ "{:.2e}".format(carga_libre[0])+ " C/m^2", font="Times 8").place(x=330, y=430)
        tk.Label(Main_page, text = "Densidad de Carga Libre Re: "+ "{:.2e}".format(carga_libre[1])+ " C/m^2", font="Times 8").place(x=330, y=460)
        tk.Label(Main_page, text = "Densidad de Carga Ligada Ri: " + "{:.2e}".format(carga_ligada[0])+ " C/m^2", font="Times 8").place(x=330, y=490)
        tk.Label(Main_page, text = "Densidad de Carga Ligada Re: " + "{:.2e}".format(carga_ligada[1])+ " C/m^2", font="Times 8").place(x=330, y=520)
        tk.Label(Main_page, text = "Carga:  "+ "{:.2e}".format(carga_total) + " C", font="Times 8").place(x=330, y=550)
        graficas.CapacitorCilindrico(RadioI,RadioE,Largo,2,Main_page)

    def Call_dec_mitad():
        RadioE = float(Input_Radio_Exterior.get())
        RadioI = float(Input_Radio_Interior.get())
        Largo = float(Input_Largo.get())
        Voltaje = float(Input_Voltaje_placa.get())

        capacitancia = calc.Capacitancia_C(Largo, RadioE, RadioI)
        carga_total = calc.Carga(capacitancia, Voltaje)
        capacitancia_diec = calc.dielectrico_mitad(capacitancia, 3.40)
        carga_libre = calc.carga_libre_Cilindro(carga_total, Largo, RadioE, RadioI, 2, 3.40)
        carga_ligada = calc.carga_ligada_EC_medio(carga_libre, 3.40)
        capacitancia_diec = calc.dielectrico_mitad(capacitancia, 3.40)
        energia = calc.energia_mitad_dielectricos(capacitancia_diec,capacitancia, 3.4, Voltaje)
        tk.Label(Main_page, text = "Energía:  " + "{:.2e}".format(energia) + " J", font="Times 8").place(x=330, y=370)
        tk.Label(Main_page, text = "Capacitancia con dieléctrico: "+ "{:.2e}".format(capacitancia_diec) + " F", font="Times 8").place(x=330, y=400)
        tk.Label(Main_page, text = "Densidad de Carga Libre Ri -> Aire: "+ "{:.2e}".format(carga_libre[0])+ " C/m^2", font="Times 8").place(x=330, y=430)
        tk.Label(Main_page, text = "Densidad de Carga Libre Re -> Aire: "+ "{:.2e}".format(carga_libre[1])+ " C/m^2", font="Times 8").place(x=330, y=460)
        tk.Label(Main_page, text = "Densidad de Carga Libre Ri -> Plexiglas: "+ "{:.2e}".format(carga_libre[2])+ " C/m^2", font="Times 8").place(x=330, y=490)
        tk.Label(Main_page, text = "Densidad de Carga Libre Re -> Plexiglas: "+ "{:.2e}".format(carga_libre[3])+ " C/m^2", font="Times 8").place(x=330, y=520)
        tk.Label(Main_page, text = "Densidad de Carga Ligada Ri: " + "{:.2e}".format(carga_ligada[0])+ " C/m^2", font="Times 8").place(x=330, y=550)
        tk.Label(Main_page, text = "Densidad de Carga Ligada Re: " + "{:.2e}".format(carga_ligada[1])+ " C/m^2", font="Times 8").place(x=330, y=580)
        tk.Label(Main_page, text = "Carga:  "+ "{:.2e}".format(carga_total) + " C", font="Times 8").place(x=330, y=610)
        graficas.CapacitorCilindrico(RadioI,RadioE,Largo,3,Main_page)
    #------------------------------------------------------------------------------------------------------

    #----------------------------------Botones de resultados------------------------------------------------
    Clc_posibles=tk.Label(Main_page, text = "Cálculos:", font="Times 15")
    Clc_posibles.place(x=150, y=230)

    ttk.Button(text ="Resultados", command= Call_capacitancia_PP).place(x=150, y=270)
    tk.Label(Main_page, text = "Dieléctricos:", font="Times 15 ").place(x=330, y=230)
    ttk.Button(text ="Lleno", command= Call_dec_lleno).place(x=330, y=270)
    ttk.Button(text ="Medio lleno", command= Call_dec_mitad).place(x=330, y=310)

    Boton_atras = ttk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=10, y=10)

if __name__ == "__main__":
    Main_page = tk.Tk()
    Main_page.geometry("1100x650")
    main()
    Main_page.mainloop()