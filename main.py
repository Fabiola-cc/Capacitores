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
    tk.Button(text ="▷", command = calculo_E).place(x=240, y=158)

    tk.Label(Main_page, text = "\tCilíndrico", font="Times 15").place(x=5, y=190)
    tk.Button(text ="▷", command = calculo_Cl).place(x=240, y=188)

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
    def Call_capacitancia_PP():
        capacitancia = calc.Capacitancia_PP(float(Input_Largo_placa.get()), float(Input_ancho_placa.get()), float(Input_separacion_placa.get()))
        energia = calc.energia(float(capacitancia), float(Input_Voltaje_placa.get()))
        carga = calc.Carga(float(capacitancia), float(Input_Voltaje_placa.get()))
        tk.Label(Main_page, text = "Capacitancia:  " + "{:.3e}".format(capacitancia), font="Times 8").place(x=30, y=300)
        tk.Label(Main_page, text = "Carga:  "+ "{:.3e}".format(carga) , font="Times 8").place(x=30, y=330)
        tk.Label(Main_page, text = "Energía:  " + "{:.3e}".format(energia), font="Times 8").place(x=30, y=360)
        graficas.CapacitorPlacasParalelas(Input_Largo_placa.get(),Input_separacion_placa.get(),1)
        return capacitancia

    def Call_dec_lleno():
        capacitancia_total = calc.Capacitancia_PP(Input_Largo_placa.get(),Input_ancho_placa.get(),Input_separacion_placa.get())
        carga_total = calc.Carga(capacitancia_total, float(Input_Voltaje_placa.get()))
        capacitancia_diec = calc.dielectrico_lleno(capacitancia_total,  3.40)
        carga_libre = calc.carga_libre_PP(carga_total,float(Input_Largo_placa.get()), float(Input_ancho_placa.get()))
        carga_ligada = calc.carga_ligada(carga_libre, 1)
        tk.Label(Main_page, text = "Capacitiacia:"+ "{:.3e}".format(capacitancia_diec), font="Times 8").place(x=330, y=290)
        tk.Label(Main_page, text = "Carga Libre"+ "{:.3e}".format(carga_libre) , font="Times 8").place(x=330, y=320)
        tk.Label(Main_page, text = "Carga Ligada" + "{:.3e}".format(carga_ligada), font="Times 8").place(x=330, y=350)
        graficas.CapacitorPlacasParalelas(Input_Largo_placa.get(),Input_separacion_placa.get(),2)

        return 0 

    def Call_dec_mitad():
        capacitancia_total = calc.Capacitancia_PP(Input_Largo_placa.get(),Input_ancho_placa.get(),Input_separacion_placa.get())
        carga_total = calc.Carga(capacitancia_total, float(Input_Voltaje_placa.get()))
        capacitancia_diec = calc.dielectrico_mitad(capacitancia_total, 3.40)
        carga_libre = calc.carga_libre_PP(carga_total,float(Input_Largo_placa.get()), float(Input_ancho_placa.get()))
        carga_ligada = calc.carga_ligada(carga_libre, 3.40)
        tk.Label(Main_page, text = "Capacitiacia:"+ "{:.3e}".format(capacitancia_diec), font="Times 8").place(x=330, y=290)
        tk.Label(Main_page, text = "Carga Libre"+ "{:.3e}".format(carga_libre) , font="Times 8").place(x=330, y=320)
        tk.Label(Main_page, text = "Carga Ligada" + "{:.3e}".format(carga_ligada), font="Times 8").place(x=330, y=350)
        graficas.CapacitorPlacasParalelas(Input_Largo_placa.get(),Input_separacion_placa.get(),3)


    #------------------------------------------------------------------------------------------------------

    #----------------------------------Botones de resultados------------------------------------------------
    Clc_posibles=tk.Label(Main_page, text = "Cálculos:", font="Times 15 italic")
    Clc_posibles.place(x=15, y=230)

    tk.Button(text ="Resultados", command= Call_capacitancia_PP).place(x=15, y=270)
    tk.Label(Main_page, text = "Dieléctricos:", font="Times 15 italic").place(x=225, y=230)
    tk.Button(text ="Lleno", command= Call_dec_lleno).place(x=225, y=270)
    tk.Button(text ="Medio lleno", command= Call_dec_mitad).place(x=225, y=310)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=10, y=10)
    #-------------------------------------------------------------------------------------------------------


