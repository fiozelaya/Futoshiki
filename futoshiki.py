'''PROYECTO III FIORELLA ZELAYA'''


## modulos ##

import pickle
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import webbrowser as wb
from playsound import playsound 


## funciones ##

#guardar la partida que se esté jugando
#se crea/abre el archivo y se guardan las listas necesarias para cargar la partida
def Guardar(configuracion,cuadriculaBotones,movimientos2,numeroPartida,coordenadas,nombre,h,m,s,Ch,Cm,Cs):
            
    archivo = open("futoshiki2021juegoactual.dat","wb")
    pickle.dump([configuracion,cuadriculaBotones,movimientos2,numeroPartida,coordenadas,nombre,[h,m,s,Ch,Cm,Cs]],archivo)
    archivo.close()


#funcion de jugar
#ventana de la partida y funciones anidadas
def jugar():

    #cada vez que se gana una partida se llama esta función
    #para ver cuando se ha ganado la partida
    #se deshabilitan los botones porque ya ha finalizado la partida
    def actualizar():
        global variableIniciar
        for fila in cuadriculaBotones:
            for columna in fila:
                if columna == []:
                    return

        #si se gana la partida, se reinician algunas variables
        variableIniciar = 0
        playsound("preview.mp3")
        messagebox.showinfo("¡Ganaste!","¡Felicidades! Juego terminado con éxito.")
        
        h,m,s = 0,0,0

        #se llama a las funciones del Top 10 para guardar los datos de la partida
        if configuracion[1][1] == 0:
            Top10listas(Top10facil,Top10intermedio,Top10dificil)
            archivosTop10()
        btnIniciar.config(state="disabled")
        btnBorrarJugada.config(state="disabled")
        btnTerminar.config(state="disabled")
        btnBorrar.config(state="disabled")


    #funcion para cargar la partida
    #recibe las listas necesarias para sobreescribirlas, aunque creo que no es necesario
    def Cargar(txtlista,objetosBotones,btnIniciar,btnBorrarJugada,btnTerminar,btnBorrar,btnGuardar,entryNombre):
        
        global h
        global m
        global s
        global Ch
        global Cm
        global Cs
        global nombre
        global configuracion
        global movimientos2
        global partida

        #destruye todos los Label que se hayan puesto en la partida en nivel intermedio o dificil
        for txt in txtlista:
            txt.destroy()

        #si no se ha guardado ninguna partida:
        try:
            archivo = open("futoshiki2021juegoactual.dat","rb")
        except:
            messagebox.showerror("Error","No se ha guardado ninguna partida")
            return

        #se sobreescriben las variables con las de la partida guardada        
        archivoPartida=pickle.load(archivo)
        
        configuracion = archivoPartida[0]
        cuadriculaBotones = archivoPartida[1]
        
        movimientos2 = archivoPartida[2]
        numeroPartida = archivoPartida[3]
        coordenadas = archivoPartida[4]
        nombre = archivoPartida[5]
        tiempo = archivoPartida[6]
        h,m,s = tiempo[0],tiempo[1],tiempo[2]
        Ch,Cm,Cs = tiempo[3],tiempo[4],tiempo[5]


        #se borran los datos de la cuadrícula de la partida actual
        fila = 0
        while fila != 5: #fila
            contador2 = 5
            columna = 0
            while columna != 5: #columna
                obj = objetosBotones[fila][columna]
                try:
                    elemento = cuadriculaBotones[fila][columna][0]
                    if not isinstance(elemento,str):
                        obj.config(text=str(elemento))
                except:
                    obj.config(text="")
                columna += 1
            fila += 1

        #datos si se escogió timer
        if configuracion[1][2] == 1:
            configuracion[3] = [h,m,s]


        #se despliega la partida guardada
        desplegar_partida_cargar(numeroPartida,cuadriculaBotones)
        archivo.close()

        #se deshabilitan ciertos botones y se cambia su función
        btnIniciar.config(state="normal")
        btnBorrarJugada.config(state="disabled",command=lambda: borrarJugadaCargar(movimientos2))
        btnTerminar.config(state="disabled")
        btnBorrar.config(state="disabled",command=lambda: borrarCargar(movimientos2))
        nombre = StringVar(value=nombre)
        entryNombre.config(textvariable=nombre)



    #funcion cada vez que se presiona la cuadricula
    #recibe el objeto del botón que se está presionando y la fila y la columna del boton
    def presionar(obj,fila,columna):
        global botonNumero
        #si no se ha iniciado el juego o escogido un botón, manda el aviso y retorna:
        if variableIniciar == 0:
            return
        if botonNumero == 0:
            messagebox.showinfo("!","Seleccione un dígito")
            return
        obj.config(text=str(botonNumero))

        #restricciones
        #filas y columnas
        #busca si el número existe en la misma fila/columna y si sí, manda aviso y retorna
        #busca si la casilla contiene un digito fijo, y si sí, avisa
        for i in range(5):
            try:
                filas = int(cuadriculaBotones[fila][i][0])
            except:
                filas = 0
            try:
                columnas = int(cuadriculaBotones[i][columna][0])
            except:
                columnas = 0
            if filas == botonNumero:
                obj.config(bg="red")
                messagebox.showinfo("!","Jugada no válida: El elemento ya se encuentra en la fila")
                try:
                    texto = str(cuadriculaBotones[fila][columna][0])
                except:
                    texto = ""
                obj.config(text=texto)
                obj.config(bg="SystemButtonFace")
                return
            if columnas == botonNumero:
                obj.config(bg="red")
                messagebox.showinfo("!","Jugada no válida: El elemento ya se encuentra en la columna")
                try:
                    texto = str(cuadriculaBotones[fila][columna][0])
                except:
                    texto = ""
                obj.config(text=texto)
                obj.config(bg="SystemButtonFace")
                return

        auxboton = botonNumero
        for simbolo in partida:
            k = 0
            elemento = simbolo[0]
            ifObj = simbolo[1]
            icObj = simbolo[2]
            if elemento.isdigit() == True:
                if ifObj == fila and icObj == columna:
                    obj = objetosBotones[fila][columna]
                    obj.config(bg="red")
                    messagebox.showinfo("!","Jugada no válida: La casilla es un dígito fijo")
                    obj.config(bg="SystemButtonFace")
                    obj.config(text=str(elemento))
                    k = 1
                    return
            #else:
            #restricciones de mayor o menor que
            #busca si el botón presionado esta cerca o tiene una restricción y la valida, si no se cumple, avisa y retorna
            contador = 1
            flag = 0
            for n in range(contador):
                if (ifObj == fila and icObj == columna) or (ifObj == fila+1 and icObj == columna) or (ifObj == fila and icObj == columna-1):
                    if ifObj == fila and icObj == columna and flag != 0:
                        contador = 0
                        flag = 0
                    elif ifObj == fila+1 and icObj == columna and flag != 1 and elemento != ">" and elemento != "<":
                        contador = 1
                        flag = 1
                    elif ifObj == fila and icObj == columna-1 and flag != 2 and elemento != "˄" and elemento != "˅":
                        contador = 2
                        flag = 2
                    else:
                        break

                    if elemento == "<":
                        try:
                            elemento2 = cuadriculaBotones[fila][columna+1][0]
                        except:
                            elemento2 = 6

                        try:
                            texto = str(cuadriculaBotones[fila][columna][0])
                        except:
                            texto = ""
                        
                        if flag == 2:
                            try:
                                botonNumero = cuadriculaBotones[fila][columna-1][0]
                                elemento2 = auxboton
                                
                            except:
                                break
                        if int(botonNumero) > int(elemento2):
                            obj.config(bg="red")
                            messagebox.showinfo("!","Jugada no válida: No se cumple la restricción de menor")
                            obj.config(bg="SystemButtonFace")
                            obj.config(text=texto)
                            botonNumero = auxboton
                            return

                    
                    if elemento == ">":
                        try:
                            elemento2 = cuadriculaBotones[fila][columna+1][0]
                            
                        except:
                            elemento2 = 0
                            

                        try:
                            texto = str(cuadriculaBotones[fila][columna][0])
                        except:
                            texto = ""
                            
                        if flag == 2:
                            try:
                                botonNumero = cuadriculaBotones[fila][columna-1][0]
                                elemento2 = auxboton
                                
                            except:
                                break
                            
                        if int(botonNumero) < int(elemento2):
                            obj.config(bg="red")
                            messagebox.showinfo("!","Jugada no válida: No se cumple la restricción de mayor")
                            obj.config(bg="SystemButtonFace")
                            obj.config(text=texto)
                            botonNumero = auxboton
                            return
                        
                    if elemento == "˄":
                        try:
                            elemento2 = cuadriculaBotones[fila-1][columna][0]
                            
                        except:
                            elemento2 = 0
                            

                        try:
                            texto = str(cuadriculaBotones[fila][columna][0])
                        except:
                            texto = ""
                            
                        if flag == 1:
                            try:
                                botonNumero = cuadriculaBotones[fila+1][columna][0]
                                elemento2 = auxboton
                            except:
                                break
                            
                        if int(botonNumero) < int(elemento2):
                            obj.config(bg="red")
                            messagebox.showinfo("!","Jugada no válida: No se cumple la restricción de mayor")
                            obj.config(bg="SystemButtonFace")
                            obj.config(text=texto)
                            botonNumero = auxboton
                            return
                        
                    if elemento == "˅":
                        try:
                            elemento2 = cuadriculaBotones[fila-1][columna][0]
                        except:
                            elemento2 = 6

                        try:
                            texto = str(cuadriculaBotones[fila][columna][0])
                        except:
                            texto = ""
                            
                        if flag == 1:
                            try:
                                botonNumero = cuadriculaBotones[fila+1][columna][0]
                                elemento2 = auxboton
                            except:
                                break
                            
                        if int(botonNumero) > int(elemento2):
                            obj.config(bg="red")
                            messagebox.showinfo("!","Jugada no válida: No se cumple la restricción de menor")
                            obj.config(bg="SystemButtonFace")
                            obj.config(text=texto)
                            botonNumero = auxboton
                            return

        #si todo está bien, se agrega a las listas de movimientos y cuadriculaBotones
        botonNumero = auxboton
        if len(cuadriculaBotones[fila][columna]) > 0:
            cuadriculaBotones[fila][columna][0] = botonNumero
        else:
            cuadriculaBotones[fila][columna].append(botonNumero)

        movimientos.append([obj,fila,columna])
        movimientos2.append([fila,columna])

        #se llama a la función para ver si ya se llenaron todas las casillas
        actualizar() 


    #funcion para cada vez que se escoja un número
    #se deseleccionan los demás botones, y se selecciona el verde el escogido
    def presionar_numero(num,obj):
        global botonNumero
        if variableIniciar == 0:
            return
        for i,objetoNumero in enumerate(listaBotonesNumero):
            if objetoNumero != obj:
                for i2,imagen in enumerate(imagenesBotones):
                    if i == i2:
                        objetoNumero.config(image=imagen)
                        break
                    
        botonNumero = num
        for i,imagen in enumerate(imagenesBotonesp):
            if i == num-1:
                obj.config(image=imagen)


    #funcion para el botón Iniciar juego
    #activa la variableIniciar
    #verifica que se haya puesto un nombre
    #habilita y deshabilita ciertos botones
    #depende de la configuración, activa el cronómetro, timer o ninguno
    def iniciar():
        global variableIniciar
        global nombre
        global h
        global m
        global s
        variableIniciar = 1
        nombre = entryNombre.get()
        if nombre == "":
            messagebox.showerror("Error","No ha registrado el nombre del jugador")
            return
        if len(nombre) < 1 or len(nombre) > 20:
            messagebox.showerror("Error","Nombre del jugador inválido")
            return
        btnIniciar.config(state="disabled")
        btnBorrarJugada.config(state="normal")
        btnTerminar.config(state="normal")
        btnBorrar.config(state="normal")
        btnGuardar.config(state="normal")
        btnCargar.config(state="disabled")
        if configuracion[1][1] == 1:
            pass
        elif configuracion[1][0] == 1:
            cronómetro()
        elif configuracion[1][2] == 1:
            h = int(configuracion[3][0])
            m = int(configuracion[3][1])
            s = int(configuracion[3][2])
            timer()

    #funcion para el timer
    #cuenta en cuenta regresiva, y también cuenta un cronómetro para saber el tiempo jugado
    def timer():
        global h
        global m
        global s
        global variableIniciar
        global tiempoJugado
        print(h,m,s)

        if variableIniciar == 0:
            txthoras.config(text=str(h))
            txtminutos.config(text=str(m))
            txtsegundos.config(text=str(s))
            return

        cronómetro_timer() #cronómetro del timer
        
        s -= 1
        if s < 0 and m != 0:
            s = 59
            m -= 1
            if m < 0 and h != 0:
                m = 59
                h -= 1

        txthoras.config(text=str(h))
        txtminutos.config(text=str(m))
        txtsegundos.config(text=str(s))

        if h == 0 and m == 0 and s == 0:
            respuesta = messagebox.askyesno("Tiempo expirado!","¿Desea continuar jugando?")
            if respuesta == True:
                h = int(configuracion[3][0])
                m = int(configuracion[3][1])
                s = int(configuracion[3][2])
                cronómetro()
                return
            else:
                cerrar()
                return
        
        juego.after(1000,timer)

    #cronometro para el timer
    #cuenta el tiempo total jugado
    def cronómetro_timer():
        global tiempoJugado
        global Ch
        global Cm
        global Cs

        Cs += 1
        if Cs > 59:
            Cs = 0
            Cm += 1
            if Cm > 59:
                Cm = 0
                Ch += 1

        tiempoJugado = str(Ch)+":"+str(Cm)+":"+str(Cs)

    #funcion para el cronómetro normal
    #cuenta el tiempo transcurrido de la partida hasta que se gane
    def cronómetro():
        global tiempoJugado
        global h
        global m
        global s
        global variableIniciar

        if variableIniciar == 0:
            tiempoJugado = str(h)+":"+str(m)+":"+str(s)
            txthoras.config(text=str(h))
            txtminutos.config(text=str(m))
            txtsegundos.config(text=str(s))
            return

        s += 1
        if s > 59:
            s = 0
            m += 1
            if m > 59:
                m = 0
                h += 1
        
        txthoras.config(text=str(h))
        txtminutos.config(text=str(m))
        txtsegundos.config(text=str(s))
        
        juego.after(1000,cronómetro)
        

    #funcion para borrar un movimiento
    #busca en la lista de movimientos el último movimiento, y lo borrar del objeto
    def borrarJugada():
        try:
            movimiento = movimientos[-1]
        except IndexError:
            messagebox.showinfo("!","No hay más jugadas para borrar")
            return
        
        obj = movimiento[0]
        fila = movimiento[1]
        columna = movimiento[2]
        del movimientos[-1]
        
        obj.config(text="")
        cuadriculaBotones[fila][columna] = []


    #funcion para borrar un movimiento al cargar una partida
    #con la fila y la columna, busca en la lista de botones el objeto y lo vacía, al igual que en la lista cuadriculaBotones
    def borrarJugadaCargar(movimientos2):
        try:
            movimiento = movimientos2[-1]
        except IndexError:
            messagebox.showinfo("!","No hay más jugadas para borrar")
            return
        fila = movimiento[0]
        columna = movimiento[1]
        
        for f,filaBoton in enumerate(objetosBotones):
            for c,columnaBoton in enumerate(filaBoton):
                if fila == f and c == columna:
                    obj = objetosBotones[fila][columna]
                    obj.config(text="")
                    cuadriculaBotones[fila][columna] = []
                    del movimientos2[-1]
        

    #función para terminar el juego
    #pregunta si se desea terminar el juego, si sí, se destruye la ventana
    def terminar():
        respuesta = messagebox.askyesno("!","¿Desea terminar el juego? Se perderá la partida actual.")
        if respuesta == False:
            return

        cerrar()
        jugar()
        

    #funcion para reiniciar la partida
    #busca todos los movimientos en la lista y los borra
    def borrar():
        respuesta = messagebox.askyesno("!","¿Desea borrar el juego? Se borrarán todos los movimientos.")
        if respuesta == False:
            return

        l = len(movimientos)
        while l != 0:
            try:
                movimiento = movimientos[-1]
            except IndexError:
                return
            
            obj = movimiento[0]
            fila = movimiento[1]
            columna = movimiento[2]
            del movimientos[-1]
            del movimientos2[-1]
            
            obj.config(text="")
            cuadriculaBotones[fila][columna] = []
        


    #funcion para reiniciar la aprtida cargarda
    #busca los movimientos en la lista 2 y los elimina con la fila y la columna
    def borrarCargar(movimientos2):
        respuesta = messagebox.askyesno("!","¿Desea borrar el juego? Se borrarán todos los movimientos.")
        if respuesta == False:
            return

        l = len(movimientos2)
        while l != 0:
            try:
                movimiento = movimientos2[-1]
            except IndexError:
                return
            
            fila = movimiento[0]
            columna = movimiento[1]

            for f,filaBoton in enumerate(objetosBotones):
                for c,columnaBoton in enumerate(filaBoton):
                    if fila == f and c == columna:
                        obj = objetosBotones[fila][columna]
                        obj.config(text="")
                        cuadriculaBotones[fila][columna] = []
                        del movimientos2[-1]
            
            obj.config(text="")
            cuadriculaBotones[fila][columna] = []
            
        
    #funcion para guardar los datos de la partida actual ordenadamente
    #recibe todas las listas y dependiendo de la configuración, se guarda la partida actual en esa
    #se comparan las horas, minutos y segundos, y el que tenga menos se coloca en frente del que tenga más
    def Top10listas(Top10facil,Top10intermedio,Top10dificil):
        if configuracion[0][0] == 1:
            if Top10facil == []:
                Top10facil.append([nombre,tiempoJugado])
                return
            for i,elemento in enumerate(Top10facil):
                tiempo = elemento[1].split(":")
                hh = int(tiempo[0])
                mm = int(tiempo[1])
                ss = int(tiempo[2])

                try:
                    tiempo2 = Top10facil[i+1][1].split(":")
                    hh2 = int(tiempo2[0])
                    mm2 = int(tiempo2[1])
                    ss2 = int(tiempo2[2])
                    if hh2 < h or mm2 < m or ss2 < s:
                        continue
                except:
                    pass
                
                if hh > h:
                    Top10facil.insert(i,[nombre,tiempoJugado])
                    return
                elif mm > m:
                    Top10facil.insert(i,[nombre,tiempoJugado])
                    return
                elif ss > s and mm >= m and hh >= h:
                    Top10facil.insert(i,[nombre,tiempoJugado])
                    return
                else:
                    Top10facil.insert(i+1,[nombre,tiempoJugado])
                    return
            
        if configuracion[0][1] == 1:
            if Top10intermedio == []:
                Top10intermedio.append([nombre,tiempoJugado])
                return
            for i,elemento in enumerate(Top10intermedio):
                tiempo = elemento[1].split(":")
                hh = int(tiempo[0])
                mm = int(tiempo[1])
                ss = int(tiempo[2])

                try:
                    tiempo2 = Top10intermedio[i+1][1].split(":")
                    hh2 = int(tiempo2[0])
                    mm2 = int(tiempo2[1])
                    ss2 = int(tiempo2[2])
                    if hh2 < h or mm2 < m or ss2 < s:
                        continue
                except:
                    pass
                
                if hh > h:
                    Top10facil.insert(i,[nombre,tiempoJugado])
                    return
                elif mm > m:
                    Top10facil.insert(i,[nombre,tiempoJugado])
                    return
                elif ss > s:
                    if ss == s and mm == m:
                        Top10facil.insert(i,[nombre,tiempoJugado])
                        return
                    Top10facil.insert(i,[nombre,tiempoJugado])
                    return
                else:
                    Top10facil.insert(i+1,[nombre,tiempoJugado])
                    return
                
        if configuracion[0][2] == 1:
            if Top10dificil == []:
                Top10dificil.append([nombre,tiempoJugado])
                return
            for i,elemento in enumerate(Top10dificil):
                tiempo = elemento[1].split(":")
                hh = int(tiempo[0])
                mm = int(tiempo[1])
                ss = int(tiempo[2])

                try:
                    tiempo2 = Top10dificil[i+1][1].split(":")
                    hh2 = int(tiempo2[0])
                    mm2 = int(tiempo2[1])
                    ss2 = int(tiempo2[2])
                    if hh2 < h or mm2 < m or ss2 < s:
                        continue
                except:
                    pass
                
                if hh > h:
                    Top10facil.insert(i,[nombre,tiempoJugado])
                    return
                elif mm > m:
                    Top10facil.insert(i,[nombre,tiempoJugado])
                    return
                elif ss > s:
                    if ss == s and mm == m:
                        Top10facil.insert(i,[nombre,tiempoJugado])
                        return
                    Top10facil.insert(i,[nombre,tiempoJugado])
                    return
                else:
                    Top10facil.insert(i+1,[nombre,tiempoJugado])
                    return


    #funcion para guardar en archivos las listas del Top 10
    def archivosTop10():
        archivo = open("futoshiki2021top10.dat","wb")
        pickle.dump([Top10facil,Top10intermedio,Top10dificil],archivo)
        archivo.close()


    #funcion para desplegar el Top10
    #con un ciclo se pone en la pantalla las Label según ciertas coordenadas
    #luego, se abre el archivo del top 10 y se van colocando los jugadores y sus tiempos con las antiguas coordenadas
    def Top10():
        #juego.after_cancel(cronómetro)
        
        top10 = Toplevel(juego)
        top10.resizable(False,False)
        top10.geometry("580x360")
        top10.configure(bg="#292929")
        top10.title("Top 10")

        txt = Label(top10,text="Top 10",bg="#292929",fg="white",font=("Arial",18,"underline")).place(x=220,y=0)
        faciltxt = Label(top10,text="Nivel fácil",fg="white",bg="#292929").place(x=25,y=40)
        intermediotxt = Label(top10,text="Nivel intermedio",fg="white",bg="#292929").place(x=225,y=40)
        dificiltxt = Label(top10,text="Nivel difícil",fg="white",bg="#292929").place(x=425,y=40)
        
        
        n=3
        Cx=20
        while n != 0:
            txt = Label(top10,text="JUGADOR",fg="white",bg="#292929").place(x=Cx+10,y=60)
            txt = Label(top10,text="TIEMPO",fg="white",bg="#292929").place(x=Cx+100,y=60)
            txt1 = Label(top10,text="1-",fg="white",bg="#292929").place(x=Cx,y=100)
            txt2 = Label(top10,text="2-",fg="white",bg="#292929").place(x=Cx,y=120)
            txt3 = Label(top10,text="3-",fg="white",bg="#292929").place(x=Cx,y=140)
            txt4 = Label(top10,text="4-",fg="white",bg="#292929").place(x=Cx,y=160)
            txt5 = Label(top10,text="5-",fg="white",bg="#292929").place(x=Cx,y=180)
            txt6 = Label(top10,text="6-",fg="white",bg="#292929").place(x=Cx,y=200)
            txt7 = Label(top10,text="7-",fg="white",bg="#292929").place(x=Cx,y=220)
            txt8 = Label(top10,text="8-",fg="white",bg="#292929").place(x=Cx,y=240)
            txt9 = Label(top10,text="9-",fg="white",bg="#292929").place(x=Cx,y=260)
            txt10 = Label(top10,text="10-",fg="white",bg="#292929").place(x=Cx-5,y=280)
            Cx += 200
            n -= 1

        try:
            
            archivo = open("futoshiki2021top10.dat","rb")
            top10listas = pickle.load(archivo)
            Cx = 20
            for nivel in top10listas:
                contador = 10
                Cy = 100
                for jugador in nivel:
                    if contador == 0:
                        break
                    txtnombre = Label(top10,text=jugador[0],fg="white",bg="#292929").place(x=Cx+15,y=Cy)
                    txttiempo = Label(top10,text=jugador[1],fg="white",bg="#292929").place(x=Cx+100,y=Cy)
                    Cy += 20
                    contador -= 1
                    
                Cx += 200

        except:
            pass


    #funcion para desplegar partida cada vez que se abre la ventana de Jugar
    #crea la lista de cuadriculaBotones, movimientos
    #busca en la partida generada al azar si hay simbolos de mayor o menor que, y los coloca
    #busca los digitos fijos y los coloca en los objetos
    def desplegar_partida():
        global partida
        global numeroPartida
        global cuadriculaBotones
        global movimientos
        global movimientos2
        global h
        global m
        global s
        global Ch
        global Cm
        global Cs
        h,m,s,Ch,Cm,Cs = 0,0,0,0,0,0
        numeroPartida = random.randint(0,2)
        partida = totalJugadas[nivelJuego][numeroPartida]
        cuadriculaBotones = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
        movimientos = []
        movimientos2 = []
        
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
                            if len(cuadriculaBotones[fila][columna]) > 0:
                                cuadriculaBotones[fila][columna][0] = elemento
                            else:
                                cuadriculaBotones[fila][columna].append(elemento)
                            k = 1
                            break
                    if k == 1:
                        break
            else:
                for fila,fcoordenadas in enumerate(coordenadas):
                    for columna,cObj in enumerate(fcoordenadas):
                        if f == fila and c == columna:
                            Cx = coordenadas[fila][columna][0]
                            Cy = coordenadas[fila][columna][1]
                            if elemento == "<":
                                txt = Label(juego,text="<",font=("Arial",13),bg="#292929",fg="white")
                                txt.place(x=Cx+40,y=Cy+10,width=15)
                            if elemento == ">":
                                txt = Label(juego,text=">",font=("Arial",13),bg="#292929",fg="white")
                                txt.place(x=Cx+40,y=Cy+10,width=15)
                            if elemento == "˄":
                                txt = Label(juego,text="˄",font=("Arial",13),bg="#292929",fg="white")
                                txt.place(x=Cx+10,y=Cy-15,height=12)
                            if elemento == "˅":
                                txt = Label(juego,text="˅",font=("Arial",13),bg="#292929",fg="white")
                                txt.place(x=Cx+10,y=Cy-15,height=12)

                            txtlista.append(txt)
                            k = 1
                            break
                    if k == 1:
                        break


    #funcion para desplegar una partida que se quiere cargar
    #recibe el numero de partida y la lista de botones de esa partida a cargar
    #realiza el mismo procedimiento que la funcipon anterior
    def desplegar_partida_cargar(numero,btns):
        global partida
        global numeroPartida
        global cuadriculaBotones
        cuadriculaBotones = btns
        partida = totalJugadas[nivelJuego][numero]
        numeroPartida = numero
    

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
                            Cx = coordenadas[fila][columna][0]
                            Cy = coordenadas[fila][columna][1]
                            if elemento == "<":
                                txt = Label(juego,text="<",font=("Arial",13),bg="#292929",fg="white")
                                txt.place(x=Cx+40,y=Cy+10,width=15)
                            if elemento == ">":
                                txt = Label(juego,text=">",font=("Arial",13),bg="#292929",fg="white")
                                txt.place(x=Cx+40,y=Cy+10,width=15)
                            if elemento == "˄":
                                txt = Label(juego,text="˄",font=("Arial",13),bg="#292929",fg="white")
                                txt.place(x=Cx+10,y=Cy-15,height=12)
                            if elemento == "˅":
                                txt = Label(juego,text="˅",font=("Arial",13),bg="#292929",fg="white")
                                txt.place(x=Cx+10,y=Cy-15,height=12)

                            txtlista.append(txt)
                            k = 1
                            break
                    if k == 1:
                        break


        

    #funcion para cerrar la ventana 
    def cerrar():
        global variableIniciar
        global botonNumero
        juego.destroy()
        raiz.deiconify()
        variableIniciar = 0
        h,m,s = 0,0,0
        botonNumero = 0
        return


    #VENTANA
    raiz.withdraw()
    juego = Toplevel(raiz)
    juego.resizable(False,False)
    juego.geometry("600x600")
    juego.configure(bg="#292929")
    juego.title("Futoshiki")

    #variables utiles
    txtlista = []
    
    #LABELS
    futoshikitxt = Label(juego,text="FUTOSHIKI",font=("cambria", 24),bg="firebrick",fg="white",relief=GROOVE).place(x=200,y=5,width=200)

            #busca en configuracion el nivel para desplegarlo en Label
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
    entryNombre = Entry(juego) #entry del nombre
    entryNombre.place(x=140,y=90,width=300)

    #cuadricula
    btn00 = Button(juego,relief=RIDGE,command=lambda: presionar(btn00,0,0))
    btn01 = Button(juego,relief=RIDGE,command=lambda: presionar(btn01,0,1))
    btn02 = Button(juego,relief=RIDGE,command=lambda: presionar(btn02,0,2))
    btn03 = Button(juego,relief=RIDGE,command=lambda: presionar(btn03,0,3))
    btn04 = Button(juego,relief=RIDGE,command=lambda: presionar(btn04,0,4))
    
    btn10 = Button(juego,relief=RIDGE,command=lambda: presionar(btn10,1,0))
    btn11 = Button(juego,relief=RIDGE,command=lambda: presionar(btn11,1,1))
    btn12 = Button(juego,relief=RIDGE,command=lambda: presionar(btn12,1,2))
    btn13 = Button(juego,relief=RIDGE,command=lambda: presionar(btn13,1,3))
    btn14 = Button(juego,relief=RIDGE,command=lambda: presionar(btn14,1,4))

    btn20 = Button(juego,relief=RIDGE,command=lambda: presionar(btn20,2,0))
    btn21 = Button(juego,relief=RIDGE,command=lambda: presionar(btn21,2,1))
    btn22 = Button(juego,relief=RIDGE,command=lambda: presionar(btn22,2,2))
    btn23 = Button(juego,relief=RIDGE,command=lambda: presionar(btn23,2,3))
    btn24 = Button(juego,relief=RIDGE,command=lambda: presionar(btn24,2,4))

    btn30 = Button(juego,relief=RIDGE,command=lambda: presionar(btn30,3,0))
    btn31 = Button(juego,relief=RIDGE,command=lambda: presionar(btn31,3,1))
    btn32 = Button(juego,relief=RIDGE,command=lambda: presionar(btn32,3,2))
    btn33 = Button(juego,relief=RIDGE,command=lambda: presionar(btn33,3,3))
    btn34 = Button(juego,relief=RIDGE,command=lambda: presionar(btn34,3,4))

    btn40 = Button(juego,relief=RIDGE,command=lambda: presionar(btn40,4,0))
    btn41 = Button(juego,relief=RIDGE,command=lambda: presionar(btn41,4,1))
    btn42 = Button(juego,relief=RIDGE,command=lambda: presionar(btn42,4,2))
    btn43 = Button(juego,relief=RIDGE,command=lambda: presionar(btn43,4,3))
    btn44 = Button(juego,relief=RIDGE,command=lambda: presionar(btn44,4,4))

    #MATRIZ DE LOS OBJETOS DE LOS BOTONES EN ORDEN DE FILA Y COLUMNA 
    objetosBotones = [[(btn00),(btn01),(btn02),(btn03),(btn04)],\
                      [(btn10),(btn11),(btn12),(btn13),(btn14)],\
                      [(btn20),(btn21),(btn22),(btn23),(btn24)],\
                      [(btn30),(btn31),(btn32),(btn33),(btn34)],\
                      [(btn40),(btn41),(btn42),(btn43),(btn44)]]

            #botones numeros
            #PANEL NUMERICO

