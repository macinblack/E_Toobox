from heapq import merge
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter
import time
import csv

''' Dependências necessárias
pip install -U pip
pip install -U matplotlib
'''

#Class change background
##################################################################
Images= "background.png"

class Example(Frame):

    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open(Images)
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

    def change_image(self, file):
        """Change background image of the window."""
        size = (self.winfo_width(), self.winfo_height())
        self.image = Image.open(file).resize(size)
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

##################################################################

#Login (User and Pass)
##################################################################
username = ("1")
password = ("1") 
usernameguess1 = ("")
passwordguess1 = ("")

def loginpage():
    #Gui Formatting
    root = tkinter.Toplevel()
    #root.resizable(width=FALSE, height=FALSE)
    root.title("Login")
    root.geometry("300x150")
    
    
    #Username and password boxes
    usernametext = tkinter.Label(root, text="Username:")
    usernameguess = tkinter.Entry(root)
    passwordtext = tkinter.Label(root, text="Password:")
    passwordguess = tkinter.Entry(root, show="*")

    #while usernameguess.get() != username and passwordguess.get() != password:

    def trylogin():
        global k,n
        k=0
        print ("Trying to login...")

        if usernameguess.get() == username and passwordguess.get() == password:
            messagebox.showinfo("Success ", "Successfully logged in.")
            n=1
            root.destroy()
                
        else:
            messagebox.showinfo("Error", "Sorry, but your username or password is incorrect. Try again")
            usernameguess.delete(0,END) 
            passwordguess.delete(0,END) 
            root.destroy()
            loginpage()

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            janela.destroy()

    attemptlogin = tkinter.Button(root, text="Login", command=trylogin)
    
    usernametext.pack()
    usernameguess.pack()
    passwordtext.pack()
    passwordguess.pack()
    attemptlogin.pack()
    root.protocol("WM_DELETE_WINDOW", on_closing)
##################################################################


#Configure Tkinter Window
##################################################################
janela=Tk()
janela.geometry('900x500')
janela.configure(bg='#262626')
janela.resizable(False,False)
janela.title('Electronic Tools V0.1') #title
janela.iconbitmap('power.ico') #photo 48x48px


##################################################################

e=Example(janela)
e.pack(fill=BOTH,expand=YES)

l3=Label(janela,text='Electronic Tools',fg='white',bg='#262626')
l3.config(font=('Comic Sans MS',50))
l3.place(x=200, y=170)



global k


def kill_objects():#kill objects 
    print("destroy: ", k)
    print(k)
    if k==1: #kill objects capacitor
        print("destroy cap objects")
        evolt.destroy()
        ecomponent.destroy()
        eresistor.destroy()
        lvolt.destroy()
        lcomponent.destroy()
        lresistor.destroy()
        bplot_charge.destroy()
        bplot_discharge.destroy()
        bclean.destroy()

    elif  k==2:#kill objects inductor
        print("destroy ind objects")
        evolt.destroy()
        ecomponent.destroy()
        eresistor.destroy()
        lvolt.destroy()
        lcomponent.destroy()
        lresistor.destroy()
        bplot_charge.destroy()
        bplot_discharge.destroy()
        bclean.destroy()

    elif k==3:#kill objects ohm
        print("destroy ohm objects")
        evolt.destroy()
        eampere.destroy()
        eresistor.destroy()
        epower.destroy()
        lvolt.destroy()
        lampere.destroy()
        lresistor.destroy()
        lpower.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        bcalc.destroy()
        bclean.destroy()

    elif k==4:#kill objects e-listbox
        print("destroy list objects")
        ldescription.destroy()
        edescription.destroy()
        lprice.destroy()
        eprice.destroy()
        lman.destroy()
        eman.destroy()
        lmpn.destroy()
        empn.destroy()
        bfadd.destroy()
        bfdelete.destroy()
        bClean.destroy()
        bExport.destroy()
        bupdate.destroy()
        listbox1.destroy()
        deslabel.destroy()
        pricelabel.destroy()
        manlabel.destroy()
        mpnlabel.destroy()
        deslabel2.destroy()
        pricelabel2.destroy()
        manlabel2.destroy()
        mpnlabel2.destroy()

        