def calculo_E(): #esfera
    clear_frame()
    tk.Label(Main_page, text = "\n Capacitor Esférico", font="Times 20").pack() #Titulo

    #----------------------------------Solicitud de datos-------------------------------------------------
    tk.Label(Main_page, text = "Ingresa el radio exterior", font="Times 8").place(x=10, y=60) 
    Input_Radio_Exterior = tk.DoubleVar()
    tk.Entry(textvariable=Input_Radio_Exterior).place(x=10,y=80)

    tk.Label(Main_page, text = "Ingresa el radio interior", font="Times 8").place(x=10, y=100)
    Input_Radio_Interior= tk.DoubleVar()
    tk.Entry(textvariable=Input_Radio_Interior).place(x=10,y=120)

    tk.Label(Main_page, text = "Ingresa el voltaje", font="Times 8").place(x=10, y=140)
    Input_Voltaje_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_Voltaje_placa).place(x=10,y=160)
    #------------------------------------------------------------------------------------------------------

    #----------------------------------Funciones de botones------------------------------------------------
    def Call_capacitancia():
        capacitancia = calc.Capacitancia_E(Input_Radio_Exterior.get,Input_Radio_Interior.get)
        energia = calc.energia(float(capacitancia), float(Input_Voltaje_placa.get()))
        carga = calc.Carga(float(capacitancia), float(Input_Voltaje_placa.get()))
        tk.Label(Main_page, text = "Capacitancia:  " + "{:.3e}".format(capacitancia), font="Times 8").place(x=30, y=300)
        tk.Label(Main_page, text = "Carga:  "+ "{:.3e}".format(carga) , font="Times 8").place(x=30, y=330)
        tk.Label(Main_page, text = "Energía:  " + "{:.3e}".format(energia), font="Times 8").place(x=30, y=360)
        graficas.CapacitorEsferico(Input_Radio_Interior.get(),Input_Radio_Exterior.get(),1)

        return capacitancia

    def Call_dec_lleno():
        capacitancia = calc.Capacitancia_E(Input_Radio_Exterior.get,Input_Radio_Interior.get)
        carga = calc.Carga(float(capacitancia), float(Input_Voltaje_placa.get()))
        capacitancia_diec = calc.dielectrico_lleno(capacitancia,  3.40)
       # carga_libre = calc.carga_libre_PP(carga,float(Input_Largo_placa.get()), float(Input_ancho_placa.get()))
       # carga_ligada = calc.carga_ligada(carga_libre, 1)
        tk.Label(Main_page, text = "Capacitiacia:"+ "{:.3e}".format(capacitancia_diec), font="Times 8").place(x=330, y=290)
       # tk.Label(Main_page, text = "Carga Libre"+ "{:.3e}".format(carga_libre) , font="Times 8").place(x=330, y=320)
       # tk.Label(Main_page, text = "Carga Ligada" + "{:.3e}".format(carga_ligada), font="Times 8").place(x=330, y=350)
        graficas.CapacitorEsferico(Input_Radio_Interior.get(),Input_Radio_Exterior.get(),2)

        return 0 


    def Call_dec_mitad():
        capacitancia = calc.Capacitancia_E(Input_Radio_Exterior.get,Input_Radio_Interior.get)
        carga_total = calc.Carga(capacitancia, float(Input_Voltaje_placa.get()))
        capacitancia_diec = calc.dielectrico_mitad(capacitancia, 3.40)
       # carga_libre = calc.carga_libre_PP(carga_total,float(Input_Largo_placa.get()), float(Input_ancho_placa.get()))
       # carga_ligada = calc.carga_ligada(carga_libre, 3.40)
        tk.Label(Main_page, text = "Capacitiacia:"+ "{:.3e}".format(capacitancia_diec), font="Times 8").place(x=330, y=290)
       # tk.Label(Main_page, text = "Carga Libre"+ "{:.3e}".format(carga_libre) , font="Times 8").place(x=330, y=320)
       # tk.Label(Main_page, text = "Carga Ligada" + "{:.3e}".format(carga_ligada), font="Times 8").place(x=330, y=350)
        graficas.CapacitorEsferico(Input_Radio_Interior.get(),Input_Radio_Exterior.get(),3)

    #------------------------------------------------------------------------------------------------------

    #----------------------------------Botones de resultados------------------------------------------------
    Clc_posibles=tk.Label(Main_page, text = "Cálculos:", font="Times 15 italic")
    Clc_posibles.place(x=15, y=230)

    tk.Button(text ="Resultados", command= Call_capacitancia).place(x=15, y=270)
    tk.Label(Main_page, text = "Dieléctricos:", font="Times 15 italic").place(x=225, y=230)
    tk.Button(text ="Lleno", command= Call_dec_lleno).place(x=225, y=270)
    tk.Button(text ="Medio lleno", command= Call_dec_mitad).place(x=225, y=310)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=10, y=10)

