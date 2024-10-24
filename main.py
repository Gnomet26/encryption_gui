from tkinter import*
from sezar import Sezar
from Morze import morze
from Vigenere import viginner
from md_5_coder import MD5
from SHA1 import SHA1
from SHA256 import SHA256
from Atbash import atbash
from Rail_fence import rail_fence
from Transmission_clipher import transmission_clipher
class MyWindow:
    def __init__(self):

        self.shifr_types = ["Sezor","vigenere","Rail fence","Transmission clipher","Atbash","morze","MD5","SHA1","SHA256"]

        self.oyna = Tk()
        self.oyna.geometry("800x400")
        self.oyna.resizable(False,False)
        self.oyna.title("Shifrlash oynasi")
    
        self.var=IntVar()
        self.flag = True
        self.values = StringVar(self.oyna)
        self.values.set("Shifr turini tanlash")

        #====================== Option Menu widget =========================================

        self.option_menu = OptionMenu(self.oyna,self.values,*self.shifr_types,command=self.option_menu_f)
        self.option_menu.place(x = 50,y = 50)

        #===================================================================================

        #=================== ochiq matn kiritish uchun =========================================

        self.info_1 = Label(self.oyna,text="Ochiq matnni uchun")
        self.info_1.place(x = 50,y = 210)
        self.ochiq_matn = Text(self.oyna,font=("Calibri",12),width=30, height=5)
        self.ochiq_matn.place(x = 50,y = 240)

        #====================================================================================

        #=================== kalit soz uchun ================================================

        self.info_2 = Label(self.oyna, text="Kalit so'z uchun")
        self.info_2.place(x=50, y=140)
        self.kalit_matn = Entry(self.oyna, font=("Calibri", 12), width=30)
        self.kalit_matn.place(x=50, y=170)

        #====================================================================================

        #==================== button uchun ==================================================

        self.button_ = Button(self.oyna, text="shifrlash", padx=40, pady=12, font=("calibri", 14),bd=3,command=lambda :self.shifrlash())
        self.button_.place(x=320, y=50)

        #====================================================================================

        #==================== sifrlangan matn uchun =========================================

        self.info_3 = Label(self.oyna, text="Shifrlangan matn uchun")
        self.info_3.place(x=400, y=140)
        self.shifr_matn = Text(self.oyna,width= 42, height=11)
        self.shifr_matn.place(x=400, y=170)

        #====================================================================================

        #==================== Radio button ==================================================

        self.R1 = Radiobutton(self.oyna, text="Shifrlash", value=1, font=("calibre",13), variable=self.var,command= lambda :self.selection())
        self.R1.place( x=550, y=50 )
        self.R2 = Radiobutton(self.oyna, text="DeShifrlash", value=2,font=("calibre",13), variable=self.var,command= lambda :self.selection())
        self.R2.place(x=550, y=80)

        #====================================================================================


        self.oyna.mainloop()

    def selection(self):
        #print("funksiya ishlayapti")
        if self.var.get() == 1:
            self.info_1.config(text="Ochiq matn uchun")
            self.info_3.config(text="shifrlangan matn")
            self.flag = True
        elif self.var.get() == 2:
            self.info_1.config(text="Shifrlangan matn uchun")
            self.info_3.config(text="Ochiq matn")
            self.flag = False

    def option_menu_f(self,event):

        if self.values.get() == "morze":
            self.kalit_matn.delete(0, END)
            self.kalit_matn.config(state=DISABLED)
            self.R1.config(state=NORMAL)
            self.R2.config(state=NORMAL)
        elif self.values.get() == "Sezor":
            self.kalit_matn.delete(0, END)
            self.kalit_matn.config(state=NORMAL)
            self.R1.config(state=NORMAL)
            self.R2.config(state=NORMAL)
        elif self.values.get() == "vigenere":
            self.kalit_matn.delete(0, END)
            self.kalit_matn.config(state=NORMAL)
            self.R1.config(state=NORMAL)
            self.R2.config(state=NORMAL)
        elif self.values.get() == "MD5":
            self.kalit_matn.delete(0, END)
            self.kalit_matn.config(state=DISABLED)
            self.R1.config(state=DISABLED)
            self.R2.config(state=DISABLED)
        elif self.values.get() == "SHA1":
            self.kalit_matn.delete(0, END)
            self.kalit_matn.config(state=DISABLED)
            self.R1.config(state=DISABLED)
            self.R2.config(state=DISABLED)
        elif self.values.get() == "SHA256":
            self.kalit_matn.delete(0, END)
            self.kalit_matn.config(state=DISABLED)
            self.R1.config(state=DISABLED)
            self.R2.config(state=DISABLED)
        elif self.values.get() == "Atbash":
            self.kalit_matn.delete(0, END)
            self.kalit_matn.config(state=DISABLED)
        elif self.values.get() == "Rail fence":
            self.kalit_matn.delete(0, END)
            self.kalit_matn.config(state=NORMAL)
            self.R1.config(state=NORMAL)
            self.R2.config(state=NORMAL)
        elif self.values.get() == "Transmission clipher":
            self.kalit_matn.delete(0, END)
            self.kalit_matn.config(state=NORMAL)
            self.R1.config(state=NORMAL)
            self.R2.config(state=NORMAL)


    def shifrlash(self):

        if self.values.get() == "Sezor":
            self.shifr_matn.config(state=NORMAL)
            self.shifr_matn.delete("1.0", "end")
            self.ss = Sezar(self.ochiq_matn.get("1.0","end"),int(self.kalit_matn.get()),self.flag)
            self.shifr_matn.insert(INSERT,self.ss.natija())
            self.shifr_matn.config(state=DISABLED)

        elif self.values.get() == "Atbash":
            self.shifr_matn.config(state=NORMAL)
            self.shifr_matn.delete("1.0", "end")
            self.atbash = atbash(self.ochiq_matn.get("1.0", "end"), self.flag)
            self.shifr_matn.insert(INSERT, self.atbash.natija())
            self.shifr_matn.config(state=DISABLED)

        elif self.values.get() == "morze":
            self.shifr_matn.config(state=NORMAL)
            self.shifr_matn.delete("1.0", "end")
            self.morze_ = morze(self.ochiq_matn.get("1.0","end"),self.flag)
            self.shifr_matn.insert(INSERT, self.morze_.natija())
            self.shifr_matn.config(state=DISABLED)

        elif self.values.get() == "vigenere":
            self.shifr_matn.config(state=NORMAL)
            self.shifr_matn.delete("1.0", "end")
            self.vv = viginner(self.ochiq_matn.get("1.0","end"),str(self.kalit_matn.get()),self.flag)
            self.shifr_matn.insert(INSERT, self.vv.natija())
            self.shifr_matn.config(state=DISABLED)

        elif self.values.get() == "MD5":
            self.shifr_matn.config(state=NORMAL)
            self.shifr_matn.delete("1.0", "end")
            self.md_5 = MD5(self.ochiq_matn.get("1.0","end"))
            self.shifr_matn.insert(INSERT, self.md_5.natija())
            self.shifr_matn.config(state=DISABLED)

        elif self.values.get() == "SHA1":
            self.shifr_matn.config(state=NORMAL)
            self.shifr_matn.delete("1.0", "end")
            self.sha_1 = SHA1(self.ochiq_matn.get("1.0","end"))
            self.shifr_matn.insert(INSERT, self.sha_1.natija())
            self.shifr_matn.config(state=DISABLED)

        elif self.values.get() == "SHA256":
            self.shifr_matn.config(state=NORMAL)
            self.shifr_matn.delete("1.0", "end")
            self.sha_256 = SHA256(self.ochiq_matn.get("1.0","end"))
            self.shifr_matn.insert(INSERT, self.sha_256.natija())
            self.shifr_matn.config(state=DISABLED)

        elif self.values.get() == "Rail fence":
            self.shifr_matn.config(state=NORMAL)
            self.shifr_matn.delete("1.0", "end")
            self.r_f = rail_fence(self.ochiq_matn.get("1.0","end"),int(self.kalit_matn.get()),self.flag)
            self.shifr_matn.insert(INSERT, self.r_f.natija())
            self.shifr_matn.config(state=DISABLED)

        elif self.values.get() == "Transmission clipher":
            self.shifr_matn.config(state=NORMAL)
            self.shifr_matn.delete("1.0", "end")
            self.t_cc = transmission_clipher(self.ochiq_matn.get("1.0", "end"), str(self.kalit_matn.get()), self.flag)
            self.shifr_matn.insert(INSERT, self.t_cc.natija())
            self.shifr_matn.config(state=DISABLED)


if __name__ == "__main__":
    MyWindow()