'''PROYECTO III FIORELLA ZELAYA'''


## modulos ##

import pickle
import tkinter
from tkinter import *
from tkinter import messagebox
import random


## funciones ##
def jugar():
    
    def presionar(fila,columna):
        pass

    def presionar_numero(num):
        pass

    def iniciar():
        nombre = entryNombre.get()
        if nombre == "":
            messagebox.showerror("Error","No ha registrado el nombre del jugador")
            return
        variableIniciar = 1

    def borrarJugada():
        pass

    def terminar():
        pass

    def borrar():
        pass

    def Top10():
        pass

    def Guardar():
        pass

    def Cargar():
        pass

    def timer():
        pass

    def horaActualizar():
        pass

    def cerrar():
        juego.destroy()
        raiz.deiconify()
        return
    
    raiz.withdraw()
    juego = Toplevel(raiz)
    juego.resizable(False,False)
    juego.geometry("600x600")
    juego.configure(bg="#292929")
    juego.title("Futoshiki")

    #variables utiles
    variableIniciar = 0

    futoshikitxt = Label(juego,text="FUTOSHIKI",font=("cambria", 24),bg="firebrick",fg="white",relief=GROOVE).place(x=200,y=5,width=200)

    for i,level in enumerate(configuracion[0]):
        if i == 0 and level == 1:
            nivel = "FÁCIL"
            nivelJuego = 0
        if i == 1 and level == 1:
            nivel = "INTERMEDIO"
            nivelJuego = 1
        if i == 2 and level == 1:
            nivel = "DIFÍCIL"
            nivelJuego = 2
    niveltxt = Label(juego,text="NIVEL "+nivel,bg="#292929",fg="white").place(x=260,y=55)
    txt = Label(juego,text="Nombre del jugador:",bg="#292929",fg="white").place(x=10,y=90)
    nombre = StringVar()
    entryNombre = Entry(juego,textvariable=nombre).place(x=140,y=90,width=300)

    #cuadricula
    btn00 = Button(juego,relief=RIDGE,command=lambda: presionar(0,0))
    btn01 = Button(juego,relief=RIDGE,command=lambda: presionar(0,1))
    btn02 = Button(juego,relief=RIDGE,command=lambda: presionar(0,2))
    btn03 = Button(juego,relief=RIDGE,command=lambda: presionar(0,3))
    btn04 = Button(juego,relief=RIDGE,command=lambda: presionar(0,4))
    
    btn10 = Button(juego,relief=RIDGE,command=lambda: presionar(1,0))
    btn11 = Button(juego,relief=RIDGE,command=lambda: presionar(1,1))
    btn12 = Button(juego,relief=RIDGE,command=lambda: presionar(1,2))
    btn13 = Button(juego,relief=RIDGE,command=lambda: presionar(1,3))
    btn14 = Button(juego,relief=RIDGE,command=lambda: presionar(1,4))

    btn20 = Button(juego,relief=RIDGE,command=lambda: presionar(2,0))
    btn21 = Button(juego,relief=RIDGE,command=lambda: presionar(2,1))
    btn22 = Button(juego,relief=RIDGE,command=lambda: presionar(2,2))
    btn23 = Button(juego,relief=RIDGE,command=lambda: presionar(2,3))
    btn24 = Button(juego,relief=RIDGE,command=lambda: presionar(2,4))

    btn30 = Button(juego,relief=RIDGE,command=lambda: presionar(3,0))
    btn31 = Button(juego,relief=RIDGE,command=lambda: presionar(3,1))
    btn32 = Button(juego,relief=RIDGE,command=lambda: presionar(3,2))
    btn33 = Button(juego,relief=RIDGE,command=lambda: presionar(3,3))
    btn34 = Button(juego,relief=RIDGE,command=lambda: presionar(3,4))

    btn40 = Button(juego,relief=RIDGE,command=lambda: presionar(4,0))
    btn41 = Button(juego,relief=RIDGE,command=lambda: presionar(4,1))
    btn42 = Button(juego,relief=RIDGE,command=lambda: presionar(4,2))
    btn43 = Button(juego,relief=RIDGE,command=lambda: presionar(4,3))
    btn44 = Button(juego,relief=RIDGE,command=lambda: presionar(4,4))

    objetosBotones = [[(btn00),(btn01),(btn02),(btn03),(btn04)],\
                      [(btn10),(btn11),(btn12),(btn13),(btn14)],\
                      [(btn20),(btn21),(btn22),(btn23),(btn24)],\
                      [(btn30),(btn31),(btn32),(btn33),(btn34)],\
                      [(btn40),(btn41),(btn42),(btn43),(btn44)]]

            #botones numeros

    btnnum1 = Button(juego,text="1",bg="violet red",command=lambda: presionar_numero(1))
    btnnum2 = Button(juego,text="2",bg="orange",command=lambda: presionar_numero(2))
    btnnum3 = Button(juego,text="3",bg="dark turquoise",command=lambda: presionar_numero(3))
    btnnum4 = Button(juego,text="4",bg="orchid",command=lambda: presionar_numero(4))
    btnnum5 = Button(juego,text="5",bg="gold",command=lambda: presionar_numero(5))
    

    #botones generales

    btnIniciar = Button(juego,text="INICIAR\nJUEGO",bg="violet red",command=iniciar)
    btnBorrarJugada = Button(juego,text="BORRAR\nJUGADA",bg="orange",command=iniciar)
    btnTerminar = Button(juego,text="TERMINAR\nJUEGO",bg="dark turquoise",command=iniciar)
    btnBorrar = Button(juego,text="BORRAR\nJUEGO",bg="orchid",command=iniciar)
    btnTop10 = Button(juego,text="TOP\n10",bg="gold",command=iniciar)

    btnGuardar= Button(juego,text="GUARDAR JUEGO",command=iniciar)
    btnCargar = Button(juego,text="CARGAR JUEGO",command=iniciar)

    btnIniciar.place(x=20,y=430,width=100)
    btnBorrarJugada.place(x=135,y=430,width=100)
    btnTerminar.place(x=249,y=430,width=100)
    btnBorrar.place(x=365,y=430,width=100)
    btnTop10.place(x=480,y=430,width=100)

    btnGuardar.place(x=269,y=520,width=100)
    btnCargar.place(x=395,y=520,width=100)

    if configuracion[2][1] == 1:

        btn00.place(x=195,y=125,width=40,height=40)
        btn01.place(x=250,y=125,width=40,height=40)
        btn02.place(x=305,y=125,width=40,height=40)
        btn03.place(x=360,y=125,width=40,height=40)
        btn04.place(x=415,y=125,width=40,height=40)

        btn10.place(x=195,y=180,width=40,height=40)
        btn11.place(x=250,y=180,width=40,height=40)
        btn12.place(x=305,y=180,width=40,height=40)
        btn13.place(x=360,y=180,width=40,height=40)
        btn14.place(x=415,y=180,width=40,height=40)

        btn20.place(x=195,y=235,width=40,height=40)
        btn21.place(x=250,y=235,width=40,height=40)
        btn22.place(x=305,y=235,width=40,height=40)
        btn23.place(x=360,y=235,width=40,height=40)
        btn24.place(x=415,y=235,width=40,height=40)

        btn30.place(x=195,y=290,width=40,height=40)
        btn31.place(x=250,y=290,width=40,height=40)
        btn32.place(x=305,y=290,width=40,height=40)
        btn33.place(x=360,y=290,width=40,height=40)
        btn34.place(x=415,y=290,width=40,height=40)

        btn40.place(x=195,y=345,width=40,height=40)
        btn41.place(x=250,y=345,width=40,height=40)
        btn42.place(x=305,y=345,width=40,height=40)
        btn43.place(x=360,y=345,width=40,height=40)
        btn44.place(x=415,y=345,width=40,height=40)

        btnnum1.place(x=140,y=135,width=30)
        btnnum2.place(x=140,y=190,width=30)
        btnnum3.place(x=140,y=245,width=30)
        btnnum4.place(x=140,y=300,width=30)
        btnnum5.place(x=140,y=355,width=30)

        coordenadas = [[(195,125),(250,125),(305,125),(360,125),(415,125)],\
                       [(195,180),(250,180),(305,180),(360,180),(415,180)],\
                       [(195,235),(250,235),(305,235),(360,235),(415,235)],\
                        [(195,290),(250,290),(305,290),(360,290),(415,290)],\
                        [(195,345),(250,345),(305,345),(360,345),(415,345)]]

        
    else:

        btn00.place(x=140,y=125,width=40,height=40)
        btn01.place(x=195,y=125,width=40,height=40)
        btn02.place(x=250,y=125,width=40,height=40)
        btn03.place(x=305,y=125,width=40,height=40)
        btn04.place(x=360,y=125,width=40,height=40)

        btn10.place(x=140,y=180,width=40,height=40)
        btn11.place(x=195,y=180,width=40,height=40)
        btn12.place(x=250,y=180,width=40,height=40)
        btn13.place(x=305,y=180,width=40,height=40)
        btn14.place(x=360,y=180,width=40,height=40)

        btn20.place(x=140,y=235,width=40,height=40)
        btn21.place(x=195,y=235,width=40,height=40)
        btn22.place(x=250,y=235,width=40,height=40)
        btn23.place(x=305,y=235,width=40,height=40)
        btn24.place(x=360,y=235,width=40,height=40)

        btn30.place(x=140,y=290,width=40,height=40)
        btn31.place(x=195,y=290,width=40,height=40)
        btn32.place(x=250,y=290,width=40,height=40)
        btn33.place(x=305,y=290,width=40,height=40)
        btn34.place(x=360,y=290,width=40,height=40)

        btn40.place(x=140,y=345,width=40,height=40)
        btn41.place(x=195,y=345,width=40,height=40)
        btn42.place(x=250,y=345,width=40,height=40)
        btn43.place(x=305,y=345,width=40,height=40)
        btn44.place(x=360,y=345,width=40,height=40)

        btnnum1.place(x=430,y=135,width=30)
        btnnum2.place(x=430,y=190,width=30)
        btnnum3.place(x=430,y=245,width=30)
        btnnum4.place(x=430,y=300,width=30)
        btnnum5.place(x=430,y=355,width=30)

        btnGuardar.place(x=190,y=520,width=100)
        btnCargar.place(x=305,y=520,width=100)

        coordenadas = [[(140,125),(195,125),(250,125),(305,125),(360,125)],\
                       [(140,180),(195,180),(250,180),(305,180),(360,180)],\
                       [(140,235),(195,235),(250,235),(305,235),(360,235)],\
                        [(140,290),(195,290),(250,290),(305,290),(360,290)],\
                        [(140,345),(195,345),(250,345),(305,345),(360,345)]]
        
    if configuracion[1][1] == 1:
        pass
    else:
        txthoras0 = Label(juego,text="Horas",relief=GROOVE).place(x=20,y=500)
        txtminutos0 = Label(juego,text="Minutos",relief=GROOVE).place(x=56,y=500)
        txtsegundos0 = Label(juego,text="Segundos",relief=GROOVE).place(x=106,y=500)
        txthoras = Label(juego,relief=GROOVE,bg="#F0F0F0").place(x=20,y=521,width=38,height=40)
        txtminutos = Label(juego,relief=GROOVE,bg="#F0F0F0").place(x=56,y=521,width=56,height=40)
        txtsegundos = Label(juego,relief=GROOVE,bg="#F0F0F0").place(x=106,y=521,width=58,height=40)
    
        if configuracion[1][0] == 1:
            txthoras = Label(juego,text="0",relief=GROOVE,bg="#F0F0F0").place(x=20,y=521,width=38,height=40)
            txtminutos = Label(juego,text="0",relief=GROOVE,bg="#F0F0F0").place(x=56,y=521,width=56,height=40)
            txtsegundos = Label(juego,text="0",relief=GROOVE,bg="#F0F0F0").place(x=106,y=521,width=58,height=40)
        
        if configuracion[1][2] == 1:
            txthoras = Label(juego,text=str(configuracion[3][0]),relief=GROOVE,bg="#F0F0F0").place(x=20,y=521,width=38,height=40)
            txtminutos = Label(juego,text=str(configuracion[3][1]),relief=GROOVE,bg="#F0F0F0").place(x=56,y=521,width=56,height=40)
            txtsegundos = Label(juego,text=str(configuracion[3][2]),relief=GROOVE,bg="#F0F0F0").place(x=106,y=521,width=58,height=40)
        

    #juego en cuadricula
    numeroPartida = random.randint(0,2)
    partida = totalJugadas[nivelJuego][numeroPartida]

    
    for simbolo in partida:
        k = 0
        f = simbolo[1]
        c = simbolo[2]
        elemento = simbolo[0]
        if elemento.isdigit() == True:
            for fila,fObj in enumerate(objetosBotones):
                for columna,cObj in enumerate(fObj):
                    if f == fila and c == columna:
                        obj = objetosBotones[fila][columna]
                        obj.config(text=elemento)
                        k = 1
                        break
                if k == 1:
                    break
        else:
            for fila,fcoordenadas in enumerate(coordenadas):
                for columna,cObj in enumerate(fcoordenadas):
                    if f == fila and c == columna:
                        print(fila,columna,f,c,cObj)
                        Cx = coordenadas[fila][columna][0]
                        Cy = coordenadas[fila][columna][1]
                        print(Cx,Cy,elemento)
                        if elemento == "<":
                            txt = Label(juego,text="<",font=("Arial",13),bg="#292929",fg="white").place(x=Cx+40,y=Cy+10,width=15)
                        if elemento == ">":
                            txt = Label(juego,text=">",font=("Arial",13),bg="#292929",fg="white").place(x=Cx+40,y=Cy+10,width=15)
                        if elemento == "˄":
                            txt = Label(juego,text="˄",font=("Arial",13),bg="#292929",fg="white").place(x=Cx+10,y=Cy-15,height=12)
                        if elemento == "˅":
                            txt = Label(juego,text="˅",font=("Arial",13),bg="#292929",fg="white").place(x=Cx+10,y=Cy-15,height=12)

                        k = 1
                        break
                if k == 1:
                    break
                
        Xbtn = Button(juego,text="X",command=cerrar)
        Xbtn.place(x=570,y=0)
                        