def capacitor():
    global lvolt,evolt,lresistor, eresistor,lcomponent,ecomponent, bplot_charge, bplot_discharge,bclean, k
    f1.destroy()
    l3.destroy()
    e.change_image('bg_capacitor.png') #change background

    kill_objects()
    k=1
    # Data for plotting
    def plot_c(): #print capacitor charge plot

        V = float(evolt.get())
        print(V)
        R = float(eresistor.get())
        print(R)
        C = float(ecomponent.get())*1e-6
        print(C)
        
        tau=R*C
        tau_linha=int(5*tau)+tau
        t=np.linspace(0, tau_linha, 1000)
        dt=0.01

        VT = V*(1 - np.exp(-t/(tau)))   
        print(VT)

        fig, ax = plt.subplots()
        ax.plot(t, VT)

        ax.set(xlabel='time (s)', ylabel='voltage (V)', title='Capacitor Charging')
        ax.grid()
        fig.savefig("capacitor_c_plot.png")
        plt.show()
   
    def plot_d(): #print capacitor discharge plot

        V = float(evolt.get())
        print(V)
        R = float(eresistor.get())
        print(R)
        C = float(ecomponent.get())*1e-6
        print(C)
        
        tau=R*C
        tau_linha=int(5*tau)+tau
        t=np.linspace(0, tau_linha, 1000)
        dt=0.01

        VT = V* np.exp(-t/(tau))  
        print(VT)

        fig, ax = plt.subplots()
        ax.plot(t, VT)

        ax.set(xlabel='time (s)', ylabel='voltage (V)', title='Capacitor Discharging')
        ax.grid()
        fig.savefig("capacitor_d_plot.png")
        plt.show()

    def clean(): #delete all 
        evolt.delete(0,END) 
        eresistor.delete(0,END)
        ecomponent.delete(0,END)
        

    lvolt = Label(janela, text = "Volt (V): ")
    evolt = Entry(janela, width=10)
    lresistor= Label(janela, text = "Resistor (Ω): ")
    eresistor= Entry(janela, width=10)
    lcomponent = Label(janela, text = "Capacitor (uF): ")
    ecomponent = Entry(janela, width=10)
    lvolt.place(x=430, y=300)
    evolt.place(x=430, y=320)
    lresistor.place(x=430, y=340)
    eresistor.place(x=430, y=360)
    lcomponent.place(x=430, y=380)
    ecomponent.place(x=430, y=400)

    bplot_charge = Button(janela,text="Plot Charge",command=plot_c,bd=5,width=10)
    bplot_discharge =Button(janela,text="Plot Discharge",command=plot_d,bd=5,width=10)
    bclean =Button(janela,text="Clean all", command=clean, bd=5,width=10)
    bplot_charge.place(x=230, y=390)
    bplot_discharge.place(x=585, y=390)
    bclean.place(x=420, y=450)

    #toggle_menu()

def inductor():
    global lvolt,evolt,lresistor,eresistor,lcomponent,ecomponent,k, bplot_charge, bplot_discharge, bclean
    
    f1.destroy()
    l3.destroy()
    e.change_image('bg_inductor.png') #change background

    kill_objects()
    k=2
    print(k)
    
    def plot_c(): #print inductor magnet plot

        V = float(evolt.get())
        print(V)
        R = float(eresistor.get())
        print(R)
        C = float(ecomponent.get())*1e-6
        print(C)
        
        tau=R/C
        tau_linha=int(5*tau)+tau
        t=np.linspace(0, tau_linha, 1000)
        dt=0.01

        IT = (V/R)* (1-np.exp(-t/(tau)))
        
        fig, ax = plt.subplots()
        ax.plot(t, IT)

        ax.set(xlabel='time (s)', ylabel='Current (A)', title='Inductor Charging')
        ax.grid()
        fig.savefig("inductor_c_plot.png")
        plt.show()
   
    def plot_d(): #print inductor desmagnet plot

        V = float(evolt.get())
        print(V)
        R = float(eresistor.get())
        print(R)
        C = float(ecomponent.get())*1e-3
        print(C)
        
        tau=R/C
        tau_linha=int(5*tau)+tau
        t=np.linspace(0, tau_linha, 1000)
        dt=0.01

        IT = (V/R)* np.exp(-t/(tau))
        

        fig, ax = plt.subplots()
        ax.plot(t, IT)

        ax.set(xlabel='time (s)', ylabel='Current (A)', title='Inductor Discharging')
        ax.grid()
        fig.savefig("inductor_d_plot.png")
        plt.show()

    def clean(): #delete all 
        evolt.delete(0,END) 
        eresistor.delete(0,END)
        ecomponent.delete(0,END)

    lvolt = Label(janela, text = "Volt (V): ")
    evolt = Entry(janela, width=10)
    lresistor= Label(janela, text = "Resistor (Ω): ")
    eresistor= Entry(janela, width=10)
    lcomponent = Label(janela, text = "Inductor (mH): ")
    ecomponent=Entry(janela, width=10)
    lvolt.place(x=420, y=300)
    evolt.place(x=420, y=320)
    lresistor.place(x=420, y=340)
    eresistor.place(x=420, y=360)
    lcomponent.place(x=420, y=380)
    ecomponent.place(x=420, y=400)

    bplot_charge = Button(janela,text="Plot Charge",command=plot_c,bd=5,width=10)
    bplot_discharge =Button(janela,text="Plot Discharge",command=plot_d,bd=5,width=10)
    bclean =Button(janela,text="Clean all",bd=5,width=10)
    bplot_charge.place(x=230, y=390)
    bplot_discharge.place(x=585, y=390)
    bclean.place(x=420, y=450)

    #toggle_menu()