##    btnnum1 = Button(juego,text="1",bg="violet red",command=lambda: presionar_numero(1,btnnum1))
##    btnnum2 = Button(juego,text="2",bg="orange",command=lambda: presionar_numero(2,btnnum2))
##    btnnum3 = Button(juego,text="3",bg="dark turquoise",command=lambda: presionar_numero(3,btnnum3))
##    btnnum4 = Button(juego,text="4",bg="orchid",command=lambda: presionar_numero(4,btnnum4))
##    btnnum5 = Button(juego,text="5",bg="gold",command=lambda: presionar_numero(5,btnnum5))
    
    btnnum1 = Button(juego,image=imagen1,relief=FLAT,command=lambda: presionar_numero(1,btnnum1))
    btnnum2 = Button(juego,image=imagen2,relief=FLAT,command=lambda: presionar_numero(2,btnnum2))
    btnnum3 = Button(juego,image=imagen3,relief=FLAT,command=lambda: presionar_numero(3,btnnum3))
    btnnum4 = Button(juego,image=imagen4,relief=FLAT,command=lambda: presionar_numero(4,btnnum4))
    btnnum5 = Button(juego,image=imagen5,relief=FLAT,command=lambda: presionar_numero(5,btnnum5))
    
    listaBotonesNumero = [btnnum1,btnnum2,btnnum3,btnnum4,btnnum5]
    colores = ["violet red","orange","dark turquoise","orchid","gold"]

    #botones generales
    #BOTONES

    btnIniciar = Button(juego,text="INICIAR\nJUEGO",bg="violet red",command=iniciar)
    btnBorrarJugada = Button(juego,text="BORRAR\nJUGADA",bg="orange",command=borrarJugada,state="disabled")
    btnTerminar = Button(juego,text="TERMINAR\nJUEGO",bg="dark turquoise",command=terminar,state="disabled")
    btnBorrar = Button(juego,text="BORRAR\nJUEGO",bg="orchid",command=borrar,state="disabled")
    btnTop10 = Button(juego,text="TOP\n10",bg="gold",command=Top10)

    btnGuardar= Button(juego,text="GUARDAR JUEGO",command=lambda: Guardar(configuracion,cuadriculaBotones,movimientos2,numeroPartida,coordenadas,nombre,h,m,s,Ch,Cm,Cs),state="disabled")
    btnCargar = Button(juego,text="CARGAR JUEGO",command=lambda: Cargar(txtlista,objetosBotones,btnIniciar,btnBorrarJugada,btnTerminar,btnBorrar,btnGuardar,entryNombre))


    #PLACE THEM
    
    btnIniciar.place(x=20,y=430,width=100)
    btnBorrarJugada.place(x=135,y=430,width=100)
    btnTerminar.place(x=249,y=430,width=100)
    btnBorrar.place(x=365,y=430,width=100)
    btnTop10.place(x=480,y=430,width=100)

    btnGuardar.place(x=269,y=520,width=100)
    btnCargar.place(x=395,y=520,width=100)

    #SE COLOCA LA CUADRICULA SEGUN LA CONFIGURACION (IZQ O DER)
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

        btnnum1.place(x=140,y=135,width=30,height=30)
        btnnum2.place(x=140,y=190,width=30,height=30)
        btnnum3.place(x=140,y=245,width=30,height=30)
        btnnum4.place(x=140,y=300,width=30,height=30)
        btnnum5.place(x=140,y=355,width=30,height=30)

        #MATRIZ DE COORDENADAS DE LOS BOTONES DE LA CUADRICULA
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

        btnnum1.place(x=430,y=135,width=30,height=30)
        btnnum2.place(x=430,y=190,width=30,height=30)
        btnnum3.place(x=430,y=245,width=30,height=30)
        btnnum4.place(x=430,y=300,width=30,height=30)
        btnnum5.place(x=430,y=355,width=30,height=30)

        btnGuardar.place(x=190,y=520,width=100)
        btnCargar.place(x=305,y=520,width=100)

        #MATRIZ DE COORDENADAS DE LOS BOTONES DE LA CUADRICULA
        coordenadas = [[(140,125),(195,125),(250,125),(305,125),(360,125)],\
                       [(140,180),(195,180),(250,180),(305,180),(360,180)],\
                       [(140,235),(195,235),(250,235),(305,235),(360,235)],\
                        [(140,290),(195,290),(250,290),(305,290),(360,290)],\
                        [(140,345),(195,345),(250,345),(305,345),(360,345)]]

        #SE COLOCA EL RELOJ DEPENDIENDO DE LA CONFIGURACION
    txthoras0 = Label(juego,text="Horas",relief=GROOVE)
    txtminutos0 = Label(juego,text="Minutos",relief=GROOVE)
    txtsegundos0 = Label(juego,text="Segundos",relief=GROOVE)
    txthoras = Label(juego,relief=GROOVE,bg="#F0F0F0")
    txtminutos = Label(juego,relief=GROOVE,bg="#F0F0F0")
    txtsegundos = Label(juego,relief=GROOVE,bg="#F0F0F0")
    
    if configuracion[1][1] == 1:
        pass
    else:
        txthoras0.place(x=20,y=500)
        txtminutos0.place(x=56,y=500)
        txtsegundos0.place(x=106,y=500)
        txthoras.place(x=20,y=521,width=38,height=40)
        txtminutos.place(x=56,y=521,width=56,height=40)
        txtsegundos.place(x=106,y=521,width=58,height=40)
    
        if configuracion[1][0] == 1:
            txthoras = Label(juego,text="0",relief=GROOVE,bg="#F0F0F0")
            txthoras.place(x=20,y=521,width=38,height=40)
            txtminutos = Label(juego,text="0",relief=GROOVE,bg="#F0F0F0")
            txtminutos.place(x=56,y=521,width=56,height=40)
            txtsegundos = Label(juego,text="0",relief=GROOVE,bg="#F0F0F0")
            txtsegundos.place(x=106,y=521,width=58,height=40)
        
        if configuracion[1][2] == 1:
            txthoras = Label(juego,text=str(configuracion[3][0]),relief=GROOVE,bg="#F0F0F0")
            txthoras.place(x=20,y=521,width=38,height=40)
            txtminutos = Label(juego,text=str(configuracion[3][1]),relief=GROOVE,bg="#F0F0F0")
            txtminutos.place(x=56,y=521,width=56,height=40)
            txtsegundos = Label(juego,text=str(configuracion[3][2]),relief=GROOVE,bg="#F0F0F0")
            txtsegundos.place(x=106,y=521,width=58,height=40)
        

    #DESPLIEGUE DE PARTIDA
    #juego en cuadricula
    txtlista = []
    desplegar_partida()

        
    #BOTON DE CERRAR VENTANA
    Xbtn = Button(juego,text="X",command=cerrar)
    Xbtn.place(x=570,y=0)

                        