def configurar():
    def nivel(num,checkbtn1,checkbtn2,checkbtn3):
        global configuracion
        if num == 1:
            checkbtn2.deselect()
            checkbtn3.deselect()
            configuracion[0] = [1,0,0]
        elif num == 2:
            checkbtn1.config(selectcolor="white")
            checkbtn1.deselect()
            checkbtn3.deselect()
            configuracion[0] = [0,1,0]
        elif num == 3:
            checkbtn1.config(selectcolor="white")
            checkbtn1.deselect()
            checkbtn2.deselect()
            configuracion[0] = [0,0,1]
    def reloj(num,checkbtn4,checkbtn5,checkbtn6):
        global configuracion
        if num == 1:
            entryhoras.config(state='disabled')
            entryminutos.config(state='disabled')
            entrysegundos.config(state='disabled')
            
            checkbtn5.deselect()
            checkbtn6.deselect()
            configuracion[1] = [1,0,0]
        elif num == 2:
            entryhoras.config(state='disabled')
            entryminutos.config(state='disabled')
            entrysegundos.config(state='disabled')
            
            checkbtn4.config(selectcolor="white")
            checkbtn4.deselect()
            checkbtn6.deselect()
            configuracion[1] = [0,1,0]
        elif num == 3:
            print(1)
            entryhoras.config(state="normal")
            entryminutos.config(state='normal')
            entrysegundos.config(state='normal')
            
            checkbtn4.config(selectcolor="white")
            checkbtn4.deselect()
            checkbtn5.deselect()
            configuracion[1] = [0,0,1]
    def lado(num,checkbtn7,checkbtn8):
        global configuracion
        if num == 1:
            checkbtn8.deselect()
            configuracion[2] = [1,0]
        elif num == 2:
            checkbtn7.config(selectcolor="white")
            checkbtn7.deselect()
            configuracion[2] = [0,1]

    def guardar():
        if configuracion[1][2] == 1:
            horas = int(entryhoras.get())
            minutos = int(entryminutos.get())
            segundos = int(entrysegundos.get())
            
            if horas > 2 or horas < 0:
                messagebox.showerror("Error","Valor inválido")
                return
            if minutos > 59 or minutos < 0:
                messagebox.showerror("Error","Valor inválido")
                return
            if segundos > 59 or segundos < 0:
                messagebox.showerror("Error","Valor inválido")
                return
            if horas == 0 and minutos == 0 and segundos == 0:
                messagebox.showerror("Error","Las casillas no pueden estar vacías")
                return
            
            configuracion.append([horas,minutos,segundos])
            
        configArchivo = open("futoshiki2021configuración.dat","wb")
        pickle.dump(configuracion,configArchivo)
        configArchivo.close()
        configraiz.destroy()
        raiz.deiconify()
        
    def fin():
        configuracion = [[1,0,0],[1,0,0],[1,0]]
        configraiz.destroy()
        raiz.deiconify()
            

        
    raiz.withdraw()
    configraiz = Toplevel(raiz)
    configraiz.resizable(False,False)
    configraiz.geometry("300x260")
    configraiz.configure(bg="#292929")
    configraiz.title("Configuración")

    facil,medio,dificil = IntVar(),IntVar(),IntVar()
    txt1 = Label(configraiz,text="Nivel:",bg="#292929",fg="white").place(x=0,y=0)
    checkbtn1 = Checkbutton(configraiz,text="Fácil",variable=facil,onvalue=1,offvalue=0,bg="#292929",selectcolor="red",command=lambda:nivel(1,checkbtn1,checkbtn2,checkbtn3))
    checkbtn1.place(x=50,y=0)
    checkbtn1.select()
    txt = Label(configraiz,text="Fácil",bg="#292929",fg="white").place(x=70,y=3)
    checkbtn2 = Checkbutton(configraiz,text="Intermedio",variable=medio,onvalue=1,offvalue=0,bg="#292929",command=lambda:nivel(2,checkbtn1,checkbtn2,checkbtn3))
    checkbtn2.place(x=50,y=20)
    txt = Label(configraiz,text="Intermedio",bg="#292929",fg="white").place(x=70,y=23)
    checkbtn3 = Checkbutton(configraiz,text="Difícil",variable=dificil,onvalue=1,offvalue=0,bg="#292929",command=lambda:nivel(3,checkbtn1,checkbtn2,checkbtn3))
    checkbtn3.place(x=50,y=40)
    txt = Label(configraiz,text="Difícil",bg="#292929",fg="white").place(x=70,y=43)

    si,no,timer= IntVar(),IntVar(),IntVar()
    txt2 = Label(configraiz,text="Reloj:",bg="#292929",fg="white").place(x=0,y=80)
    checkbtn4 = Checkbutton(configraiz,text="Sí",variable=si,onvalue=1,offvalue=0,bg="#292929",selectcolor="red",command=lambda:reloj(1,checkbtn4,checkbtn5,checkbtn6))
    checkbtn4.place(x=50,y=80)
    txt = Label(configraiz,text="Sí",bg="#292929",fg="white").place(x=70,y=83)
    checkbtn5 = Checkbutton(configraiz,text="No",variable=no,onvalue=1,offvalue=0,bg="#292929",command=lambda:reloj(2,checkbtn4,checkbtn5,checkbtn6))
    checkbtn5.place(x=50,y=100)
    txt = Label(configraiz,text="No",bg="#292929",fg="white").place(x=70,y=103)
    checkbtn6 = Checkbutton(configraiz,text="Timer",variable=timer,onvalue=1,offvalue=0,bg="#292929",command=lambda:reloj(3,checkbtn4,checkbtn5,checkbtn6))
    checkbtn6.place(x=50,y=120)
    txt = Label(configraiz,text="Timer",bg="#292929",fg="white").place(x=70,y=123)

    derecha,izquierda = IntVar(),IntVar()
    txt3 = Label(configraiz,text="Posición del reloj:",bg="#292929",fg="white").place(x=0,y=160)
    checkbtn7 = Checkbutton(configraiz,text="Derecha",variable=derecha,onvalue=1,offvalue=0,bg="#292929",selectcolor="red",command=lambda:lado(1,checkbtn7,checkbtn8))
    checkbtn7.place(x=100,y=160)
    txt = Label(configraiz,text="Derecha",bg="#292929",fg="white").place(x=120,y=163)
    checkbtn8 = Checkbutton(configraiz,text="Izquierda",variable=izquierda,onvalue=1,offvalue=0,bg="#292929",command=lambda:lado(2,checkbtn7,checkbtn8))
    checkbtn8.place(x=100,y=180)
    txt = Label(configraiz,text="Izquierda",bg="#292929",fg="white").place(x=120,y=183)

    #timer
    txthoras = Label(configraiz,text="Horas",relief=GROOVE).place(x=115,y=83)
    txtmunutos = Label(configraiz,text="Minutos",relief=GROOVE).place(x=151,y=83)
    txtsegundos = Label(configraiz,text="Segundos",relief=GROOVE).place(x=201,y=83)

    horas,minutos,segundos = IntVar(value=0),IntVar(value=0),IntVar(value=0)
    entryhoras = Entry(configraiz,textvariable=horas,state='disabled',relief=GROOVE,bg="#F0F0F0")
    entryhoras.place(x=115,y=104,width=38,height=40)
    entryminutos = Entry(configraiz,textvariable=minutos,state='disabled',relief=GROOVE,bg="#F0F0F0")
    entryminutos.place(x=151,y=104,width=56,height=40)
    entrysegundos = Entry(configraiz,textvariable=segundos,state='disabled',relief=GROOVE,bg="#F0F0F0")
    entrysegundos.place(x=201,y=104,width=58,height=40)
    


    okbtn = Button(configraiz,text="Ok",command=guardar)
    okbtn.place(x=30,y=220,width=30)
    cancelbtn = Button(configraiz,text="Cancelar",command=fin)
    cancelbtn.place(x=80,y=220,width=60)