def ohm():
    global evolt,eampere,eresistor,epower,lvolt,lampere,lresistor,lpower, r1,r2,r3,r4,bcalc,bclean,k
    
    f1.destroy()
    l3.destroy()
    e.change_image('bg_ohm.png') #change background

    kill_objects()
    k=3

    #global evolt_r,eampere_r,eresistor_r,epower_r

    

    def calc():

        if valor.get() == 1: #volt
            # v = Squareroot(p*r)
            if int(epower.get())>0 and int(eresistor.get())>0:
                evolt_r = math.sqrt(epower*eresistor)
                messagebox.showinfo("Volt: " + evolt_r + " V")
            # v = p / i
            elif int(epower.get())>0 and int(eampere.get())>0:
                evolt_r = epower/eampere
                messagebox.showinfo("Volt: " + evolt_r + " V")
            # v = i * r
            elif int(eampere.get())>0 and int(eresistor.get())>0:
                evolt_r = eampere*eresistor
                messagebox.showinfo("Volt: " + evolt_r + " V")
            #else:
                #return ""
            

        elif valor.get() == 2: #current
            # i = v / r
            if int(evolt.get())>0 and int(eresistor.get())>0:
                eampere_r =evolt/eresistor
            # i = p / v
            elif int(epower.get())>0 and int(evolt.get())>0:
                eampere_r =epower/evolt
            # i = Squareroot (p / r)
            elif int(epower.get())>0 and int(eresistor.get())>0:
                eampere_r =math.sqrt(epower/eresistor)
            #else:
                #return ""

    
        elif valor.get() == 3: #power
            # p = v * i
            if evolt>0 and eampere>0:
                epower_r =evolt*eampere
            # p = i² * r
            elif eampere>0 and eresistor>0:
                epower_r =math.pow(eampere, 2)*eresistor
            # p = v²/r
            elif evolt>0 and eresistor>0:
                epower_r =math.pow(evolt, 2)/eresistor
            #else:
                #return ""

   
        elif valor.get() == 4: #resistor
            # r = v / i
            if evolt>0 and eampere>0:
                eresistor_r =evolt/eampere
           
            # r = v² / p
            elif evolt>0 and epower>0:
                eresistor_r = math.pow(evolt, 2)/epower
        
            # r = p / i²
            elif epower>0 and eampere>0:
                eresistor_r = epower/math.pow(eampere, 2)
            #else:
                #return ""

    evolt_r = 0.0
    eampere_r = 0.0
    eresistor_r = 0.0
    epower_r = 0.0

    def clean():
        evolt.delete(0,END) 
        eresistor.delete(0,END)
        epower.delete(0,END)
        eampere.delete(0,END)

    evolt = Entry(janela, textvariable=evolt_r, width=10)
    eampere = Entry(janela, textvariable=eampere_r, width=10)
    eresistor= Entry(janela,textvariable=eresistor_r, width=10)
    epower = Entry(janela,textvariable=epower_r, width=10)
    lvolt= Label(janela, width=9, text="V", textvariable=evolt)
    lampere= Label(janela, width=9, text="A", textvariable=eampere)
    lresistor= Label(janela, width=9, text="Ω", textvariable=eresistor)
    lpower= Label(janela, width=9, text="P", textvariable=epower)



    lvolt.place(x=570,y=115)
    lampere.place(x=245, y=425)
    lresistor.place(x=570, y=425)
    lpower.place(x=245,y=115)
    
    evolt.place(x=570, y=95)
    eampere.place(x=245, y=405)
    eresistor.place(x=570, y=405)
    epower.place(x=245, y=95)

    valor = IntVar()
    r1 = Radiobutton(janela, text="Volt",
                     value = 1, variable=valor)

    r2 = Radiobutton(janela, text="Current",
                     value = 2, variable=valor)

    r3 = Radiobutton(janela, text="Resistor",
                     value = 3, variable=valor)

    r4 = Radiobutton(janela, text="Power",
                     value = 4, variable=valor)

    r1.place(x=585, y=70)
    r2.place(x=245, y=380)
    r3.place(x=570, y=380)
    r4.place(x=245, y=70)

    bcalc =Button(janela,text="Calc",command=calc,bd=5,width=10)
    bclean =Button(janela,text="Clean all", command=clean, bd=5,width=10)
    bcalc.place(x=340, y=450)
    bclean.place(x=430, y=450)
    
    #toggle_menu()

