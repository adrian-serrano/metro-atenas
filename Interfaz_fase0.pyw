"""
@author: Grupo 26
"""

from tkinter import *
import AlgoritmoEstrella as AE


class UI(Frame):
    #
    #Funciones
    #
    def __init__(self):
        self.inicial = None
        self.nombreI = None
        self.nombreF = None
        self.lineaInicial = None
        self.final = None  
        self.lineaFinal = None
        self.numTransbordos = None
        self.longitud = None
        ventana = Tk()
        self.frame0(ventana)
        self.estrella = None
    
    
    def put(self,texto,linea,ventana):
    
        ventana.wm_title("Line Selector")
        Label(ventana, text="Seleccionar linea",bg = "white", fg='black', font=('Helvetica', 12,"bold")).place(x=460, y=540)
        
        if texto == "Attiki":

           
            
            buttonImage1 =  PhotoImage(file = r"img/rsz_number-1.png")
            button = Button(ventana, borderwidth = 0, image = buttonImage1, command = lambda: self.put2(texto,1,ventana))
            button.place(x=480, y=570)
            
            buttonImage2 =  PhotoImage(file = r"img/rsz_number-2.png")
            button2 = Button(ventana, borderwidth = 0, image = buttonImage2, command = lambda: self.put2(texto,2,ventana))
            button2.place(x=535, y=570)
            
            
            
            
        elif texto == "Omonia":

          
            
            buttonImage1 =  PhotoImage(file = r"img/rsz_number-1.png")
            button = Button(ventana, borderwidth = 0, image = buttonImage1, command = lambda: self.put2(texto,1,ventana))
            button.place(x=480, y=570)
            
            buttonImage2 =  PhotoImage(file = r"img/rsz_number-2.png")
            button2 = Button(ventana, borderwidth = 0, image = buttonImage2, command = lambda: self.put2(texto,2,ventana))
            button2.place(x=535, y=570)
            
            
        
        elif texto == "Monastiraki":


       
            
            buttonImage1 =  PhotoImage(file = r"img/rsz_number-1.png")
            button = Button(ventana, borderwidth = 0, image = buttonImage1, command = lambda: self.put2(texto,1,ventana))
            button.place(x=480, y=570)
            
            buttonImage2 =  PhotoImage(file = r"img/rsz_number-3.png")
            button2 = Button(ventana, borderwidth = 0, image = buttonImage2, command = lambda: self.put2(texto,3,ventana))
            button2.place(x=535, y=570)
            
                
            
        elif texto == "Syntagma":

         
            
            buttonImage1 =  PhotoImage(file = r"img/rsz_number-2.png")
            button = Button(ventana, borderwidth = 0, image = buttonImage1, command = lambda: self.put2(texto,2,ventana))
            button.place(x=480, y=570)
            
            buttonImage2 =  PhotoImage(file = r"img/rsz_number-3.png")
            button2 = Button(ventana, borderwidth = 0, image = buttonImage2, command = lambda: self.put2(texto,3,ventana))
            button2.place(x=535, y=570)
            
            
            
        else:   
            self.put2(texto,linea,ventana)
            
        ventana.mainloop() 
                
            
    def put2(self,texto,linea,ventana):
        if self.inicial == None:
            self.inicial = texto
            self.lineaInicial = linea
            self.frame2(ventana)
            
        else:
            self.final = texto
            self.lineaFinal = linea
            
            if(self.inicial == "Monastiraki" or self.inicial == "Omonia" 
               or self.inicial == "Attiki" or self.inicial == "Syntagma"):
                 self.nombreI = self.inicial
                 self.inicial  = self.inicial +  str(self.lineaInicial)
                
                
            if(self.final == "Monastiraki" or self.final == "Omonia" 
               or self.final == "Attiki" or self.final == "Syntagma"):
                self.nombreF = self.final
                self.final = self.final + str(self.lineaFinal)
                
            
            
            self.estrella = AE.AlgoritmoEstrella(self.inicial, self.final)
            self.estrella.apply()
            self.frame3(ventana)
            
    def frame3(self,ventana):
        path,transfers,time = self.estrella.convertSolution()
        #Titulo
        ventana.title("Atenas")
        #icono
        ventana.iconbitmap("img/attiko.ico")
        #Tamaño
        ventana.geometry("1065x1167")
        #background
        bgImage = PhotoImage(file = r"img/fondoB.png")
        Label(ventana, image = bgImage).place(relwidth = 1, relheight = 1)
        #La ventana no es escalable
        ventana.resizable(0,0)
        
        canvas1= Canvas(ventana, width = 450, height = 980,  relief = 'raised')
        canvas1.place(x=330, y=50) 
                
        
        container = Frame(ventana)
        canvas = Canvas(container, width = 350, height = 450,  relief = 'raised')
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
 
        
        Label(scrollable_frame, text=path, justify=LEFT, font=('Helvetica', 12)).pack()
        
        Label(scrollable_frame, text="").pack()

        
        container.place(x=350, y=490) 
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        
   
        exitImage =  PhotoImage(file = r"img/X.png")
        exitbutton = Button(ventana, borderwidth = 0, image = exitImage, command = lambda: ventana.destroy())
        exitbutton.place(x=950, y=50)
        
        
        #buscar otro origen
        button = Button(ventana, text = "  Nueva ruta   ",bg='brown', fg='white',font=('Helvetica', 10, "bold"), command = lambda: self.frame0(ventana))
        button.place(x=405, y=970)
        #buscar otro destino
        button = Button(ventana, text = " Nuevo destino ",bg='brown', fg='white',font=('Helvetica', 10, "bold"), command = lambda: self.frame2(ventana))
        button.place(x=625, y=970)
        
        label = Label(ventana, text="Metro Atenas", font=('Helvetica', 18, "bold"))
        label.place(x=480,y=75)
        
        
        #Parada de inicio
        inicio = Label(ventana, text="Inicio:", font=('Helvetica', 18, "bold"))
        inicio.place(x=350, y=150)
        if(self.inicial == "Monastiraki1" or self.inicial == "Omonia1" 
               or self.inicial == "Attiki1" or self.inicial == "Syntagma2" 
               or self.inicial == "Monastiraki3" or self.inicial == "Omonia2" 
               or self.inicial == "Attiki2" or self.inicial == "Syntagma3"):
            
            inicio = Label(ventana, text=self.nombreI, font=('Helvetica', 18))
        else:
            inicio = Label(ventana, text=self.inicial, font=('Helvetica', 18))
            
        inicio.place(x=430, y=152)
        
        inicio = Label(ventana, text="Linea:", font=('Helvetica', 18, "bold"))
        inicio.place(x=350, y=185)
        inicio = Label(ventana, text=str(self.lineaInicial), font=('Helvetica', 18))
        inicio.place(x=430, y=187)
        
        #Parada final
        inicio = Label(ventana, text="Destino:", font=('Helvetica', 18, "bold"))
        inicio.place(x=350, y=240)
        if(self.final == "Monastiraki1" or self.final == "Omonia1" 
               or self.final == "Attiki1" or self.final == "Syntagma2" 
               or self.final == "Monastiraki3" or self.final == "Omonia2" 
               or self.final == "Attiki2" or self.final == "Syntagma3"):
            
            inicio = Label(ventana, text=self.nombreF, font=('Helvetica', 18))
        else:
            inicio = Label(ventana, text=self.final, font=('Helvetica', 18))
        
        inicio.place(x=454, y=242)
        
        inicio = Label(ventana, text="Linea:", font=('Helvetica', 18, "bold"))
        inicio.place(x=350, y=275)
        inicio = Label(ventana, text=str(self.lineaFinal), font=('Helvetica', 18))
        inicio.place(x=430, y=277)
        
        #Transbordos
        inicio = Label(ventana, text="Numero de transbordos:", font=('Helvetica', 18, "bold"))
        inicio.place(x=350, y=335) 
        inicio = Label(ventana, text=str(transfers), font=('Helvetica', 18))                             
        inicio.place(x=645, y=337)
        #Tiempo
        inicio = Label(ventana, text="Tiempo del trayecto:", font=('Helvetica', 18, "bold"))
        inicio.place(x=350, y=390) 
        inicio = Label(ventana, text=str(round(time/60))+" minutos", font=('Helvetica', 18))                             
        inicio.place(x=600, y=392)
        #Ruta
        inicio = Label(ventana, text="Ruta:", font=('Helvetica', 18, "bold"))
        inicio.place(x=350, y=450) 
    

        
      
        ventana.mainloop()
        
    def frame2(self,ventana):
       
        #Titulo
        ventana.title("Atenas")
        #icono
        ventana.iconbitmap("img/attiko.ico")
        #bg
        ventana.configure(bg = "white")
        #Tamaño
        ventana.geometry("1065x1167")
        #La ventana no es escalable
        ventana.resizable(0,0)
        #bg image
        bgImage = PhotoImage(file = r"img/Atenas.png")
        Label(ventana, image = bgImage).place(relwidth = 1, relheight = 1)
        
        
        buttonAtras = Button(ventana, text = "Undo", bg='brown', fg='white', command = lambda: self.frame1(ventana))
        buttonAtras.place(x=50, y=50)
        
        exitImage =  PhotoImage(file = r"img/X.png")
        exitbutton = Button(ventana, borderwidth = 0, image = exitImage, command = lambda: ventana.destroy())
        exitbutton.place(x=950, y=50)     
        
        #image button
        buttonImage =  PhotoImage(file = r"img/RoundButton.png")
        
        
        label = Label(ventana, text="Estación origen:", bg="white",fg="red",font=('Helvetica', 18, "bold"))
        label.place(x=350,y=60)
     
        origen = Label(ventana, bg="white", text=self.inicial,fg="red", font=('Helvetica', 18, "bold"))
        origen.place(x=550, y=60)
        
        #label = Label(ventana, text="Estación destino:", bg="white",font=('Helvetica', 18, "bold"))
        #label.place(x=350,y=100)


        # botones linea 1
        button4 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Victoria", 1, ventana))
        button4.place(x=314, y=626)
        button4.config(bg="green", activebackground="green")
        button34 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Monastiraki", 1, ventana))
        button34.place(x=315, y=723)
        button34.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button35 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Thissio", 1, ventana))
        button35.place(x=314, y=779)
        button35.config(bg="green", activebackground="green")
        button36 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Petralona", 1, ventana))
        button36.place(x=300, y=815)
        button36.config(bg="green", activebackground="green")
        button16 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Tavros", 1, ventana))
        button16.place(x=265, y=850)
        button16.config(bg="green", activebackground="green")
        button17 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Kallithea", 1, ventana))
        button17.place(x=232, y=884)
        button17.config(bg="green", activebackground="green")
        button18 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Moschato", 1, ventana))
        button18.place(x=199, y=917)
        button18.config(bg="green", activebackground="green")
        button19 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Faliro", 1, ventana))
        button19.place(x=161, y=951)
        button19.config(bg="green", activebackground="green")
        button20 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Piraeus", 1, ventana))
        button20.place(x=28, y=967)
        button20.config(bg="green", activebackground="green")
        button21 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Agios Nikolaos", 1, ventana))
        button21.place(x=286, y=524)
        button21.config(bg="green", activebackground="green")
        button22 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Kato Patissia", 1, ventana))
        button22.place(x=318, y=492)
        button22.config(bg="green", activebackground="green")
        button23 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Agios Eleftherios", 1, ventana))
        button23.place(x=350, y=458)
        button23.config(bg="green", activebackground="green")
        button24 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Ano Patissia", 1, ventana))
        button24.place(x=380, y=429)
        button24.config(bg="green", activebackground="green")
        button25 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Perissos", 1, ventana))
        button25.place(x=408, y=400)
        button25.config(bg="green", activebackground="green")
        button26 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Pefkakia", 1, ventana))
        button26.place(x=437, y=370)
        button26.config(bg="green", activebackground="green")
        button27 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Nea Ionia", 1, ventana))
        button27.place(x=464, y=344)
        button27.config(bg="green", activebackground="green")
        button28 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Iraklio", 1, ventana))
        button28.place(x=492, y=315)
        button28.config(bg="green", activebackground="green")
        button29 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Irini", 1, ventana))
        button29.place(x=601, y=303)
        button29.config(bg="green", activebackground="green")
        button30 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Neratziotissa", 1, ventana))
        button30.place(x=642, y=297)
        button30.config(bg="gold", activebackground="gold")
        button31 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Maroussi", 1, ventana))
        button31.place(x=700, y=244)
        button31.config(bg="green", activebackground="green")
        button32 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("KAT", 1, ventana))
        button32.place(x=748, y=194)
        button32.config(bg="green", activebackground="green")
        button33 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Kifissia", 1, ventana))
        button33.place(x=797, y=145)
        button33.config(bg="green", activebackground="green")

        # botones linea 2
        button = Button(ventana, borderwidth=0, image=buttonImage,
                        command=lambda: self.put("Agios Antonios", 2, ventana))
        button.place(x=164, y=453)
        button.config(bg="red", activebackground="red")
        button2 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Omonia", 2, ventana))
        button2.place(x=314, y=671)
        button2.config(bg="green", activebackground="green")
        button3 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Sepolia", 2, ventana))
        button3.place(x=213, y=502)
        button3.config(bg="red", activebackground="red")
        button5 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Attiki", 2, ventana))
        button5.place(x=260, y=550)
        button5.config(bg="green", activebackground="green")
        button6 = Button(ventana, borderwidth=0, image=buttonImage,
                         command=lambda: self.put("Larissa Station", 2, ventana))
        button6.place(x=260, y=601)
        button6.config(bg="red", activebackground="red")
        button7 = Button(ventana, borderwidth=0, image=buttonImage,
                         command=lambda: self.put("Metaxourghio", 2, ventana))
        button7.place(x=260, y=643)
        button7.config(bg="red", activebackground="red")
        button8 = Button(ventana, borderwidth=0, image=buttonImage,
                         command=lambda: self.put("Panepistimio", 2, ventana))
        button8.place(x=344, y=696)
        button8.config(bg="red", activebackground="red")
        button9 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Syntagma", 2, ventana))
        button9.place(x=371, y=723)
        button9.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button10 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Akropoli", 2, ventana))
        button10.place(x=375, y=782)
        button10.config(bg="red", activebackground="red")
        button11 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Sygrou - Fix", 2, ventana))
        button11.place(x=375, y=827)
        button11.config(bg="red", activebackground="red")
        button12 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Neos Kosmos", 2, ventana))
        button12.place(x=375, y=872)
        button12.config(bg="red", activebackground="red")
        button13 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Agios Ioannis", 2, ventana))
        button13.place(x=375, y=916)
        button13.config(bg="red", activebackground="red")
        button14 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Dafni", 2, ventana))
        button14.place(x=375, y=960)
        button14.config(bg="red", activebackground="red")
        button15 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Agios Dimitrios", 2, ventana))
        button15.place(x=375, y=1004)
        button15.config(bg="red", activebackground="red")

        # botones linea 3
        button50 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Egaleo", 3, ventana))
        button50.place(x=75, y=596)
        button50.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button51 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Eleonas", 3, ventana))
        button51.place(x=138, y=660)
        button51.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button52 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Kerameikos", 3, ventana))
        button52.place(x=187, y=708)
        button52.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button53 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Evangelismos", 3, ventana))
        button53.place(x=469, y=723)
        button53.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button54 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Megaro Moussikis", 3, ventana))
        button54.place(x=550, y=707)
        button54.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button55 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Ambelokipi", 3, ventana))
        button55.place(x=576, y=680)
        button55.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button56 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Panormou", 3, ventana))
        button56.place(x=602, y=654)
        button56.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button57 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Katehaki", 3, ventana))
        button57.place(x=628, y=626)
        button57.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button58 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Ethniki Amyna", 3, ventana))
        button58.place(x=654, y=600)
        button58.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button59 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Holargos", 3, ventana))
        button59.place(x=681, y=574)
        button59.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button60 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Nomismatokopio", 3, ventana))
        button60.place(x=708, y=547)
        button60.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button61 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Aghia Paraskevi", 3, ventana))
        button61.place(x=733, y=520)
        button61.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button62 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Halandri", 3, ventana))
        button62.place(x=760, y=493)
        button62.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button63 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Doukissis Plakentias", 3, ventana))
        button63.place(x=804, y=452)
        button63.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button64 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Pallini", 3, ventana))
        button64.place(x=877, y=482)
        button64.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button65 = Button(ventana, borderwidth=0, image=buttonImage,
                          command=lambda: self.put("Palania - Kantza", 3, ventana))
        button65.place(x=877, y=552)
        button65.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button66 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Koropi", 3, ventana))
        button66.place(x=877, y=710)
        button66.config(bg="RoyalBlue1", activebackground="RoyalBlue1")
        button67 = Button(ventana, borderwidth=0, image=buttonImage, command=lambda: self.put("Airport", 3, ventana))
        button67.place(x=968, y=748)
        button67.config(bg="RoyalBlue1", activebackground="RoyalBlue1")


  
        ventana.mainloop()         
       
    def frame1(self,ventana):
        
        self.inicial = None
       
        #Titulo
        ventana.title("Atenas")
        #icono
        ventana.iconbitmap("img/attiko.ico")
        #bg
        ventana.configure(bg = "white")
        #Tamaño
        ventana.geometry("1065x1167")
        #La ventana no es escalable
        ventana.resizable(0,0)
        #bg image
        bgImage = PhotoImage(file = r"img/Atenas.png")
        Label(ventana, image = bgImage).place(relwidth = 1, relheight = 1)
        #image button
        buttonImage =  PhotoImage(file = r"img/RoundButton.png")
        
        label = Label(ventana, text="Estación origen:", bg="white",fg="red",font=('Helvetica', 18, "bold"))
        label.place(x=350,y=60)
        #label = Label(ventana, text="Estación destino:", bg="white",font=('Helvetica', 18, "bold"))
        #label.place(x=350,y=100)
        
        self.msg(ventana)
        
        exitImage =  PhotoImage(file = r"img/X.png")
        exitbutton = Button(ventana, borderwidth = 0, image = exitImage, command = lambda: ventana.destroy())
        exitbutton.place(x=950, y=50)
        
              #botones linea 1
        button4 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Victoria",1,ventana))
        button4.place(x=314, y=626)
        button4.config(bg="green",activebackground="green")
        button34 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Monastiraki",1,ventana))
        button34.place(x=315, y=723)
        button34.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button35 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Thissio",1,ventana))
        button35.place(x=314, y=779)
        button35.config(bg="green",activebackground="green")
        button36 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Petralona",1,ventana))
        button36.place(x=300, y=815)
        button36.config(bg="green",activebackground="green")
        button16 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Tavros",1,ventana))
        button16.place(x=265, y=850)
        button16.config(bg="green",activebackground="green")
        button17 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Kallithea",1,ventana))
        button17.place(x=232, y=884)
        button17.config(bg="green",activebackground="green")
        button18 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Moschato",1,ventana))
        button18.place(x=199, y=917)
        button18.config(bg="green",activebackground="green")
        button19 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Faliro",1,ventana))
        button19.place(x=161, y=951)
        button19.config(bg="green",activebackground="green")
        button20 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Piraeus",1,ventana))
        button20.place(x=28, y=967)
        button20.config(bg="green",activebackground="green")
        button21 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Agios Nikolaos",1,ventana))
        button21.place(x=286, y=524)
        button21.config(bg="green",activebackground="green")
        button22 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Kato Patissia",1,ventana))
        button22.place(x=318, y=492)
        button22.config(bg="green",activebackground="green")
        button23 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Agios Eleftherios",1,ventana))
        button23.place(x=350, y=458)
        button23.config(bg="green",activebackground="green")
        button24 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Ano Patissia",1,ventana))
        button24.place(x=380, y=429)
        button24.config(bg="green",activebackground="green")
        button25 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Perissos",1,ventana))
        button25.place(x=408, y=400)
        button25.config(bg="green",activebackground="green")
        button26 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Pefkakia",1,ventana))
        button26.place(x=437, y=370)
        button26.config(bg="green",activebackground="green")
        button27 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Nea Ionia",1,ventana))
        button27.place(x=464, y=344)
        button27.config(bg="green",activebackground="green")
        button28 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Iraklio",1,ventana))
        button28.place(x=492, y=315)
        button28.config(bg="green",activebackground="green")
        button29 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Irini",1,ventana))
        button29.place(x=601, y=303)
        button29.config(bg="green",activebackground="green")
        button30 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Neratziotissa",1,ventana))
        button30.place(x=642, y=297)
        button30.config(bg="gold",activebackground="gold")
        button31 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Maroussi",1,ventana))
        button31.place(x=700, y=244)
        button31.config(bg="green",activebackground="green")
        button32 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("KAT",1,ventana))
        button32.place(x=748, y=194)
        button32.config(bg="green",activebackground="green")
        button33 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Kifissia",1,ventana))
        button33.place(x=797, y=145)
        button33.config(bg="green",activebackground="green")
        
        
        #botones linea 2
        button = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Agios Antonios",2,ventana))
        button.place(x=164, y=453)
        button.config(bg="red",activebackground="red")
        button2 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Omonia",2,ventana))
        button2.place(x=314, y=671)
        button2.config(bg="green",activebackground="green")
        button3 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Sepolia",2,ventana))
        button3.place(x=213, y=502)
        button3.config(bg="red",activebackground="red")
        button5 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Attiki",2,ventana))
        button5.place(x=260, y=550)
        button5.config(bg="green",activebackground="green")
        button6 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Larissa Station",2,ventana))
        button6.place(x=260, y=601)
        button6.config(bg="red",activebackground="red")
        button7 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Metaxourghio",2,ventana))
        button7.place(x=260, y=643)
        button7.config(bg="red",activebackground="red")
        button8 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Panepistimio",2,ventana))
        button8.place(x=344, y=696)
        button8.config(bg="red",activebackground="red")
        button9 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Syntagma",2,ventana))
        button9.place(x=371, y=723)
        button9.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button10 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Akropoli",2,ventana))
        button10.place(x=375, y=782)
        button10.config(bg="red",activebackground="red")
        button11 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Sygrou - Fix",2,ventana))
        button11.place(x=375, y=827)
        button11.config(bg="red",activebackground="red")
        button12 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Neos Kosmos",2,ventana))
        button12.place(x=375, y=872)
        button12.config(bg="red",activebackground="red")
        button13 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Agios Ioannis",2,ventana))
        button13.place(x=375, y=916)
        button13.config(bg="red",activebackground="red")
        button14 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Dafni",2,ventana))
        button14.place(x=375, y=960)
        button14.config(bg="red",activebackground="red")
        button15 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Agios Dimitrios",2,ventana))
        button15.place(x=375, y=1004)
        button15.config(bg="red",activebackground="red")
        
        
        #botones linea 3
        button50 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Egaleo",3,ventana))
        button50.place(x=75, y=596)
        button50.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button51 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Eleonas",3,ventana))
        button51.place(x=138, y=660)
        button51.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button52 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Kerameikos",3,ventana))
        button52.place(x=187, y=708)
        button52.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button53 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Evangelismos",3,ventana))
        button53.place(x=469, y=723)
        button53.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button54 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Megaro Moussikis",3,ventana))
        button54.place(x=550, y=707)
        button54.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button55 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Ambelokipi",3,ventana))
        button55.place(x=576, y=680)
        button55.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button56 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Panormou",3,ventana))
        button56.place(x=602, y=654)        
        button56.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button57 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Katehaki",3,ventana))
        button57.place(x=628, y=626)        
        button57.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button58 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Ethniki Amyna",3,ventana))
        button58.place(x=654, y=600)
        button58.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button59 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Holargos",3,ventana))
        button59.place(x=681, y=574)
        button59.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button60 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Nomismatokopio",3,ventana))
        button60.place(x=708, y=547)
        button60.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button61 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Aghia Paraskevi",3,ventana))
        button61.place(x=733, y=520)
        button61.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button62 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Halandri",3,ventana))
        button62.place(x=760, y=493)
        button62.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button63 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Doukissis Plakentias",3,ventana))
        button63.place(x=804, y=452)  
        button63.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button64 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Pallini",3,ventana))
        button64.place(x=877, y=482) 
        button64.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button65 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Palania - Kantza",3,ventana))
        button65.place(x=877, y=552) 
        button65.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button66 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Koropi",3,ventana))
        button66.place(x=877, y=710) 
        button66.config(bg="RoyalBlue1",activebackground="RoyalBlue1")
        button67 = Button(ventana, borderwidth = 0, image = buttonImage, command = lambda: self.put("Airport",3,ventana))
        button67.place(x=968, y=748) 
        button67.config(bg="RoyalBlue1",activebackground="RoyalBlue1")




        
        ventana.mainloop()
        
    def frame0(self,ventana):
        
        self.inicial = None
        self.final= None
        
        ws = ventana.winfo_screenwidth() # width of the screen
        hs = ventana.winfo_screenheight() # height of the screen
        
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (1065/2)
        y = (hs/2) - (1167/2)

        
        #Titulo
        ventana.title("Atenas")
        #icono
        ventana.iconbitmap("img/attiko.ico")
        #Tamaño
        ventana.geometry('%dx%d+%d+%d' % (1065, 1167, x, y))
        #background
        bgImage = PhotoImage(file = r"img/fondo.png")
        Label(ventana, image = bgImage).place(relwidth = 1, relheight = 1)
        #La ventana no es escalable
        ventana.resizable(0,0)
        
        exitImage =  PhotoImage(file = r"img/X.png")
        exitbutton = Button(ventana, borderwidth = 0, image = exitImage, command = lambda: ventana.destroy())
        exitbutton.place(x=950, y=50)


        button = Button(ventana, text="¡Iniciar viaje!",bg='brown', fg='white', font=('Helvetica', 18, "bold"), command=lambda: self.frame1(ventana))
        button.place(x=460, y=530)

        ventana.mainloop()
    def msg(self,ventana):
        
        ventana_extra=Toplevel(ventana)
                
        ws = ventana_extra.winfo_screenwidth() # width of the screen
        hs = ventana_extra.winfo_screenheight() # height of the screen
        
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (300/2)
        y = (hs/2) - (130/2)
        
        #Titulo
        ventana_extra.title("Atenas")
        #icono
        ventana_extra.iconbitmap("img/attiko.ico")
        #Tamaño
        ventana_extra.geometry('%dx%d+%d+%d' % (300, 130, x, y))
        ventana_extra.resizable(0,0)
      
        ventana_extra.lift
        Label(ventana_extra, text="Elija estación origen", fg='black', font=('Helvetica', 14)).place(x=70,y=30)
        button = Button(ventana_extra, text="Aceptar",bg='brown', fg='white', font=('Helvetica', 10, "bold"), command= lambda: ventana_extra.destroy())
        button.place(x=125, y=90)


UI()
