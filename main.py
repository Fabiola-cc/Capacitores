'''
Universidad del Valle de Guatemala
Parcial 1 - Física 3
Simulación de capacitancias
 ---> Menú principal

Fabiola Contreras 22787
María José Villafuerte 22129
'''

import tkinter as tk # Libreria para creacion de interfaz grafica
import calc
import graficas

def clear_frame():
    for widgets in Main_page.winfo_children():
      widgets.destroy()

def main():
    clear_frame()
    tk.Label(Main_page, text = "\nEjercicio 5 - Parcial 2 - Física 3", font="Times 10 italic").pack()
    tk.Label(Main_page, text = "Fabiola Contreras 22787\tMaría José Villafuerte 22129\n", font="Times 10 italic").pack()
    tk.Label(Main_page, text = "¿Qué tipo de capacitor deseas calcular?", font="Times 15 italic").pack()

    tk.Label(Main_page, text = "\t Placas paralelas", font="Times 15").place(x=5, y=130)
    tk.Button(text ="▷", command= calculo_PP).place(x=240, y=128)

    tk.Label(Main_page, text = "\t Esférico", font="Times 15").place(x=5, y=160)
    tk.Button(text ="▷", command = calculo_E).place(x=240, y=158)

    tk.Label(Main_page, text = "\t Cilíndrico", font="Times 15").place(x=5, y=190)
    tk.Button(text ="▷", command = calculo_Cl).place(x=240, y=188)

def calculo_PP():
    clear_frame()
    tk.Label(Main_page, text = " \nPlacas Paralelas", font="Times 20").pack()

    tk.Label(Main_page, text = "Ingresa el largo de la placa", font="Times 8").place(x=10, y=60)
    Input_Largo_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_Largo_placa).place(x=10,y=80)

    tk.Label(Main_page, text = "Ingresa el ancho de la placa", font="Times 8").place(x=10, y=100)
    Input_ancho_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_ancho_placa).place(x=10,y=120)

    tk.Label(Main_page, text = "Ingresa la separación entre placas", font="Times 8").place(x=10, y=140)
    Input_separacion_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_separacion_placa).place(x=10,y=160)

    tk.Label(Main_page, text = "Ingresa el voltaje", font="Times 8").place(x=10, y=140)
    Input_Voltaje_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_Voltaje_placa).place(x=10,y=200)

    def Call_calculation():
        capacitancia = calc.Capacitancia_PP(float(Input_Largo_placa.get()), float(Input_ancho_placa.get()), float(Input_separacion_placa.get()))
       # graficas.Grafica_CampoE_LineasDeCarga(float(Input_Distancia.get()), E)

    def Call_energia():
        energia = calc.energia(float(Call_calculation), float(Input_Voltaje_placa.get()))

    def Call_carga():
        carga = calc.Carga(float(Call_calculation), float(Input_Voltaje_placa.get()))

    def Call_dec_vacio():
        capacitancia_diec = calc.dielectrico(float(Call_calculation), 1)
        carga_libre = calc.carga_libre_PP(float(Call_carga()),float(Input_Largo_placa.get()), float(Input_ancho_placa.get()))
        carga_ligada = calc.carga_ligada(carga_libre, 1)
 

    #NO RECUERDO QUE CONSTANTE USAR
    def Call_dec_mitad():
        capacitancia_diec = calc.dielectrico(float(Call_calculation), 3.83)
        carga_libre = calc.carga_libre_PP(float(Call_carga()),float(Input_Largo_placa.get()), float(Input_ancho_placa.get()))
        carga_ligada = calc.carga_ligada(carga_libre, 3.83)
 
    Clc_posibles=tk.Label(Main_page, text = "Cálculos:", font="Times 15 italic")
    Clc_posibles.place(x=15, y=230)

    Boton_listo = tk.Button(text ="Capacitancia", command= Call_calculation)
    Boton_listo.place(x=15, y=270)

    Boton_listo = tk.Button(text ="Carga", command= Call_carga)
    Boton_listo.place(x=15, y=300)

    Boton_listo = tk.Button(text ="Energía", command= Call_energia)
    Boton_listo.place(x=15, y=330)

    Dielect=tk .Label(Main_page, text = "Dieléctricos:", font="Times 15 italic")
    Dielect.place(x=200, y=250)

    Boton_listo = tk.Button(text ="Vacio", command= Call_dec_vacio)
    Boton_listo.place(x=200, y=280)

    Boton_listo = tk.Button(text ="Medio lleno", command= Call_dec_mitad)
    Boton_listo.place(x=200, y=310)


    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=10, y=10)
    
def calculo_E():
    clear_frame()
    tk.Label(Main_page, text = "\nAnillo de carga", font="Times 20").pack()

    tk.Label(Main_page, text = "Ingresa el radio del anillo", font="Times 8").place(x=10, y=60)
    Input_radio = tk.DoubleVar()
    tk.Entry(textvariable=Input_radio).place(x=10,y=80)

    tk.Label(Main_page, text = "Ingresa la carga del elemento", font="Times 8").place(x=10, y=100)
    Input_Carga = tk.DoubleVar()
    tk.Entry(textvariable=Input_Carga).place(x=10,y=120)

    tk.Label(Main_page, text = "Ingresa la distancia 'x' entre la partícula y el anillo", font="Times 8").place(x=10, y=140)
    Input_Distancia = tk.DoubleVar()
    tk.Entry(textvariable=Input_Distancia).place(x=10,y=160)

    def Call_calculation():
        E = calc.Funcion_ecuacion_CampoE_anillo(float(Input_Carga.get()), float(Input_Distancia.get()), float(Input_radio.get()))
        graficas.Grafica_CampoE_anillo(float(Input_radio.get()), float(Input_Distancia.get()), E)

    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=190)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=105, y=190)

def calculo_Cl():
    clear_frame()
    tk.Label(Main_page, text = "\nDisco", font="Times 20").pack()
    
    tk.Label(Main_page, text = "Ingresa el radio del disco", font="Times 8").place(x=10, y=60)
    Input_radio = tk.DoubleVar()
    tk.Entry(textvariable=Input_radio).place(x=10,y=80)

    tk.Label(Main_page, text = "Ingresa la carga del elemento", font="Times 8").place(x=10, y=100)
    Input_Carga = tk.DoubleVar()
    tk.Entry(textvariable=Input_Carga).place(x=10,y=120)

    tk.Label(Main_page, text = "Ingresa la distancia 'x' entre la partícula y el disco", font="Times 8").place(x=10, y=140)
    Input_Distancia = tk.DoubleVar()
    tk.Entry(textvariable=Input_Distancia).place(x=10,y=160)

    def Call_calculation():
        E = calc.Funcion_ecuacion_CampoE_Disco(float(Input_Carga.get()), float(Input_Distancia.get()), float(Input_radio.get()))
        graficas.Grafica_CampoE_Disco(float(Input_radio.get()), float(Input_Distancia.get()), E)

    Boton_listo = tk.Button(text ="Listo", command= Call_calculation)
    Boton_listo.place(x=15, y=190)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=105, y=190)

Main_page = tk.Tk()
Main_page.geometry("550x450")
main()
Main_page.mainloop()