'''
def rlc():
    f1.destroy()
    l3.destroy()
    e.change_image('bg_rlc.png') #change background
    
   
    
    def plot_c(): # RLC Parallel

        V = float(evolt.get())
        print(V)
        R = float(eresistor.get())
        print(R)
        C = float(einductor.get())*1e-6
        print(C)
        
        tau=R*C
        tau_linha=int(6*tau)+1
        t=np.linspace(0, tau_linha, 1000)
        dt=0.01

        IT = (V/R)* (1-np.exp(-t/(tau)))
        
        fig, ax = plt.subplots()
        ax.plot(t, IT)

        ax.set(xlabel='time (s)', ylabel='Current (A)', title='Parallel')
        ax.grid()
        fig.savefig("rlc_plot_parallel.png")
        plt.show()
   
    def plot_d(): # RLC Series

        V = float(evolt.get())
        print(V)
        R = float(eresistor.get())
        print(R)
        C = float(einductor.get())*1e-3
        print(C)
        
        tau=R*C
        tau_linha=int(6*tau)+1
        t=np.linspace(0, tau_linha, 1000)
        dt=0.01

        IT = (V/R)* np.exp(-t/(tau))
        

        fig, ax = plt.subplots()
        ax.plot(t, IT)

        ax.set(xlabel='time (s)', ylabel='voltage (V)', title='Series')
        ax.grid()
        fig.savefig("rlc_plot_series.png")
        plt.show()

    def clean():
        evolt.delete(0,END) 
        eresistor.delete(0,END)
        einductor.delete(0,END)

    lvolt = Label(janela, text = "Volt (V): ")
    evolt = Entry(janela, width=10)
    lresistor= Label(janela, text = "Resistor (Ohm): ")
    eresistor= Entry(janela, width=10)
    linductor = Label(janela, text = "Inductor (mH): ")
    einductor = Entry(janela, width=10)
    lvolt.place(x=420, y=300)
    evolt.place(x=420, y=320)
    lresistor.place(x=420, y=340)
    eresistor.place(x=420, y=360)
    linductor.place(x=420, y=380)
    einductor.place(x=420, y=400)

    bplot_charge = Button(janela,text="Parallel",command=plot_c,bd=5,width=10)
    bplot_discharge =Button(janela,text="Series",command=plot_d,bd=5,width=10)
    bclean =Button(janela,text="Clean all",bd=5,width=10)
    bplot_charge.place(x=230, y=390)
    bplot_discharge.place(x=585, y=390)
    bclean.place(x=420, y=450)
    toggle_menu()
'''
def List_CSV():
    global ldescription, edescription, lprice,eprice,lman,eman,lmpn,empn,bfadd,bfdelete,bClean,bExport,bupdate,listbox1,k
    global deslabel,deslabel2,pricelabel,manlabel,mpnlabel,pricelabel2,manlabel2,mpnlabel2
    f1.destroy()
    l3.destroy()
    e.change_image('background.png') #change background
    
    kill_objects()
    k=4    

    File = open('etoolbox.csv')
    Reader = csv.reader(File) #import all from csv file
    Data = list(Reader)
    print(Data)
    del(Data[0])

    list_of_entries = []
    for x in list(range(0,len(Data))): #list for listbox
        list_of_entries.append(Data[x][0]) #add to listbox on last position of x

    var = StringVar(value = list_of_entries)
    listbox1 = Listbox(janela, listvariable = var)
    listbox1.place(x=100,y=100)
    
    def clean(): #delete all positions
        edescription.delete(0,END) 
        eprice.delete(0,END) 
        eman.delete(0,END) 
        empn.delete(0,END) 
        
    def update(): #update all positions imported from CSV File
        index = listbox1.curselection()[0]
        deslabel2.config(text = Data[index][0])
        pricelabel2.config(text = Data[index][1])
        manlabel2.config(text = Data[index][2])
        mpnlabel2.config(text = Data[index][3])

        return None

    def add(): #Add to last position from listbox and Data
        x=len(Data)
        listbox1.insert(x,edescription.get())
        print(Data)
        Data_t=['','','','']

        Data_t[0]=edescription.get()
        Data_t[1]=eprice.get()
        Data_t[2]=eman.get()
        Data_t[3]=empn.get()
        Data.append(Data_t)
        print(Data)
        x=x+1
        messagebox.showinfo("Information","The data has been added successfully")

    def delete(): #delete last position from listbox and Data
        x=len(Data)-1
        listbox1.delete(x)
        Data.pop()
        print(Data)
        x=x-1
        messagebox.showinfo("Information","The data has been deleted successfully")

    def export_csv(): #export to CSV file
        
        with open("etoolbox.csv","w", encoding='UTF8', newline='') as file:
            Writer= csv.writer(file)
            Writer.writerow(["Description","Price","Manufacturer","MPN"])
            Writer.writerows(Data)
            messagebox.showinfo("Information","Saved succesfully")
        
    
    ldescription = Label(janela, text = "Insert description: ")
    edescription = Entry(janela, width=25)
    lprice = Label(janela, text = "Insert Price: ")
    eprice = Entry(janela, width=25)
    lman = Label(janela, text = "Insert Manufacturer: ")
    eman = Entry(janela, width=25)
    lmpn = Label(janela, text = "Insert MPN: ")
    empn = Entry(janela, width=25)
    bfadd = Button(janela,text="Add",command=add,bd=5,width=10)
    bfdelete = Button(janela,text="Delete",command=delete,bd=5,width=10)
    bClean =Button(janela,text="Clean All",command=clean,bd=5,width=10)
    bExport =Button(janela,text="Export CSV",command=export_csv,bd=5,width=10)
    bupdate = Button(janela, text="Update Data", command=update)

    
    ldescription.place(x=350, y=105)
    edescription.place(x=500, y=105)
    lprice.place(x=350, y=125)
    eprice.place(x=500, y=125)
    lman.place(x=350, y=145)
    eman.place(x=500, y=145)
    lmpn.place(x=350, y=165)
    empn.place(x=500, y=165)

    bfadd.place(x=350, y=200)
    bfdelete.place(x=350, y=240)
    bClean.place(x=500, y=200)
    bExport.place(x=650, y=200)
    bupdate.place(x=125, y=268)

    deslabel = Label(janela, text="Description:")
    deslabel.place(x=100,y=300)
    pricelabel = Label(janela, text="Price:")
    pricelabel.place(x=100,y=320)
    manlabel = Label(janela, text="Manufacturer:")
    manlabel.place(x=100,y=340)
    mpnlabel = Label(janela, text="MPN:")
    mpnlabel.place(x=100,y=360)

    deslabel2 = Label(janela, text="")
    deslabel2.place(x=200,y=300)
    pricelabel2 = Label(janela, text="")
    pricelabel2.place(x=200,y=320)
    manlabel2 = Label(janela, text="")
    manlabel2.place(x=200,y=340)
    mpnlabel2 = Label(janela, text="")
    mpnlabel2.place(x=200,y=360)

    #toggle_menu()

