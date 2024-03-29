﻿from Tkinter import *
from temporizador import *
from threading import *
from time import *


class InterfazTemporizador(Thread):

    def __init__(self):
        self.root = Tk()
        self.temporizador = Temporizador()
        self.frame = Frame(self.root)
        self.frame.pack()

        #Texto para iniciar  el temporizador
        self.inicio = StringVar()
        self.inicio.set("00 : 00 : 00")
        self.text = Entry(self.frame, textvariable = self.inicio, justify="center")
        self.text.pack(side=TOP)

        #Etiqueta para mostrar valor del temporizador
        self.tiempo = StringVar()
        self.display = Label(self.frame, textvariable = self.tiempo, font=("Helvetica",30))
        self.display.pack(side=TOP)

        self.boton_iniciar = Button(self.frame, text="Iniciar/Parar")
        self.boton_iniciar.bind("<Button-1>", self.cambiar)
        self.boton_iniciar.pack(side=LEFT)

        self.boton_establecer = Button(self.frame, text="Establecer")
        self.boton_establecer.bind("<Button-1>", self.establecer)
        self.boton_establecer.pack(side=RIGHT)

        Thread.__init__(self)
        self.start()

        self.root.mainloop()

    def cambiar(self, event):       #Se asocia la variable event porque la función está asociada a un botón
        self.temporizador.parado = not self.temporizador.parado

    def establecer(self, event):
        try:
            lista = [int(x) for x in self.inicio.get().split(" : ")]
        except:
            lista = [0,0,0]
        self.temporizador.iniciar(lista)


    def run(self):              #Hilo de ejecución de "Thread"
        while True:
            if not self.temporizador.parado:
                self.temporizador.retroceder()
            sleep(0.5)
            self.tiempo.set(self.temporizador.mostrar_tiempo())

        
            
app = InterfazTemporizador()


