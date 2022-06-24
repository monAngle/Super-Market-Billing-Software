from cProfile import label
from textwrap import fill
import math,random,os
from tkinter import *
from tkinter import font
from tkinter.font import BOLD, ITALIC
from turtle import color, right, title, width
from tkinter import messagebox
class Bill_App:
    def __init__(self,window):
        self.window=window
        self.window.geometry("1350x750+0+0")
        self.window.title("Super Market Billing Software")
        bg_color="#660066"
        title=Label(self.window,text="Billing System",bd=13,relief="groove",bg=bg_color,fg="WHITE",font=("Algerian",25,BOLD),pady=2).pack(fill=X)

        # Variables
        # cosmetics variables
        self.Shower_gel=IntVar()
        self.face_pack=IntVar()
        self.face_wash=IntVar()
        self.make_up=IntVar()
        self.lotion=IntVar()
        self.hair_oil=IntVar()
        # grocery variables
        self.rice=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.oil=IntVar()
        self.dry_fruits=IntVar()
        self.cookies=IntVar()
        # cold Drinks
        self.Mountain_Dew=IntVar()
        self.sting=IntVar()
        self.coca_cola=IntVar()
        self.maaza=IntVar()
        self.sprite=IntVar()
        self.red_bull=IntVar()
        # customer details variables
        self.bill_no=StringVar()
        b=random.randint(1000,9999)
        self.bill_no.set(str(b))
        self.search=StringVar()
        self.customer_Name=StringVar()
        self.contact_Number=StringVar()
        # bill menu variable
        self.Total_Grocery_Price=StringVar()
        self.Total_Cosmetics_Price=StringVar()
        self.Total_Cold_Drink_Price=StringVar()
        self.Grocery_Tax=StringVar()
        self.Cosmetics_Tax=StringVar()
        self.Cold_Drink_Tax=StringVar()
        # Customer Details Frame
        frame1=LabelFrame(self.window,bd=10,relief="raised",text="Customer Info",fg="gold",bg=bg_color,font=("Algerian",15,BOLD))
        frame1.place(x=0,y=80,relwidth=1)

        name_label=Label(frame1,text="Customer Name",fg="white",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=0,column=0,padx=20,pady=5)
        name_entry=Entry(frame1,width=15,textvariable=self.customer_Name,font="arial",bd=7,relief="raised").grid(row=0,column=1,padx=10,pady=5)

        pn_label=Label(frame1,text="Contact Number",fg="white",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=0,column=2,padx=20,pady=5)
        number_entry=Entry(frame1,width=15,textvariable=self.contact_Number,font="arial",bd=7,relief="raised").grid(row=0,column=3,padx=10,pady=5)

        
        # cosmetics Frame
        Frame2=LabelFrame(self.window,bd=10,relief=GROOVE,text="Cosmetics",fg="gold",bg=bg_color,font=("Algerian",15,BOLD),pady=2)
        Frame2.place(x=5,y=170,width=325,height=380)

        bath_lbl=Label(Frame2,text="Shower gel",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=0,column=0,padx=10,pady=10,sticky="W")
        bath_txt=Entry(Frame2,width=10,textvariable=self.Shower_gel,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl=Label(Frame2,text="Face Pack",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=1,column=0,padx=10,pady=10,sticky="W")
        face_cream_txt=Entry(Frame2,width=10,textvariable=self.face_pack,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=1,column=1,padx=10,pady=10)

        face_wash_lbl=Label(Frame2,text="Face Wash",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=2,column=0,padx=10,pady=10,sticky="W")
        face_wash_txt=Entry(Frame2,width=10,textvariable=self.face_wash,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=2,column=1,padx=10,pady=10)

        make_up_lbl=Label(Frame2,text="Make-up Kit",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=3,column=0,padx=10,pady=10,sticky="W")
        make_up_txt=Entry(Frame2,width=10,textvariable=self.make_up,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=3,column=1,padx=10,pady=10)

        body_lbl=Label(Frame2,text="Body Lotion",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=4,column=0,padx=10,pady=10,sticky="W")
        body_txt=Entry(Frame2,width=10,textvariable=self.lotion,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=4,column=1,padx=10,pady=10)

        hair_lbl=Label(Frame2,text="Hair Oil",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=5,column=0,padx=10,pady=10,sticky="W")
        hair_txt=Entry(Frame2,width=10,textvariable=self.hair_oil,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=5,column=1,padx=10,pady=10)

        # Grocery Frame
        
        Frame3=LabelFrame(self.window,bd=10,relief=GROOVE,text="GROCERY",fg="gold",bg=bg_color,font=("Algerian",15,BOLD),pady=2)
        Frame3.place(x=340,y=170,width=325,height=380)

        rice_lbl=Label(Frame3,text="Rice",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=0,column=0,padx=10,pady=10,sticky="W")
        rice_txt=Entry(Frame3,width=10,textvariable=self.rice,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=0,column=1,padx=10,pady=10)

        wheat_lbl=Label(Frame3,text="Wheat",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=1,column=0,padx=10,pady=10,sticky="W")
        wheat_cream_txt=Entry(Frame3,width=10,textvariable=self.wheat,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=1,column=1,padx=10,pady=10)

        Sugar_lbl=Label(Frame3,text="Sugar",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=2,column=0,padx=10,pady=10,sticky="W")
        sugar_wash_txt=Entry(Frame3,width=10,textvariable=self.sugar,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=2,column=1,padx=10,pady=10)

        oil_lbl=Label(Frame3,text="Mustard Oil",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=3,column=0,padx=10,pady=10,sticky="W")
        oil_up_txt=Entry(Frame3,width=10,textvariable=self.oil,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=3,column=1,padx=10,pady=10)

        nutrition_lbl=Label(Frame3,text="Dryfruits Pack",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=4,column=0,padx=10,pady=10,sticky="W")
        nutrition_txt=Entry(Frame3,width=10,textvariable=self.dry_fruits,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=4,column=1,padx=10,pady=10)

        cookies_lbl=Label(Frame3,text="Cookies",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=5,column=0,padx=10,pady=10,sticky="W")
        cookies_txt=Entry(Frame3,width=10,textvariable=self.cookies,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=5,column=1,padx=10,pady=10)

# Cold Drinks Frame
        Frame4=LabelFrame(self.window,bd=10,relief=GROOVE,text="Cold Drinks",fg="gold",bg=bg_color,font=("Algerian",15,BOLD),pady=2)
        Frame4.place(x=670,y=170,width=325,height=380)

        dew_lbl=Label(Frame4,text="Mountain Dew",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=0,column=0,padx=10,pady=10,sticky="W")
        dew_txt=Entry(Frame4,width=10,textvariable=self.Mountain_Dew,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=0,column=1,padx=10,pady=10)

        sting_lbl=Label(Frame4,text="Sting",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=1,column=0,padx=10,pady=10,sticky="W")
        sting_cream_txt=Entry(Frame4,width=10,textvariable=self.sting,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=1,column=1,padx=10,pady=10)

        coke_lbl=Label(Frame4,text="Coca-Cola",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=2,column=0,padx=10,pady=10,sticky="W")
        coke_txt=Entry(Frame4,width=10,textvariable=self.coca_cola,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=2,column=1,padx=10,pady=10)

        maza_lbl=Label(Frame4,text="Maaza",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=3,column=0,padx=10,pady=10,sticky="W")
        maza_txt=Entry(Frame4,width=10,textvariable=self.maaza,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=3,column=1,padx=10,pady=10)

        sprite_lbl=Label(Frame4,text="sprite",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=4,column=0,padx=10,pady=10,sticky="W")
        sprite_txt=Entry(Frame4,width=10,textvariable=self.sprite,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=4,column=1,padx=10,pady=10)

        enrgy_lbl=Label(Frame4,text="RedBull",fg="lightgreen",bg=bg_color,font=("Times New Roman",15,BOLD)).grid(row=5,column=0,padx=10,pady=10,sticky="W")
        enrgy_txt=Entry(Frame4,width=10,textvariable=self.red_bull,font=("Times New Roman",15,BOLD),bd=6,relief=RAISED).grid(row=5,column=1,padx=10,pady=10)

# Bill Area frame
        Frame5=LabelFrame(self.window,bd=10,relief=GROOVE)
        Frame5.place(x=1010,y=170,width=325,height=380)
        bill_title=Label(Frame5,text="Bill Area",relief="groove",font="Arial 15 bold",bd=7).pack(fill=X)
        scroll_y=Scrollbar(Frame5,orient=VERTICAL)
        self.text_area=Text(Frame5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.text_area.yview)
        self.text_area.pack(fill=BOTH,expand=1)
    
# frame for Button
        Frame6=LabelFrame(self.window,bd=10,relief=GROOVE,text="Bill Menu",fg="gold",bg=bg_color,font=("Algerian",15,BOLD),pady=2)
        Frame6.place(x=0,y=560,relwidth=1,height=140)
        p1_lbl=Label(Frame6,text="Total Grocery Price",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,BOLD)).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        p1_txt=Entry(Frame6,width=18,textvariable=self.Total_Grocery_Price,font="arial 10 bold",bd=7,relief=RAISED).grid(row=0,column=1,padx=10,pady=1)

        p2_lbl=Label(Frame6,text="Total Cosmetics Price",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,BOLD)).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        p2_txt=Entry(Frame6,width=18,textvariable=self.Total_Cosmetics_Price,font="arial 10 bold",bd=7,relief=RAISED).grid(row=1,column=1,padx=10,pady=1)

        p3_lbl=Label(Frame6,text="Total Cold Drink Price",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,BOLD)).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        p3_txt=Entry(Frame6,width=18,textvariable=self.Total_Cold_Drink_Price,font="arial 10 bold",bd=7,relief=RAISED).grid(row=2,column=1,padx=10,pady=1)

        t1_lbl=Label(Frame6,text="Grocery Tax",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,BOLD)).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        t1_txt=Entry(Frame6,width=18,textvariable=self.Grocery_Tax,font="arial 10 bold",bd=7,relief=RAISED).grid(row=0,column=3,padx=10,pady=1)

        t2_lbl=Label(Frame6,text="Cosmetics Tax",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,BOLD)).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        p2_txt=Entry(Frame6,width=18,textvariable=self.Cosmetics_Tax,font="arial 10 bold",bd=7,relief=RAISED).grid(row=1,column=3,padx=10,pady=1)

        t3_lbl=Label(Frame6,text="Cold Drink Tax",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,BOLD)).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        t3_txt=Entry(Frame6,width=18,textvariable=self.Cold_Drink_Tax,font="arial 10 bold",bd=7,relief=RAISED).grid(row=2,column=3,padx=10,pady=1)

        btn1=Frame(Frame6,bd=7,relief=GROOVE)
        btn1.place(x=750,width=570,height=105)

        t_btn=Button(btn1,command=self.total,text="Total",bg="VioletRed3",fg="white",bd=4,pady=15,width=11,font="arial 13 bold").grid(row=0,column=0,padx=5,pady=5)
        g_btn=Button(btn1,command=self.bill_area,text="Generate Bill",bg="VioletRed3",fg="white",bd=4,pady=15,width=11,font="arial 13 bold").grid(row=0,column=1,padx=5,pady=5)
        c_btn=Button(btn1,text="Clear",command=self.clear_data,bg="VioletRed3",fg="white",bd=4,pady=15,width=11,font="arial 13 bold").grid(row=0,column=2,padx=5,pady=5)
        e_btn=Button(btn1,text="Exit",command=self.exit_app,bg="VioletRed3",fg="white",bd=4,pady=15,width=11,font="arial 13 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_to()
    def total(self):
        self.cos_gel_p=self.Shower_gel.get()*150
        self.fp_p=self.face_pack.get()*250
        self.fw_p=self.face_wash.get()*99
        self.mu_p=self.make_up.get()*499
        self.l_p=self.lotion.get()*199
        self.h_oil_p=self.hair_oil.get()*89
        self.total_cosmetic_price=float(
            self.cos_gel_p+               
            self.fp_p+
            self.fw_p+
            self.mu_p+
            self.l_p+
            self.h_oil_p
           )  
        self.Total_Cosmetics_Price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.Cosmetics_Tax.set("Rs. "+str(self.c_tax))
        self.r_p=self.rice.get()*50
        self.w_p=self.wheat.get()*40
        self.s_p=self.sugar.get()*40
        self.o_p=self.oil.get()*190
        self.df_p=self.dry_fruits.get()*850
        self.cookie_p=(self.cookies.get()*250)
        self.total_grocery_price=float(
            self.r_p+
            self.w_p+
            self.s_p+
            self.o_p+
            self.df_p+
            self.cookie_p
           )  
        self.Total_Grocery_Price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.08),2)
        self.Grocery_Tax.set("Rs. "+str(self.g_tax))

        self.m_d_p=self.Mountain_Dew.get()*35
        self.sting_p=self.sting.get()*20
        self.coke_p=self.coca_cola.get()*85
        self.maaza_p=self.maaza.get()*89
        self.sprite_p=self.sprite.get()*65
        self.red_bull_p=self.red_bull.get()*30
        self.total_cold_drinks_price=float(
            self.m_d_p+
            self.sting_p+
            self.coke_p+
            self.maaza_p+
            self.sprite_p+
            self.red_bull_p
           )  
        self.Total_Cold_Drink_Price.set("Rs. "+str(self.total_cold_drinks_price)) 
        self.cd_tax=round((self.total_cold_drinks_price*0.1),2)  
        self.Cold_Drink_Tax.set("Rs. "+str(self.cd_tax) )    

        self.Total_Bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_drinks_price+
                              self.c_tax+
                              self.g_tax+
                              self.cd_tax
                             )
    def welcome_to(self):
        self.text_area.delete("1.0",END)
        self.text_area.insert(END,"\tWelcome to Morehyper Mart")
        self.text_area.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.text_area.insert(END,f"\n Customer Name: {self.customer_Name.get()}")
        self.text_area.insert(END,f"\n Contact No:{self.contact_Number.get()}")
        self.text_area.insert(END,f"\n ==================================")
        self.text_area.insert(END,f"\n Products\t\tQTY\tPrice")
        self.text_area.insert(END,f"\n ==================================")

    def bill_area(self):
        if self.customer_Name.get()=="" or self.contact_Number.get()=="":
            messagebox.showerror("Error","Dear Customer,Plaese Enter Your Details")
        else:
            self.welcome_to()
        #cosmetics
            if self.Shower_gel.get()!=0:
                self.text_area.insert(END,f"\nShower Gel\t\t{self.Shower_gel.get()}\t{self.cos_gel_p} ")
            if self.face_pack.get()!=0:
                self.text_area.insert(END,f"\nFace Pack\t\t{self.face_pack.get()}\t{self.fp_p} ")   
            if self.face_wash.get()!=0:
                self.text_area.insert(END,f"\nFace_Wash\t\t{self.face_wash.get()}\t{self.fw_p} ")
            if self.make_up.get()!=0:
                self.text_area.insert(END,f"\nMake Up Kit\t\t{self.make_up.get()}\t{self.mu_p} ")
            if self.lotion.get()!=0:
                self.text_area.insert(END,f"\nBody Lotion\t\t{self.lotion.get()}\t{self.l_p} ")
            if self.hair_oil.get()!=0:
                self.text_area.insert(END,f"\nHair Oil\t\t{self.hair_oil.get()}\t{self.h_oil_p} ")
        #grocery
            if self.rice.get()!=0:
                self.text_area.insert(END,f"\nRice\t\t{self.rice.get()}\t{self.r_p} ")
            if self.wheat.get()!=0:
                self.text_area.insert(END,f"\nWheat\t\t{self.wheat.get()}\t{self.w_p} ")   
            if self.sugar.get()!=0:
                self.text_area.insert(END,f"\nSugar\t\t{self.sugar.get()}\t{self.s_p} ")
            if self.oil.get()!=0:
                self.text_area.insert(END,f"\nOil\t\t{self.oil.get()}\t{self.o_p} ")
            if self.dry_fruits.get()!=0:
                self.text_area.insert(END,f"\nDry_Fruits\t\t{self.dry_fruits.get()}\t{self.df_p} ")
            if self.cookies.get()!=0:
                self.text_area.insert(END,f"\nCoockies\t\t{self.cookies.get()}\t{self.cookie_p} ")
        #cold drinks
            if self.Mountain_Dew.get()!=0:
                self.text_area.insert(END,f"\nMountain Dew\t\t{self.Mountain_Dew.get()}\t{self.m_d_p} ")
            if self.sting.get()!=0:
                self.text_area.insert(END,f"\nSting\t\t{self.sting.get()}\t{self.sting_p} ")   
            if self.coca_cola.get()!=0:
                self.text_area.insert(END,f"\nCoca Cola\t\t{self.coca_cola.get()}\t{self.coke_p} ")
            if self.maaza.get()!=0:
                self.text_area.insert(END,f"\nMaaza\t\t{self.maaza.get()}\t{self.maaza_p} ")
            if self.sprite.get()!=0:
                self.text_area.insert(END,f"\nSprite\t\t{self.sprite.get()}\t{self.sprite_p} ")
            if self.red_bull.get()!=0:
                self.text_area.insert(END,f"\nHair Oil\t\t{self.red_bull.get()}\t{self.red_bull_p} ")

            self.text_area.insert(END,f"\n-----------------------------------")
            if self.Cosmetics_Tax.get()!="Rs. 0.0":
                self.text_area.insert(END,f"\nCosmetics Tax\t\t\t{self.Cosmetics_Tax.get()}")
        
            if self.Grocery_Tax.get()!="Rs. 0.0":
                self.text_area.insert(END,f"\nGrocery Tax\t\t\t{self.Grocery_Tax.get()}")

            if self.Cold_Drink_Tax.get()!="Rs. 0.0":
                self.text_area.insert(END,f"\nCold Drink Tax\t\t\t{self.Cold_Drink_Tax.get()}")
            self.text_area.insert(END,f"\nTotal Bill : \t\t\tRs. {self.Total_Bill}")
            self.text_area.insert(END,f"\n-----------------------------------")
            
    def clear_data(self):
        op=messagebox.askyesno("Exit","Do you want to clear?")
        if op>0:
        # cosmetics variables
            self.Shower_gel.set(0)
            self.face_pack.set(0)
            self.face_wash.set(0)
            self.make_up.set(0)
            self.lotion.set(0)
            self.hair_oil.set(0)
        # grocery variables
            self.rice.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.oil.set(0)
            self.dry_fruits.set(0)
            self.cookies.set(0)
        # cold Drinks
            self.Mountain_Dew.set(0)
            self.sting.set(0)
            self.coca_cola.set(0)
            self.maaza.set(0)
            self.sprite.set(0)
            self.red_bull.set(0)
        # customer details variables
            self.bill_no.set("")
            b=random.randint(1000,9999)
            self.bill_no.set(str(b))
            self.search.set("")
            self.customer_Name.set("")
            self.contact_Number.set("")
        # bill menu variable
            self.Total_Grocery_Price.set("")
            self.Total_Cosmetics_Price.set("")
            self.Total_Cold_Drink_Price.set("")
            self.Grocery_Tax.set("")
            self.Cosmetics_Tax.set("")
            self.Cold_Drink_Tax.set("")
            self.welcome_to()

    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.window.destroy()

window=Tk()
object=Bill_App(window)
window.mainloop()