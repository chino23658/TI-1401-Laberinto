#Importamos las librerias necesarias
import pygame
import random
from tkinter import *
from random import randint

##*************************************Funcion de aumeto de probabilidad****************************************************************
def applanar1(ba):
    lista1=[]
    for g in ba:                             # Estas 6 funciones de aumento de la probabilidad fueron creadas para resolver un problema quenos
        if isinstance(g,str):                 #nos presentaba la fucion random.shuffle que cuando se encargaba de mezclar los unos y ceros en combinaciones aleatorias
            lista1=lista1+[g]                 #casi simpre nos producia combinaciones que obstrian la salida por lo que obtamos por crear una funcion que aumetara la
        elif isinstance(g,list):              #lacantidad de ceros que hay cerca de la salida grarntizandoque la matoria por no decir todas las matrices producidas
            for h in g:                       #por el modo automatico sean resolvibles.
                if isinstance(h,list): 
                    for j in h:
                        lista1=lista1+[j]         #Estas funciones cuentan con :
                                                  # **Funcion Comprobar** estas funciones se encargan de tomar los strings unidos de unos y ceros y los separa para 
    return lista1                                 ##para unirlos en una lista. 
                                                  #**Funcion Quitar** esta genera los ceros para aumetar las probablidades                          

def quitar2(a):                                  # **Funcio Aplanar** se encarga de aplanar las listas donde los ceros y unos fueron introducidos para formar un vector
    lista11=[]                                     #añadibles a la matriz que genera el laberinto.
    while lista11==[]:
        lista11=[comprobar5("0"*(int(a)-2))]
    return lista11

        
def comprobar5(num4):
    resultado5=[]
    for k in num4:
        if isinstance(num4,str):
            resultado5=resultado5+[k]
    return resultado5
##******************************************Funcion de aunmeto de la probabilidad********************************************************************


def applanar(bc): 
    lista111=[]
    for z in bc:
        if isinstance(z,str):
            lista111=lista111+[z]
        elif isinstance(z,list):
            for d in z:                         
                if isinstance(d,list):
                    for f in d:
                        lista111=lista111+[f]
    return lista111
    

def quitar(a):
    lista1111=[]
    while lista1111==[]:
        lista1111=[comprobar4("0"*(int(a)-2))]
    return lista1111

        
def comprobar4(num3):
    resultado4=[]
    for a in num3:
        if isinstance(num3,str):
            resultado4=resultado4+[a]
    return resultado4
##************************************************Funcion mezcladora de padered Superior ********************************************************************************************************

def comprobar2(num):
    resultado1=[]                          #Estas fuciones fueron creadas con la intencion de crear la distribucion aleatoria de las salidas en las pared superior  
    for i in num:                           #e inferior.
        if isinstance(num,str):           
            resultado1=resultado1+[i]       #Utiliza la funcion***Comprobar**** que se utiliza para la divicion y el procesamiento de los strings unidos.
    return resultado1                       #Funcio***Mezclar***que le añade los unos conforman los ladrillos de la pared y el 2 o 3 que conforman las salidas      
                                            #Fucion ***apla** aplana las listas donde se introducieron las pares para formar vectores compatibles conla matriz generda
def mezclar1(a):                              
    res=[]
    while res==[]:
        res=res+[comprobar2("1"*(int(a)-1))]
        res=res+["2"]
    return apla(res)

def apla(res):
    result1=[]
    for reco in res:
        if isinstance(reco,list):
            for el3 in reco:
                result1=result1+[el3]
        elif isinstance(reco,str):
            result1=result1+[reco]
            random.shuffle(result1)
    return result1
##*********************************************************Funcion mezcladora de pared Inferior**************************************************************************************

def comprobar3(num1):
    resultado2=[]
    for e in num1:
        if isinstance(num1,str):
            resultado2=resultado2+[e]
    return resultado2

def mezclar2(a):
    res1=[]
    while res1==[]:
        res1=res1+[comprobar3("1"*(int(a)-1))]
        res1=res1+["3"]
    return apla1(res1)