#función de configuración de la partida
#contiene la ventana y las funciones anidadas para realizar la configuración
def configurar():

    #las funciones nivel, reloj y lado son funciones para actualizar la configuración
    # y evitar que se puedan seleccionar más de un checkbutton
    #1 significa seleccionado y 0 no seleccionado (on,off)
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


    #funcion para guardar la configuración hecha por el usuario
    #se valida que si se escogió timer, se haya introducido un tiempo límite
    #se crear/sobreescribe el archivo de la configuración
    #se cierra la ventana
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

        derecha,izquierda = IntVar(),IntVar()
        facil,medio,dificil = IntVar(),IntVar(),IntVar()
        si,no,timer= IntVar(),IntVar(),IntVar()
        configraiz.destroy()
        raiz.deiconify()

    #no se guarda ningún cambio hecho
    #se cierra la ventana
    def fin():
        derecha,izquierda = IntVar(),IntVar()
        facil,medio,dificil = IntVar(),IntVar(),IntVar()
        si,no,timer= IntVar(),IntVar(),IntVar()
        configuracion = [[1,0,0],[1,0,0],[1,0]]
        configraiz.destroy()
        raiz.deiconify()
            

    #VENTANA
    raiz.withdraw()
    configraiz = Toplevel(raiz)
    configraiz.resizable(False,False)
    configraiz.geometry("300x260")
    configraiz.configure(bg="#292929")
    configraiz.title("Configuración")

    #LABELS Y CHECKBUTTONS
    
    #la configuración por default está marcada en rojo, si no está marcada se quita lo rojo
    #valores on 1 off 0
    txt1 = Label(configraiz,text="Nivel:",bg="#292929",fg="white").place(x=0,y=0)
    if facil.get() == 1:
        checkbtn1 = Checkbutton(configraiz,text="Fácil",variable=facil,onvalue=1,offvalue=0,bg="#292929",selectcolor="red",command=lambda:nivel(1,checkbtn1,checkbtn2,checkbtn3))
    else:
        checkbtn1 = Checkbutton(configraiz,text="Fácil",variable=facil,onvalue=1,offvalue=0,bg="#292929",command=lambda:nivel(1,checkbtn1,checkbtn2,checkbtn3))
    checkbtn1.place(x=50,y=0)
    
    
    txt = Label(configraiz,text="Fácil",bg="#292929",fg="white").place(x=70,y=3)
    checkbtn2 = Checkbutton(configraiz,text="Intermedio",variable=medio,onvalue=1,offvalue=0,bg="#292929",command=lambda:nivel(2,checkbtn1,checkbtn2,checkbtn3))
    checkbtn2.place(x=50,y=20)
    
    txt = Label(configraiz,text="Intermedio",bg="#292929",fg="white").place(x=70,y=23)
    checkbtn3 = Checkbutton(configraiz,text="Difícil",variable=dificil,onvalue=1,offvalue=0,bg="#292929",command=lambda:nivel(3,checkbtn1,checkbtn2,checkbtn3))
    checkbtn3.place(x=50,y=40)
    
    txt = Label(configraiz,text="Difícil",bg="#292929",fg="white").place(x=70,y=43)

    
    txt2 = Label(configraiz,text="Reloj:",bg="#292929",fg="white").place(x=0,y=80)
    checkbtn4 = Checkbutton(configraiz,text="Sí",variable=si,onvalue=1,offvalue=0,bg="#292929",selectcolor="red",command=lambda:reloj(1,checkbtn4,checkbtn5,checkbtn6))
    if si.get() == 1:
        checkbtn4 = Checkbutton(configraiz,text="Sí",variable=si,onvalue=1,offvalue=0,bg="#292929",selectcolor="red",command=lambda:reloj(1,checkbtn4,checkbtn5,checkbtn6))
    else:
        checkbtn4 = Checkbutton(configraiz,text="Sí",variable=si,onvalue=1,offvalue=0,bg="#292929",command=lambda:reloj(1,checkbtn4,checkbtn5,checkbtn6))
    checkbtn4.place(x=50,y=80)
    
    txt = Label(configraiz,text="Sí",bg="#292929",fg="white").place(x=70,y=83)
    checkbtn5 = Checkbutton(configraiz,text="No",variable=no,onvalue=1,offvalue=0,bg="#292929",command=lambda:reloj(2,checkbtn4,checkbtn5,checkbtn6))
    checkbtn5.place(x=50,y=100)
    
    txt = Label(configraiz,text="No",bg="#292929",fg="white").place(x=70,y=103)
    checkbtn6 = Checkbutton(configraiz,text="Timer",variable=timer,onvalue=1,offvalue=0,bg="#292929",command=lambda:reloj(3,checkbtn4,checkbtn5,checkbtn6))
    checkbtn6.place(x=50,y=120)
    
    txt = Label(configraiz,text="Timer",bg="#292929",fg="white").place(x=70,y=123)

    
    
    txt3 = Label(configraiz,text="Posición del reloj:",bg="#292929",fg="white").place(x=0,y=160)
    checkbtn7 = Checkbutton(configraiz,text="Derecha",variable=derecha,onvalue=1,offvalue=0,bg="#292929",selectcolor="red",command=lambda:lado(1,checkbtn7,checkbtn8))
    if si.get() == 1:
        checkbtn7 = Checkbutton(configraiz,text="Derecha",variable=derecha,onvalue=1,offvalue=0,bg="#292929",selectcolor="red",command=lambda:lado(1,checkbtn7,checkbtn8))
    else:
        checkbtn7 = Checkbutton(configraiz,text="Derecha",variable=derecha,onvalue=1,offvalue=0,bg="#292929",command=lambda:lado(1,checkbtn7,checkbtn8))
    checkbtn7.place(x=100,y=160)
    
    txt = Label(configraiz,text="Derecha",bg="#292929",fg="white").place(x=120,y=163)
    checkbtn8 = Checkbutton(configraiz,text="Izquierda",variable=izquierda,onvalue=1,offvalue=0,bg="#292929",command=lambda:lado(2,checkbtn7,checkbtn8))
    checkbtn8.place(x=100,y=180)
    
    txt = Label(configraiz,text="Izquierda",bg="#292929",fg="white").place(x=120,y=183)

    


    #RELOJ
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
    

    #BOTONES GUARDAR O CANCELAR
    okbtn = Button(configraiz,text="Ok",command=guardar)
    okbtn.place(x=30,y=220,width=30)
    cancelbtn = Button(configraiz,text="Cancelar",command=fin)
    cancelbtn.place(x=80,y=220,width=60)