def toggle_menu():
    if n == 1:
        global f1
        f1=Frame(janela,width=300,height=500,bg='#12c4c0')
        f1.place(x=0,y=0)
    
        #botões
        def bttn(x,y,text,bcolor,fcolor,cmd):
     
            def on_entera(e):
                myButton1['background'] = bcolor #ffcc66
                myButton1['foreground']= '#262626'  #000d33

            def on_leavea(e):
                myButton1['background'] = fcolor
                myButton1['foreground']= '#262626'

            myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)

        bttn(0,80,'C A P A C I T O R','#0f9d9a','#12c4c0',capacitor)
        bttn(0,117,'I N D U C T O R','#0f9d9a','#12c4c0',inductor)
        bttn(0,154,'O H M  L A W','#0f9d9a','#12c4c0',ohm)
        #bttn(0,191,'R L C  C I R C U I T','#0f9d9a','#12c4c0',rlc)
        bttn(0,191,' E - L I S T B O X','#0f9d9a','#12c4c0',List_CSV)


        def close():
            f1.destroy()

        global img2
        img2 = ImageTk.PhotoImage(Image.open("close.png"))

        Button(f1,image=img2,border=0,command=close,bg='#12c4c0',activebackground='#12c4c0').place(x=5,y=10)

img1 = ImageTk.PhotoImage(Image.open("open.png"))

Button(janela,image=img1,
       command=toggle_menu,
       border=0,
       bg='#262626',
       activebackground='#262626').place(x=5,y=10)

loginpage()

janela.mainloop()