def apla1(res1):
    result11=[]
    for reco1 in res1:
        if isinstance(reco1,list):
            for el31 in reco1:
                result11=result11+[el31]
        elif isinstance(reco1,str):
            result11=result11+[reco1]
            random.shuffle(result11)
    return result11
##****************************************************Distribuidor y ordenamiento de matriz***************************************************************************************************            
##    
    
def comprobar(numero2,numero):                        #Estas funciones se encargan de construir el cuerpo aleatorio de la matriz al mismo tiempo permite
    resultado=[]                                      #manejo de la trivialidad del laberinto aumentando o diminuyendola cantidadde seros en los randgos establecidos 
    for ele in numero2:                               #en la funcion******* Distibuidor de variables ****** esta funcion detecta sielnumeroingresado por el
        if isinstance(numero2,str):                   #usuario es para o impar en el caso de ser par elancho de la matriz solicida buscara un balance entre los unosy 
            resultado=resultado+[ele]                 #ceros para una trivialidad media debidoa que ingresa lamitadde unos ceros aunque este parametropude ser modificado 
    for ele1 in numero:                               #disminuyendo los unos y aumentandolos ceros para un nivelmas bajo o aumentandolos unos y disminuyendolos ceros 
        if isinstance(numero,str):                    #para una dificultad mas elevada para modificar estosparametros se tien que tener en cuenta que se tiene que aumentar
            resultado=resultado+[ele1]                #el mismo numero de cerosy unos para que el generador funcione a la perfeccion.
    
    return shuffle(resultado)                         #Luego de inicializarse el Distribuidor se activa otra funcion ****Comprobar*** que cumple la misma fucion que 
                                                      #los anteriores.

def shuffle(resultado):                               #Por ultimo tenemosla funciones secundarias ****shuffle*** que mezcla los cerosy unos mediante la libreria
    if isinstance(resultado,list):                    #random y por ultimo***producir**** este se encarga de convocar al ditribuidor que (enzambla la matriz) y lo
        random.shuffle(resultado)                     #une con las paredes inferior y superior, basicamente esta ultima se encarga del ordenamineto de la matriz.
    return resultado[0:-1]

    