#funcion para desplegar el menu de usuario
def ayuda():
    wb.open_new(r"Manual_de_usuario_futoshiki.pdf")


#funcion acerca del programa
def acercade():
    acerca = Toplevel(raiz)
    acerca.geometry("300x200")
    acerca.config(relief="raised")
    acerca.configure(bg="#292929")
    acerca.resizable(False,False)
    Label1 = Label(acerca,text="\n\nPrograma Futoshiki \n\n Fiorella Zelaya Coto \n\n Fecha de creación: 03/06/2021 \n\n Versión 1.0.0",bg="#292929",fg="white").pack()
    btnX = Button(acerca,text="X",command=acerca.destroy).place(x=270,y=0,width=30)






## programa principal ##

    #variables
configuracion = [[1,0,0],[1,0,0],[1,0]]
actual = []
#txtlista = []
h,m,s = 0,0,0
Ch,Cm,Cs = 0,0,0
botonNumero = 0
variableIniciar = 0
tiempoJugado = ""
nombre = ""


#se intenta leer un archivo, si existe
try:
    archivo = open("futoshiki2021top10.dat","rb")
    top10listas = pickle.load(archivo)
    Top10facil = top10listas[0]
    Top10intermedio = top10listas[1]
    Top10dificil = top10listas[2]