## programa principal ##
configuracion = [[1,0,0],[1,0,0],[1,0]]
top10facil = []
top10intermedio = []
top10dificil = []
actual = []

#jugadas

jugadasFacil = [(("1",0,0),("4",0,1),("3",0,2),("3",1,1),("1",2,1),("4",2,3),("2",3,4),("1",4,3)), \
                (("2",1,0),("3",1,1),("5",1,2),("1",2,0),("5",3,0),("1",3,2),("4",3,4),("1",4,1),("3",4,4)), \
                (("3",0,0),("1",1,0),("3",1,1),("5",1,4),("4",2,0),("1",2,1),("5",3,3),("1",4,4))]

jugadasIntermedio = [((">",0,0),("<",0,3),("<",1,1),("<",1,2),("<",1,3),("4",1,4),("˄",1,4),("˄",3,2),("˅",3,3),(">",3,3),("˄",4,0),("˄",4,2)),\
                     ((">",0,0),(">",0,2),(">",0,3),("˅",1,4),("3",1,1),("˄",1,2),("˄",3,0),("˄",3,2),("3",4,4)), \
                     ((">",1,0),("˅",1,1),(">",2,3),(">",3,0),(">",3,1),(">",3,2),("˅",3,3),("2",4,1))]

jugadasDificil = [(("<",0,3),("<",1,2),("˅",1,2),("4",2,0),("˄",2,1),("˄",3,0),("˄",3,1),(">",3,2),("˅",3,4),(">",4,0)),\
                  (("<",0,1),("˄",1,0),(">",1,1),("˄",1,2),("˅",1,2),(">",2,3),(">",3,0),(">",3,1),("˅",3,3),("˅",3,4),("˄",4,1),(">",4,3)),\
                  (("<",0,0),("˅",1,4),(">",1,1),("3",2,0),("˄",2,0),("<",2,1),("1",2,3),("5",2,4),("<",3,3),("˄",4,1),("<",4,3))]

totalJugadas = [jugadasFacil,jugadasIntermedio,jugadasDificil]
jugadas = open("futoshiki2021partidas.dat","wb")
pickle.dump(totalJugadas,jugadas)
jugadas.close()



                         
raiz = Tk()
raiz.resizable(False,False)
raiz.geometry("512x384")
raiz.configure(bg="light gray")
raiz.title("futoshiki")

fondo = PhotoImage(file="futoshiki.png")
Labelfondo = Label(raiz,image=fondo).pack()

ButtonJugar = Button(raiz,text="Jugar",command=jugar,font=("cambria", 15),fg="white",bg="#292929")
ButtonConfigurar = Button(raiz,text="Configurar",command=configurar,font=("cambria", 15),fg="white",bg="#292929")
ButtonJugar.place(x=165,y=250,width=180)
ButtonConfigurar.place(x=165,y=290,width=180)

raiz.mainloop()
