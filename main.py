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

    tk.Label(Main_page, text = "\tPlacas paralelas", font="Times 15").place(x=5, y=130)
    tk.Button(text ="▷", command= calculo_PP).place(x=240, y=128)

    tk.Label(Main_page, text = "\tEsférico", font="Times 15").place(x=5, y=160)
    #tk.Button(text ="▷", command = calculo_E).place(x=240, y=158)

    tk.Label(Main_page, text = "\tCilíndrico", font="Times 15").place(x=5, y=190)
    #tk.Button(text ="▷", command = calculo_Cl).place(x=240, y=188)

def calculo_PP(): #Placas paralelas
    clear_frame()
    tk.Label(Main_page, text = "\n Capacitor de Placas Paralelas", font="Times 20").pack() #Titulo

    #----------------------------------Solicitud de datos-------------------------------------------------
    tk.Label(Main_page, text = "Ingresa el largo de la placa", font="Times 8").place(x=10, y=60) 
    Input_Largo_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_Largo_placa).place(x=10,y=80)

    tk.Label(Main_page, text = "Ingresa el ancho de la placa", font="Times 8").place(x=10, y=100)
    Input_ancho_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_ancho_placa).place(x=10,y=120)

    tk.Label(Main_page, text = "Ingresa la separación entre placas", font="Times 8").place(x=10, y=140)
    Input_separacion_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_separacion_placa).place(x=10,y=160)

    tk.Label(Main_page, text = "Ingresa el voltaje", font="Times 8").place(x=10, y=180)
    Input_Voltaje_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_Voltaje_placa).place(x=10,y=200)
    #------------------------------------------------------------------------------------------------------

    #----------------------------------Funciones de botones------------------------------------------------
    def Call_capacitancia():
        capacitancia = calc.Capacitancia_PP(float(Input_Largo_placa.get()), float(Input_ancho_placa.get()), float(Input_separacion_placa.get()))
        return capacitancia

    def Call_energia():
        energia = calc.energia(float(Call_capacitancia()), float(Input_Voltaje_placa.get()))
        return energia

    def Call_carga():
        carga = calc.Carga(float(Call_capacitancia()), float(Input_Voltaje_placa.get()))
        return carga

    def Call_dec_vacio():
        capacitancia_diec = calc.dielectrico(float(Call_capacitancia()), 1)
        carga_libre = calc.carga_libre_PP(float(Call_carga()),float(Input_Largo_placa.get()), float(Input_ancho_placa.get()))
        carga_ligada = calc.carga_ligada(carga_libre, 1)
 
    def Call_dec_mitad():
        capacitancia_diec = calc.dielectrico(float(Call_capacitancia()), 3.40)
        carga_libre = calc.carga_libre_PP(float(Call_carga()),float(Input_Largo_placa.get()), float(Input_ancho_placa.get()))
        carga_ligada = calc.carga_ligada(carga_libre, 3.40)
    #------------------------------------------------------------------------------------------------------

    #----------------------------------Botones de resultados------------------------------------------------
    Clc_posibles=tk.Label(Main_page, text = "Cálculos:", font="Times 15 italic")
    Clc_posibles.place(x=15, y=230)

    tk.Button(text ="Capacitancia", command= Call_capacitancia).place(x=15, y=270)
    tk.Button(text ="Carga", command= Call_carga).place(x=15, y=300)
    tk.Button(text ="Energía", command= Call_energia).place(x=15, y=330)
    tk.Label(Main_page, text = "Dieléctricos:", font="Times 15 italic").place(x=200, y=250)
    tk.Button(text ="Vacio", command= Call_dec_vacio).place(x=200, y=280)
    tk.Button(text ="Medio lleno", command= Call_dec_mitad).place(x=200, y=310)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=10, y=10)
    #-------------------------------------------------------------------------------------------------------

Main_page = tk.Tk()
Main_page.geometry("550x450")
main()
Main_page.mainloop()