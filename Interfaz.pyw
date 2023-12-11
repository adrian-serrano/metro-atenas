from tkinter import *
from tkinter import Tk, Label, PhotoImage, Button, Entry, StringVar, Listbox, Canvas
import AlgoritmoEstrella as AE

class MetroApp:
    def __init__(self, master):

        self.master = master
        self.master.title("Metro Atenas")
        self.master.iconbitmap("img/attiko.ico")

        # Add image file
        self.bg = PhotoImage(file="img/bg2.png")
        self.logo = PhotoImage(file="img/attiko.png")

        # Set window size to match the image
        self.master.geometry(f"{self.bg.width()}x{self.bg.height()}")

        # Disable window resizing
        self.master.resizable(False, False)

        # Show image bg using label
        self.label1 = Label(self.master, image=self.bg)
        self.label1.place(x=0, y=0)

        self.create_canvas1()

        # Back button in the map
        self.back_button = Button(self.master, text="← Volver al menú",bg='brown', fg='white', command=self.show_menu)
        self.back_button.pack(side="top", anchor="nw", padx=10, pady=10)

    
        # Create additional canvas for the trip details
        self.trip_canvas = Canvas(self.master, width=450, height=700, relief='raised', bg="white", highlightthickness=2)

        # Add an image for the map
        self.map_image = PhotoImage(file="img/Atenas1.png")
        # Create additional canvas for the map details
        self.map_canvas = Canvas(self.map_frame, width=self.bg.width(), height=self.bg.height())
        self.map_canvas.create_image(0, 0, anchor="nw", image=self.map_image)
        self.map_canvas.pack()


    def create_canvas1(self):

        names_line1 = ["Victoria", "Omonia", "Thissio", "Petralona", "Tavros", "Kallithea", "Moschato", "Faliro", "Piraeus","Attiki", "Agios Nikolaos", "Kato Patissia", "Agios Eleftherios", "Ano Patissia", "Perissos", "Pefkakia", "Nea Ionia", "Iraklio", "Irini", "Neratziotissa", "Maroussi", "KAT", "Kifissia"]
        names_line2 = ["Agios Antonios", "Sepolia", "Larissa Station", "Metaxourghio", "Panepistimio", "Syntagma", "Akropoli", "Sygrou - Fix", "Neos Kosmos", "Agios Ioannis", "Dafni", "Agios Dimitrios"]
        names_line3 = ["Egaleo", "Eleonas", "Kerameikos", "Monastiraki","Evangelismos", "Megaro Moussikis", "Ambelokipi", "Panormou", "Katehaki", "Ethniki Amyna", "Holargos", "Nomismatokopio", "Aghia Paraskevi", "Halandri", "Doukissis Plakentias", "Pallini", "Palania - Kantza", "Koropi", "Airport"]
      
        self.canvas1 = Canvas(self.master, width=450, height=700, relief='raised',bg="white")

        self.canvas1.place(x=195, y=50)

        # Add an image of the logo
        self.canvas1.create_image(self.canvas1.winfo_reqwidth() // 1.9, 50, anchor=N, image=self.logo, tags="front")

        # Raise the image to the front
        self.canvas1.tag_raise("front")


        self.label = Label(self.canvas1, text="Metro Atenas", font=('Helvetica', 18, "bold"),bg="white")
        self.label.place(x=160, y=270)

        self.origin_label = Label(self.canvas1, text="Origen:", font=('Helvetica', 12, "bold"),bg="white")
        self.origin_label.place(x=20, rely=0.45)

        self.destiny_label = Label(self.canvas1, text="Destino:", font=('Helvetica', 12, "bold"),bg="white")
        self.destiny_label.place(x=20, rely=0.55)
        
        # Entry
        entry_width = 22
        entry_font = ('Helvetica', 16)
        self.origin_var = StringVar()
        self.origin_entry = Entry(self.canvas1, textvariable=self.origin_var, width=entry_width, font=entry_font)
        self.origin_entry.place(x=100, rely=0.45)
        self.origin_entry.bind("<FocusIn>", self.show_search_boxes)
        self.origin_entry.bind("<FocusOut>", self.hide_search_boxes)
        self.origin_entry.bind("<KeyRelease>", self.filter_options)

        self.destiny_var = StringVar()
        self.destiny_entry = Entry(self.canvas1, textvariable=self.destiny_var, width=entry_width, font=entry_font)
        self.destiny_entry.place(x=100, rely=0.55)
        self.destiny_entry.bind("<FocusIn>", self.show_search_boxes)
        self.destiny_entry.bind("<FocusOut>", self.hide_search_boxes)
        self.destiny_entry.bind("<KeyRelease>", self.filter_options)

        # Listbox
        listbox_width = 22
        listbox_font = ('Helvetica', 16)
        self.origin_listbox = Listbox(self.canvas1, width=listbox_width, font=listbox_font)
        self.origin_listbox_options = names_line1 + names_line2 + names_line3
        self.listbox_options = {self.origin_listbox: self.origin_listbox_options}
        self.origin_listbox.place_forget()
        self.origin_listbox.bind("<ButtonRelease-1>", self.select_station)

        self.destiny_listbox = Listbox(self.canvas1, width=listbox_width, font=listbox_font)
        self.destiny_listbox_options = names_line1 + names_line2 + names_line3
        self.listbox_options[self.destiny_listbox] = self.destiny_listbox_options
        self.destiny_listbox.place_forget()
        self.destiny_listbox.bind("<ButtonRelease-1>", self.select_station)
        
        # Bottom Buttons 
        self.start_trip_button = Button(self.canvas1, text="Iniciar viaje",bg='brown', fg='white', command=self.start_trip)
        self.start_trip_button.place(relx=0.35, rely=0.8, anchor="center")

        self.map_button = Button(self.canvas1, text="Mapa",bg='brown', fg='white', command=self.show_map)
        self.map_button.place(relx=0.65, rely=0.8, anchor="center")

        self.map_frame = Frame(self.master, bg="white")

    def show_menu(self):
        # Delete map
        self.map_frame.place_forget()
        # Delete trip_canvas
        self.trip_canvas.destroy()
        # Show entrys
        self.canvas1.place(x=195, y=50)
        self.origin_entry.place(x=100, rely=0.45)
        self.destiny_entry.place(x=100, rely=0.55)

        # Bottom Buttons 
        self.start_trip_button.place(relx=0.35, rely=0.8, anchor="center")
        self.map_button.place(relx=0.65, rely=0.8, anchor="center")


    def show_map(self):
        self.map_frame.place(x=0, y=0)
        self.canvas1.place_forget()

    def show_search_boxes(self, event):
        if event.widget == self.origin_entry:
            self.origin_listbox.place(x=100, rely=0.49)
        elif event.widget == self.destiny_entry:
            self.destiny_listbox.place(x=100, rely=0.59)

        # Lift the Listbox to the top
        self.origin_listbox.lift()
        self.destiny_listbox.lift()

    def hide_search_boxes(self, event):
        self.origin_listbox.place_forget()
        self.destiny_listbox.place_forget()

    def filter_options(self, event):
        entry = event.widget
        listbox = self.origin_listbox if entry == self.origin_entry else self.destiny_listbox
        filter_text = entry.get().lower()
        self.filter_listbox(listbox, filter_text)

    def filter_listbox(self, listbox, filter_text):
        listbox.delete(0, 'end')
        for option in self.listbox_options[listbox]:
            if filter_text in option.lower():
                listbox.insert('end', option)

    def select_station(self, event):
        station = event.widget.get(event.widget.curselection()[0])
        if event.widget == self.origin_listbox:
            self.origin_var.set(station)
        elif event.widget == self.destiny_listbox:
            self.destiny_var.set(station)
            

            
            
    def start_trip(self):
        stationOG = self.origin_var.get()
        stationDY = self.destiny_var.get()
        station1 = self.origin_var.get()
        station2 = self.destiny_var.get()
        #"Omonia""Attiki""Monastiraki""Syntagma"
        if station1 in "Omonia":
            station1= "Omonia1"
        elif station1 in "Attiki":
            station1=  "Attiki1"
        elif station1 in "Monastiraki":
            station1=  "Monastiraki3"
        elif station1 in "Syntagma":
            station1=  "Syntagma2"
        else:
            station1=  station1

        if station2 in "Omonia":
            station2= "Omonia1"
        elif station2 in "Attiki":
            station2=  "Attiki1"
        elif station2 in "Monastiraki":
            station2=  "Monastiraki3"
        elif station2 in "Syntagma":
            station2=  "Syntagma2"
        else:
            station2=  station2
   
        self.estrella = AE.AlgoritmoEstrella(station1, station2)
        self.estrella.apply()
        path,transfers,time = self.estrella.convertSolution()

        # Create additional canvas for the trip details
        self.trip_canvas = Canvas(self.master, width=450, height=700, relief='raised', bg="white", highlightthickness=2)
        self.trip_canvas.place(x=195, y=50)

        self.canvas1.place_forget()
        
        #Parada de inicio
        self.origin = Label(self.trip_canvas, text="Inicio:", font=('Helvetica', 18, "bold"),bg="white")
        self.origin.place(x=10, y=10)
        self.origin = Label(self.trip_canvas, text=self.origin_var.get(), font=('Helvetica', 18, "bold"),bg="white")
        self.origin.place(x=90, y=10)
        self.line_origin = Label(self.trip_canvas, text="Línea:", font=('Helvetica', 18, "bold"),bg="white")
        self.line_origin.place(x=10, y=45)
        self.line_origin = Label(self.trip_canvas, text=self.get_line_for_station(self.origin_var.get()), font=('Helvetica', 18, "bold"),bg="white")
        self.line_origin.place(x=90, y=45)
        
        #Parada final
        self.destiny = Label(self.trip_canvas, text="Destino:", font=('Helvetica', 18, "bold"),bg="white")
        self.destiny.place(x=10, y=80)
        self.destiny = Label(self.trip_canvas, text=self.destiny_var.get(), font=('Helvetica', 18, "bold"),bg="white")
        self.destiny.place(x=110, y=80)
        self.line_destiny  = Label(self.trip_canvas, text="Línea:", font=('Helvetica', 18, "bold"),bg="white")
        self.line_destiny.place(x=10, y=115)
        self.line_destiny  = Label(self.trip_canvas, text=self.get_line_for_station(self.destiny_var.get()), font=('Helvetica', 18, "bold"),bg="white")
        self.line_destiny.place(x=90, y=115)
  
        
        #Transbordos
        self.transfers = Label(self.trip_canvas, text="Numero de transbordos:", font=('Helvetica', 18, "bold"),bg="white")
        self.transfers.place(x=10, y=150) 
        self.transfers2 = Label(self.trip_canvas, text=str(transfers), font=('Helvetica', 18, "bold"),bg="white")                             
        self.transfers2.place(x=300, y=150)
        #Tiempo
        self.time = Label(self.trip_canvas, text="Tiempo del trayecto:", font=('Helvetica', 18, "bold"),bg="white")
        self.time .place(x=10, y=185) 
        self.time2 = Label(self.trip_canvas, text=str(round(time/60))+" minutos", font=('Helvetica', 18, "bold"),bg="white")                             
        self.time2.place(x=270, y=185)
        #Ruta
        self.route  = Label(self.trip_canvas, text="Ruta:", font=('Helvetica', 18, "bold"),bg="white")
        self.route.place(x=10, y=220) 
        # Display the path on the canvas

        self.path  = Label(self.trip_canvas, text=path, font=('Helvetica', 12, "bold"),bg="white",justify=LEFT)
        self.path.place(x=20, y=270) 

        
        # # Dividir la cadena en líneas
        # path_lines = path.split('\n')

        # # Crear una lista con el formato deseado
        # formatted_path = [f"{line}" for line in path_lines]
        # print(formatted_path)
        





    def get_line_for_station(self, station):
        names_line1 = ["Victoria", "Omonia", "Monastiraki", "Thissio", "Petralona", "Tavros", "Kallithea", "Moschato", "Faliro", "Piraeus","Attiki", "Agios Nikolaos", "Kato Patissia", "Agios Eleftherios", "Ano Patissia", "Perissos", "Pefkakia", "Nea Ionia", "Iraklio", "Irini", "Neratziotissa", "Maroussi", "KAT", "Kifissia"]
        names_line2 = ["Agios Antonios", "Omonia", "Sepolia", "Attiki", "Larissa Station", "Metaxourghio", "Panepistimio", "Syntagma", "Akropoli", "Sygrou - Fix", "Neos Kosmos", "Agios Ioannis", "Dafni", "Agios Dimitrios"]
        names_line3 = ["Egaleo", "Eleonas", "Kerameikos", "Monastiraki","Syntagma","Evangelismos", "Megaro Moussikis", "Ambelokipi", "Panormou", "Katehaki", "Ethniki Amyna", "Holargos", "Nomismatokopio", "Aghia Paraskevi", "Halandri", "Doukissis Plakentias", "Pallini", "Palania - Kantza", "Koropi", "Airport"]
        if station in "Omonia":
            return "1,2"
        elif station in "Attiki":
            return "1,2"
        elif station in "Monastiraki":
            return "1,3"
        elif station in "Syntagma":
            return "2,3"
        elif station in names_line1:
            return 1
        elif station in names_line2:
            return 2
        elif station in names_line3:
            return 3
        else:
            return None  # Station doesn't belong to any line
        




if __name__ == "__main__":
    root = Tk()
    app = MetroApp(root)
    root.mainloop()