except:
    Top10facil = []
    Top10intermedio = []
    Top10dificil = []


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



#VENTANA                 
raiz = Tk()
raiz.resizable(False,False)
raiz.geometry("512x384")
raiz.configure(bg="light gray")
raiz.title("futoshiki")

derecha,izquierda = IntVar(value=1),IntVar()
facil,medio,dificil = IntVar(value=1),IntVar(),IntVar()
si,no,timer= IntVar(value=1),IntVar(),IntVar()

fondo = PhotoImage(file="futoshiki.png")
Labelfondo = Label(raiz,image=fondo).pack()

imagen1 = PhotoImage(file="boton1.png")
imagen2 = PhotoImage(file="boton2.png")
imagen3 = PhotoImage(file="boton3.png")
imagen4 = PhotoImage(file="boton4.png")
imagen5 = PhotoImage(file="boton5.png")
imagenesBotones = [imagen1,imagen2,imagen3,imagen4,imagen5]

imagen1p = PhotoImage(file="boton1p.png")
imagen2p = PhotoImage(file="boton2p.png")
imagen3p = PhotoImage(file="boton3p.png")
imagen4p = PhotoImage(file="boton4p.png")
imagen5p = PhotoImage(file="boton5p.png")
imagenesBotonesp = [imagen1p,imagen2p,imagen3p,imagen4p,imagen5p]

#BOTONES 
ButtonJugar = Button(raiz,text="Jugar",command=jugar,font=("cambria", 15),fg="white",bg="#292929")
ButtonConfigurar = Button(raiz,text="Configurar",command=configurar,font=("cambria", 15),fg="white",bg="#292929")
ButtonJugar.place(x=165,y=250,width=180)
ButtonConfigurar.place(x=165,y=290,width=180)
ButtonAyuda = Button(raiz,text="Ayuda",command=ayuda,font=("cambria", 15),fg="white",bg="#292929")
ButtonSalir = Button(raiz,text="Salir",command=raiz.destroy,font=("cambria", 15),fg="white",bg="#292929")
ButtonAyuda.place(x=165,y=330,width=90)
ButtonSalir.place(x=255,y=330,width=90)
ButtonAcercade = Button(raiz,text="Acerca de",command=acercade,font=("cambria", 8),fg="white",bg="#292929")
ButtonAcercade.place(x=230,y=225)

raiz.mainloop()