def calculo_Cl(): #Placas paralelas
    clear_frame()
    tk.Label(Main_page, text = "\n Capacitor Cilíndrico", font="Times 20").pack() #Titulo

    #----------------------------------Solicitud de datos-------------------------------------------------
    tk.Label(Main_page, text = "Ingresa el radio exterior", font="Times 8").place(x=10, y=60) 
    Input_Radio_Exterior = tk.DoubleVar()
    tk.Entry(textvariable=Input_Radio_Exterior).place(x=10,y=80)

    tk.Label(Main_page, text = "Ingresa el radio interior", font="Times 8").place(x=10, y=100)
    Input_Radio_Interior= tk.DoubleVar()
    tk.Entry(textvariable=Input_Radio_Interior).place(x=10,y=120)

    tk.Label(Main_page, text = "Ingresa el largo", font="Times 8").place(x=10, y=140)
    Input_Largo = tk.DoubleVar()
    tk.Entry(textvariable=Input_Largo).place(x=10,y=160)

    tk.Label(Main_page, text = "Ingresa el voltaje", font="Times 8").place(x=10, y=180)
    Input_Voltaje_placa = tk.DoubleVar()
    tk.Entry(textvariable=Input_Voltaje_placa).place(x=10,y=200)
    #------------------------------------------------------------------------------------------------------

    #----------------------------------Funciones de botones------------------------------------------------
    def Call_capacitancia_PP():
        capacitancia = calc.Capacitancia_C(Input_Largo.get(), Input_Radio_Exterior.get(),Input_Radio_Interior.get())
        energia = calc.energia(float(capacitancia), float(Input_Voltaje_placa.get()))
        carga = calc.Carga(float(capacitancia), float(Input_Voltaje_placa.get()))
        tk.Label(Main_page, text = "Capacitancia:  " + "{:.3e}".format(capacitancia), font="Times 8").place(x=30, y=300)
        tk.Label(Main_page, text = "Carga:  "+ "{:.3e}".format(carga) , font="Times 8").place(x=30, y=330)
        tk.Label(Main_page, text = "Energía:  " + "{:.3e}".format(energia), font="Times 8").place(x=30, y=360)
        graficas.CapacitorCilindrico(Input_Radio_Interior.get(),Input_Radio_Exterior.get(),Input_Largo.get(),1)
        return capacitancia

    def Call_dec_lleno():
        capacitancia = calc.Capacitancia_C(Input_Largo, Input_Radio_Exterior,Input_Radio_Interior)
        carga_total = calc.Carga(capacitancia, float(Input_Voltaje_placa.get()))
        capacitancia_diec = calc.dielectrico_lleno(capacitancia,  3.40)
       # carga_libre = calc.carga_libre_PP(carga_total,float(Input_Largo_placa.get()), float(Input_ancho_placa.get()))
       # carga_ligada = calc.carga_ligada(carga_libre, 1)
        tk.Label(Main_page, text = "Capacitiacia:"+ "{:.3e}".format(capacitancia_diec), font="Times 8").place(x=330, y=290)
       # tk.Label(Main_page, text = "Carga Libre"+ "{:.3e}".format(carga_libre) , font="Times 8").place(x=330, y=320)
       # tk.Label(Main_page, text = "Carga Ligada" + "{:.3e}".format(carga_ligada), font="Times 8").place(x=330, y=350)
        graficas.CapacitorCilindrico(Input_Radio_Interior.get(),Input_Radio_Exterior.get(),Input_Largo.get(),2)
        return 0 

    def Call_dec_mitad():
        capacitancia = calc.Capacitancia_C(Input_Largo, Input_Radio_Exterior,Input_Radio_Interior)
        carga_total = calc.Carga(capacitancia, float(Input_Voltaje_placa.get()))
        capacitancia_diec = calc.dielectrico_mitad(capacitancia, 3.40)
        #carga_libre = calc.carga_libre_PP(carga_total,float(Input_Largo_placa.get()), float(Input_ancho_placa.get()))
        #carga_ligada = calc.carga_ligada(carga_libre, 3.40)
        tk.Label(Main_page, text = "Capacitiacia:"+ "{:.3e}".format(capacitancia_diec), font="Times 8").place(x=330, y=290)
        #tk.Label(Main_page, text = "Carga Libre"+ "{:.3e}".format(carga_libre) , font="Times 8").place(x=330, y=320)
        #tk.Label(Main_page, text = "Carga Ligada" + "{:.3e}".format(carga_ligada), font="Times 8").place(x=330, y=350)
        graficas.CapacitorCilindrico(Input_Radio_Interior.get(),Input_Radio_Exterior.get(),Input_Largo.get(),3)
    #------------------------------------------------------------------------------------------------------

    #----------------------------------Botones de resultados------------------------------------------------
    Clc_posibles=tk.Label(Main_page, text = "Cálculos:", font="Times 15 italic")
    Clc_posibles.place(x=15, y=230)

    tk.Button(text ="Resultados", command= Call_capacitancia_PP).place(x=15, y=270)
    tk.Label(Main_page, text = "Dieléctricos:", font="Times 15 italic").place(x=225, y=230)
    tk.Button(text ="Lleno", command= Call_dec_lleno).place(x=225, y=270)
    tk.Button(text ="Medio lleno", command= Call_dec_mitad).place(x=225, y=310)
    tk.Button(text ="Medio lleno", command= Call_dec_mitad).place(x=225, y=310)

    Boton_atras = tk.Button(text ="Regresar", command= main)
    Boton_atras.place(x=10, y=10)
Main_page = tk.Tk()
Main_page.geometry("550x450")
main()
Main_page.mainloop()