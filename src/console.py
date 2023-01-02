import tkinter as tk
from PIL import ImageTk,Image,ImageOps
import time
import customtkinter as ctk

import model
import user

class console:    
    def __init__(self):

        maincolor = "#A66213"
        subcolor = "#d19458"
        darkcolor = "#281500"
        pastelcolor = "#f2dfcb"
        pastel_darkcolor = "#563F24"
        hovorcolor = "#6E4617"

        self.size = "850x900"
        self.base = ctk.CTk(fg_color=darkcolor)
        self.base.geometry(self.size)
        self.base.title("ProjectDedenne for AI Pokemon Solutions - v0.1 Console ")
        self.base.resizable(width=False,height=False)
        ctk.set_default_color_theme("dark-blue")

        self.frame1 = ctk.CTkFrame(
            master=self.base,
            fg_color=subcolor
        )

        self.exitbutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="おわる",command=lambda:self.base.destroy(),fg_color="red",hover_color="maroon")
        self.exitbutton.pack(padx=10,pady=20)
        self.movebutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="うえ",command=lambda:self.moveup(),fg_color=maincolor,hover_color=hovorcolor)
        self.movebutton.pack(padx=10,pady=20)
        self.movedbutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="した",command=lambda:self.movedown(),fg_color=maincolor,hover_color=hovorcolor)
        self.movedbutton.pack(padx=10,pady=20)
        self.reversebutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="ふりかえる",command=lambda:self.reverse(),fg_color=maincolor,hover_color=hovorcolor)
        self.reversebutton.pack(padx=10,pady=20)
        self.pushbutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="おくる",command=lambda:push(),fg_color=maincolor,hover_color=hovorcolor)
        self.pushbutton.pack(padx=10,pady=20,side=tk.BOTTOM)
        
        self.frame1.pack(side=tk.LEFT,padx=10,pady=10,fill=tk.Y)

        self.frame2 = ctk.CTkFrame(
            master=self.base,
            fg_color=subcolor
        )
        self.frame2.pack(side=tk.RIGHT,padx=10,pady=10,fill=tk.BOTH)
        self.canvas = ctk.CTkCanvas(self.frame2,bg=darkcolor,width=750,height=500)
        
        self.Mismagiusimage = Image.open("./img/Dedenne.png")
        self.Sprigatitoimg = ImageTk.PhotoImage(self.Mismagiusimage)
        self.model = model.Model()
        
        self.model.setModelPosX(425) #初期値：425（中央）
        self.model.setModelPosY(250) #初期値：250（中央）
        self.User = user.user()
        self.imgid = self.canvas.create_image(
            self.model.getModelPosX(),
            self.model.getModelPosY(),
            image=self.Sprigatitoimg
        )
        self.outlabel = ctk.CTkLabel(self.frame2,text="出力",text_color=pastelcolor)
        self.outputbox = ctk.CTkTextbox(self.frame2,width=600,height=200,fg_color=pastel_darkcolor,corner_radius=15)
        self.outputbox.configure(state="disabled")
        self.inlabel = ctk.CTkLabel(self.frame2,text="入力",text_color=pastelcolor)
        self.inputbox = ctk.CTkTextbox(self.frame2,width=600,height=50,fg_color=pastel_darkcolor,corner_radius=15)
        self.canvas.pack(padx=10,pady=10)
        self.outlabel.pack(padx=5,pady=3)
        self.outputbox.pack(padx=5,pady=3)
        self.inlabel.pack(padx=5,pady=3)
        self.inputbox.pack(padx=5,pady=3)

        self.inputbox.bind('<Return>',lambda event:self.push())

    def moveup(self):
        for i in range(10):
            self.canvas.move(self.imgid,0,-5)
            self.canvas.update()
            time.sleep(0.03)
        self.model.setModelPosY(self.model.getModelPosY()-50)
    def movedown(self):
        for i in range(10):
            self.canvas.move(self.imgid,0,5)
            self.canvas.update()
            time.sleep(0.03)
        self.model.setModelPosY(self.model.getModelPosY()+50)

    def push(self):
        text = self.inputbox.get("1.0","end")
        if not text.isspace():
            text = text.replace("\n","")
            self.inputbox.delete("1.0","end")
            self.insertoutput(self.User.getUserName()+":"+text)
            self.model.send(text)
            self.insertoutput(self.model.getModelName()+":"+self.model.getSendMessage())

    def reverse(self):
            self.canvas.delete(self.imgid)
            self.Mismagiusimage = ImageOps.mirror(self.Mismagiusimage)
            self.Mismagiusimg = ImageTk.PhotoImage(self.Mismagiusimage)
            self.imgid = self.canvas.create_image(
                self.model.getModelPosX(),
                self.model.getModelPosY(),
                image=self.Mismagiusimg
            )    

    def insertoutput(self,text):
            self.outputbox.configure(state="normal")
            self.outputbox.insert("end",text+"\n")
            self.outputbox.configure(state="disabled")