def Distribuidor_de_valriables(a):
    if a>30:
        if(int(a)%2)==0:
            numero2="1"*((int(a)-11)//2)
            numero="0"*((int(a)+11)//2)
            return comprobar(numero2,numero)
        else:
            if(a%2)==1:
                numero2="1"*(int(a)-25)
                numero="0"*25
                return comprobar(numero2,numero)
    
    elif a>25 and a<=30:
        if(int(a)%2)==0:
            numero2="1"*((int(a)-9)//2)
            numero="0"*((int(a)+9)//2)
            return comprobar(numero2,numero)
        else:
            if(a%2)==1:
                numero2="1"*(int(a)-17)
                numero="0"*17
                return comprobar(numero2,numero)
    elif a<=25 and a>15:
        if(int(a)%2)==0:
            numero2="1"*((int(a)-7)//2)
            numero="0"*((int(a)+7)//2)
            return comprobar(numero2,numero)
        else:
            if(a%2)==1:
                numero2="1"*(int(a)-15)
                numero="0"*15
                return comprobar(numero2,numero)
    elif a<=15 and a>10:
        if(int(a)%2)==0:
            numero2="1"*((int(a)-4)//2)
            numero="0"*((int(a)+4)//2)
            return comprobar(numero2,numero)
        else:
            if(a%2)==1:
                numero2="1"*(int(a)-8)
                numero="0"*8
                return comprobar(numero2,numero)
    elif a<=10:
        if(int(a)%2)==0:
            numero2="1"*((int(a)-1)//2)
            numero="0"*((int(a)+1)//2)
            return comprobar(numero2,numero)
        else:
            if(a%2)==1:
                numero2="1"*(int(a)-6)
                numero="0"*6
                return comprobar(numero2,numero)
        
    
        

def producir2(a,b):
    if not isinstance(int(b),int):
        return "Error de entrada"
    contador=0
    result=[]
    while contador!=int(b):
       result=result+[[1,Distribuidor_de_valriables(int(a)),1]]
       contador+=1
       bc=["1",quitar(a),"1"]
       ba=["1",quitar2(a),"1"]
    return[mezclar1(a)]+[applanar(bc)]+aplanar(result)[2:-2]+[applanar1(ba)]+[mezclar2(a)]

def aplanar(lista):
    res=[]
    for elementos in lista:
        if isinstance(elementos,list):
            for numeros in elementos:
                if isinstance(numeros,list):
                    res+=[["1"]+numeros+["1"]]
        if isinstance(elementos,int):
            res+=[elementos]
    return res
        
##*********************************************************************************************************************************


def validar (a,b):
    try:
        print("a: ",a," b:",b)
        num_a = int(a)
        num_b = int(b)
    except:
        print("Dimensiones no válidas")
        return []
    return producir2(num_a,num_b)

#Busqueda de solucion#

def principio_solucion(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == "2" or matriz[fila][columna] == 2:
                return (fila,columna)

def obtener_vecinos(coordenadas,laberinto):
    tuplas=[]
    fila,columna=coordenadas[0],coordenadas[1]
    # Abajo
    if fila < len(laberinto)-1 and laberinto[fila+1][columna] in [0,3,"0","3"]:
        tuplas+=[(fila+1,columna)]
    # Arriba
    if fila > 0 and laberinto[fila-1][columna] in [0,3,"0","3"]:
        tuplas+=[(fila-1,columna)]
    # Derecha
    if columna < len(laberinto[0])-1 and laberinto[fila][columna+1] in [0,3,"0","3"]:
        tuplas+=[(fila,columna+1)]
    # Izquierda
    if columna > 0 and laberinto[fila][columna-1] in [0,3,"0","3"]:
        tuplas+=[(fila,columna-1)]
    return tuplas
    

def solucionable(laberinto):
    por_revisar=[principio_solucion(laberinto)]
    ruta=[]
    while por_revisar!=[]:
        (filas,columnas) = por_revisar[-1]
        por_revisar = por_revisar[:-1]
        if laberinto[filas][columnas]==3:
            ruta.append((filas,columnas))
            break
        else:
            laberinto[filas][columnas]=4            
            otros_ceros=obtener_vecinos((filas,columnas),laberinto)
            if otros_ceros!=[]:
                por_revisar+=otros_ceros
                ruta+=[[(filas,columnas),len(otros_ceros)]]
            else:
                while ruta !=[]:
                    ruta[-1][1] -= 1
                    if ruta[-1][1] ==0:
                        ruta = ruta[:-1]
                    else:
                        break
                if ruta == []:
                    break
        print("Las casillas que falta revisar son:",por_revisar)
        print("La ruta actual es:",ruta)
    return ruta

#Leer .txt#

def leer_laberinto(archivo):
    laberinto = []
    entrada = open(archivo,"r")
    try:
        lineas = entrada.readlines()
        entrada.close()                
    except:
        return []
    for linea in lineas:
        filastr = linea.strip("[],\n").split(",")
        filanum = []
        for x in filastr:
            filanum.append(int(x))
        laberinto.append(filanum)
    print(laberinto)
    return laberinto

#creamos variables#

rectangulos=[]
salidas=[]

#lee la matriz y crea las coordenadas de los sprites y rectangulos#

def leer(matriz):
    global rectangulos
    rectangulos=[]
    rec_pared=[]
    w=12
    h=12
    x=2
    y=2
    for vectores in matriz:
        for elemento in vectores:
            if elemento=="1" or elemento==1:
                rectangulos.append(pygame.Rect(x+2.5,y+2.5,w,h))
                rec_pared.append((x,y))
                x+=16
            if elemento=="0" or elemento==0:
                x+=16
            if elemento=="2" or elemento==2:
                x+=16
            if elemento=="3" or elemento==3:
                x+=16
        y+=16
        x=2
    return rec_pared

#busca el inicio y da las coordenadas de la misma para yoda #

def inicio(matriz):
    rec_pared=[]
    x=2
    y=2
    for vectores in matriz:
        for elemento in vectores:
            if elemento=="2" or elemento==2:
                return x+1,y
            if elemento=="0" or elemento==0:
                x+=16
            if elemento=="1" or elemento==1:
                x+=16
            if elemento=="3" or elemento==3:
                x+=16
        y+=16
        x=2
    return rec_pared

#busca los finales y sus coordenadas para la creacion de sprites y rects#

def final(matriz):
    global salidas
    salidas=[]
    rec_pared=[]
    w=12
    h=12
    x=2
    y=2
    for vectores in matriz:
        for elemento in vectores:
            if elemento=="2" or elemento==2:
                x+=16
            if elemento=="0" or elemento==0:
                x+=16
            if elemento=="1" or elemento==1:
                x+=16
            if elemento=="3" or elemento==3:
                salidas.append(pygame.Rect(x+2.5,y+2.5,w,h))
                rec_pared.append((x,y))
                x+=16
        y+=16
        x=2
    return rec_pared

#juego pygame laberinto código#

def juego():
    global matriz
    print(matriz)
    laberinto=leer(matriz)
    principio=inicio(matriz)
    salida=final(matriz)
    #iniciamos los modulos#
    pygame.init()
    #creamos ventana y fondo donde se pondran imagenes#
    superficie=pygame.display.set_mode((800,450))
    #titulo de la ventana#
    pygame.display.set_caption("Yodaberinto")
    #variable de salida#
    salir=False
    #creamos un timer#
    tiempo=pygame.time.Clock()
    #datos sobre texto y su impresion#
    letra=pygame.font.SysFont("Castellar", 25, True, True)
    texto=letra.render("Yodaberinto",0,(150,225,250))
    #extraemos musica#
    pygame.mixer.music.load("Weird al yankovic-Yoda with lyrics.wav")
    #extraemos imagenes#
    r2d2_final=pygame.image.load("r2d2.gif").convert_alpha()
    pantano_fondo=pygame.image.load("DarkSideCave.jpg").convert_alpha()
    trooper_muro=pygame.image.load("trooper.png").convert_alpha()
    yoda_jugador=pygame.image.load("yoda_papier.jpg").convert_alpha()

    #creamos variables de movimiento#
    velocidadx=0
    velocidady=0

    #asignamos sprite de RD2D#
    r2d2=pygame.sprite.Sprite()
    r2d2.image=r2d2_final
    r2d2.rect=r2d2_final.get_rect()
    r2d2.rect.top=0
    r2d2.rect.left=0

    #asignamos sprite de fondo#
    cueva=pygame.sprite.Sprite()
    cueva.image=pantano_fondo
    cueva.rect=pantano_fondo.get_rect()
    cueva.rect.top=0
    cueva.rect.left=0

    #asignamos sprite de paredes(los troopers)#
    trooper=pygame.sprite.Sprite()
    trooper.image=trooper_muro
    trooper.rect=trooper_muro.get_rect()
    trooper.rect.top=0
    trooper.rect.left=0

    #asignamos sprite de yoda(jugador)#
    yoda=pygame.sprite.Sprite()
    yoda.image=yoda_jugador
    yoda.rect=yoda_jugador.get_rect()
    yoda.rect.top=principio[1]
    yoda.rect.left=principio[0]
    #reproducimos la musica#
    pygame.mixer.music.play(99)
    #asignamos que debe suceder al interactuar con la ventana#
    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                salir = True
                break
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    velocidady-=8
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    velocidady+=8
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    velocidadx-=8
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    velocidadx+=8
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    salir = True
                    break
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                    velocidadx=0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_w:
                    velocidady=0
        if salir:
            break
        #creamos coordenadas pasadas de personaje para usarlas en colisiones#
        anteriorx=yoda.rect.left
        anteriory=yoda.rect.top
        #determinamos el movimiento del jugador#
        yoda.rect.move_ip(velocidadx,velocidady)
        #determinamos que hacer si colisiona con una pared#
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for muros in rectangulos:
                if yoda.rect.colliderect(muros):
                    yoda.rect.left=anteriorx
                    yoda.rect.top=anteriory
        #determinamos que hace si encuentra la salida#
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for R2D2 in salidas:
                if yoda.rect.colliderect(R2D2):
                    pygame.quit()
                    salir = True
                    break
        if salir:
            break
        #utilizamos el timer para delimitar el consumo de recursos de la computadora#
        tiempo.tick(15)
        #introducimos los sprites a la ventana#
        superficie.blit(cueva.image,cueva.rect)
        superficie.blit(yoda.image,yoda.rect)
        superficie.blit(texto,(563,7))
        #determinamos los sprites y rectangulos que se deben clonar#
        for muros in rectangulos:
            pygame.draw.rect(superficie,(200,200,200),muros)
        for paredes in laberinto:
            superficie.blit(trooper.image,paredes)
        for vacios in salidas:
            pygame.draw.rect(superficie,(200,200,200),vacios)
        for yodas in salida:
            superficie.blit(r2d2.image,yodas)
        #asignamos que actualice constantemente la ventana#
        pygame.display.update()
    ventana.mainloop()
#####################################################

#ventana principal#

ventana = Tk()

ventana.title("Pre-Laberinto") 
ventana.minsize(250,154) 
ventana.maxsize(250,154)

#Barra de herramientas#

def SobreLosAutores():
    messagebox.showinfo("Autores","Benjamin Calvo de León\nCarné: 201235868\nJuan Fabricio Soto Mejías\nCarné: 201250955\nJose Andrés Hernández\nCarné:201235912\nCarlos Alberto Campos Fuentes\nCarné: 201250962\nTarea Programada#2\nTaller de Programación\nProfesor Andrei Fuentes")

def Salir():
    messagebox.showinfo("Hasta luego","Que la fuerza te acompañe")
    ventana.destroy()

barraherramientas = Menu(ventana)
barraherramientas.add_command(label="Sobre los Autores", command=SobreLosAutores)
barraherramientas.add_command(label="Salir del programa", command=Salir)
ventana.config(menu=barraherramientas)

#canvas(para color en el fondo)#

canvas = Canvas(ventana , width= 500, height = 500,bg = "Black")
canvas.place(x=0, y=0)

#Marcos#

marco = LabelFrame(ventana, text="Nombre del archivo (Modo Manual)", width = 248, height = 44)
marco.place(x = 1.5, y = 1)

marco2 = LabelFrame(ventana, text="Ancho        (Modo Automatico)         Alto", width = 248, height = 44)
marco2.place(x = 1.5, y = 110)


#barra de entrada#

entradas=StringVar()

barra_de_entrada = Entry(ventana, width = 39, textvariable=entradas)
barra_de_entrada.place(x=4.5,y=18)

entradas_numericas1=IntVar()
entradas_numericas2=IntVar()

barra_de_entrada_Ancho=Entry(ventana, width = 11, textvariable=entradas_numericas1)
barra_de_entrada_Ancho.place(x=24.5,y=127.5)

barra_de_entrada_Alto=Entry(ventana, width = 11, textvariable=entradas_numericas2)
barra_de_entrada_Alto.place(x=150,y=127.5)

#Acciones de botones#

def Manual():
    global matriz
    direccion=barra_de_entrada.get()
    matriz = leer_laberinto(direccion)
    if matriz != []:
        # Agregar lo que falta para las cabecillas
        ventana.quit()
        juego()
    else:
        print("Error: las dimensiones de la matriz son no válidas. Compruebe que sean valores númericos, y que estén en el rango apropiado.")
    
def Automatico():
    global matriz
    #ancho=barra_de_entrada_Ancho.get()
    ancho = entradas_numericas1.get()
    #alto=barra_de_entrada_Alto.get()
    alto = entradas_numericas2.get()
    print("Ancho:",ancho," Alto:",alto)
    matriz= validar(ancho,alto)
    if matriz != []:
        print("Generé una matriz de",alto,"filas por",ancho,"columnas")
        # Agregar lo que falta para las cabecillas
        ventana.quit()
        juego()
    else:
        print("Error: las dimensiones de la matriz son no válidas. Compruebe que sean valores númericos, y que estén en el rango apropiado.")

#Botones#

botonManual = Button(ventana, text="Manual", command=Manual, bg = "#EFFBFB", fg = "#0B0B3B")
botonManual.place(x=30,y=65)

botonAutomatico = Button(ventana, text="Automatico", command=Automatico, bg = "#EFFBFB", fg = "#0B0B3B")
botonAutomatico.place(x=130,y=65)


#abrir ventana y mantener abierta#

ventana.mainloop()

