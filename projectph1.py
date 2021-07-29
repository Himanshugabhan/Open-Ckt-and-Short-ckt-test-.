import  math
import sys
from tkinter import *
from  tkinter import  messagebox
wt=Tk()
wt.geometry("700x700")
#wt.resizable(0,0)
wt.configure(bg="Wheat")
wt.title("RCOEM")
head1=Label(wt, text = "Shri Ramdeobaba College of Engineering and Management",bg='Light Cyan', fg = "blue", font = "Castellar 18 bold italic underline")
head1.place(x=10, y=10)
head2=Label(wt, text = "Department of Electrical Engineering",bg='Sandy Brown', fg = "blue", font = "Castellar 16 underline ")
head2.place(x=160, y=45)
head3=Label(wt, text = "OC and SC Test",bg='lightgreen', fg = "blue", font = "Castellar 15")
head3.place(x=350, y=76)


#open CKT
l1=Label(wt, text = "Open Ckt Test : ",font='calibri 16 bold').place(x=50, y=110)
l2=Label(wt, text = "Enter The readings of the Voltmeter, ammeter and wattmeter",font='calibri 11 bold').place(x=100, y=150)
l3=Label(wt, text = "Readings of the Voltmeter  : ",font='calibri 11 bold').place(x=110, y=170)
voc=Entry(wt)
voc.focus()
voc.place(x=330,y=170)
l4=Label(wt, text = "Readings of the Ammeter    : ",font='calibri 11 bold').place(x=110, y=190)
ioc=Entry(wt)
ioc.place(x=330,y=190)
l5=Label(wt, text = "Readings of the Wattmeter : ",font='calibri 11 bold').place(x=110, y=210)
woc=Entry(wt)
woc.place(x=330,y=210)
#l11=Label(wt, text = "Secondary Induced Voltage : ",font='calibri 11 bold').place(x=110, y=170)
#v2oc=Entry(wt)
#v2oc.place(x=330,y=170)
sys.argv.append("OC-test.png")
#print((sys.argv))
img=PhotoImage(file=sys.argv[1])
IMG=Label(image=img)
IMG.place(x=500,y=150)

#SHORT CKT

l6=Label(wt, text = "Short Ckt Test : ",font='calibri 16 bold').place(x=50, y=250)
l7=Label(wt, text = "Enter The readings of the Voltmeter, ammeter and wattmeter",font='calibri 11 bold').place(x=100, y=290)
l8=Label(wt, text = "Readings of the Voltmeter  : ",font='calibri 11 bold').place(x=110, y=310)
vsc=Entry(wt)
vsc.place(x=330,y=310)
l9=Label(wt, text = "Readings of the Ammeter    : ",font='calibri 11 bold').place(x=110, y=330)
isc=Entry(wt)
isc.place(x=330,y=330)
l10=Label(wt, text = "Readings of the Wattmeter : ",font='calibri 11 bold').place(x=110, y=350)
wsc=Entry(wt)
wsc.place(x=330,y=350)
#l12=Label(wt, text = "Secondary current I2sc : ",font='calibri 11 bold').place(x=110, y=320)
#wsc=Entry(wt)
#wsc.place(x=330,y=320)
sys.argv.append("short-circuit-test-1.png")
print((sys.argv))
img1=PhotoImage(file=sys.argv[2])
IMG1=Label(image=img1)
IMG1.place(x=500,y=290)


def my():
    try:
        voc1 = float(voc.get())
        ioc1 = float(ioc.get())
        woc1 = float(woc.get())
        vsc1 = float(vsc.get())
        isc1 = float(isc.get())
        wsc1 = float(wsc.get())
        try :
            # oc parameters
            cosx = (woc1) / (voc1 * ioc1)
            sinx = math.sin(math.acos(cosx))
            iw = ioc1 * cosx
            im = ioc1 * sinx
            r0 = (voc1) / (ioc1 * cosx)
            x0 = (voc1) / (ioc1 * sinx)
            global l;global lcosx;global liw;global lim;global lr0;global lx0; global lr01; global lx01
            l = Label(wt, text="Calculations : ", font='calibri')
            l.place(x=50, y=440)
            lcosx = Label(wt, text="1)No Load Power Factor : " + str(round(cosx,2)), font='calibri')
            lcosx.place(x=110, y=460)
            liw = Label(wt, text="2)Iron Loss Component : " + str(round(iw,2))+" Amp", font='calibri')
            liw.place(x=110, y=480)
            lim = Label(wt, text="3)Magnetizing Component  : " + str(round(im,2))+" Amp", font='calibri')
            lim.place(x=450, y=480)
            lr0 = Label(wt, text="4)Magnetizing Component  : " + str(round(r0,2))+" ohm", font='calibri')
            lr0.place(x=110, y=502)
            lx0 = Label(wt, text="5)Magnetizing Reactance  : " + str(round(x0,2))+" ohm", font='calibri')
            lx0.place(x=450, y=502)
            # sc parameters
            rsc = (wsc1) / (isc1 ** 2)
            zsc = (vsc1) / (isc1)
            xsc = ((zsc ** 2) - (rsc ** 2)) ** 0.5
            r01 = rsc
            x01 = xsc
            lr01 = Label(wt, text="6) R Equivalent : " + str(round(r01,2))+" ohm",
                         font='calibri')
            lr01.place(x=110, y=525)
            lx01 = Label(wt, text="7) X Equivalent  : " + str(round(x01,2))+" ohm",
                         font='calibri')
            lx01.place(x=110, y=547)
            # x = Text(wt)
            # x.insert(INSERT, p.get())
            # x.pack()
            # k=Label(wt, text=p.get(), bg='white', fg="blue", font="Castellar")
            # k.grid(row=150,column=10)
            # print(p.get())
        except:
            messagebox.showerror("Error", "Data is Inavlid")
            #sys.exit()
            wt.destroy()
    except:
        #print("mandatory data missing")
        messagebox.showerror("Error", "mandatory data missing")
        wt.destroy()





def clearall():
        l.destroy()
        lcosx.destroy()
        liw.destroy()
        lim.destroy()
        lr0.destroy()
        lx0.destroy()
        lr01.destroy()
        lx01.destroy()
        voc.delete(0, END)
        ioc.delete(0, END)
        woc.delete(0, END)
        vsc.delete(0, END)
        isc.delete(0, END)
        wsc.delete(0, END)
        voc.focus()

mbut1= Button(wt, text='Submit', command=my, bg="Light Blue").place(x=250,y=400)
mbut2 = Button(wt, text='Clear', command=clearall, bg="Light Blue").place(x=350, y=400)












wt.mainloop()