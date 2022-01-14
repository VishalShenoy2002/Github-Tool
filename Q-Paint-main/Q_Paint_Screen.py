from tkinter import *
from tkinter.ttk import Scale
from tkinter.colorchooser import askcolor


class Paintbox:
    def __init__(self,master):
        self.master=master

        self.paintbox_frame=LabelFrame(self.master,text='PAINTBOX',font=('',14,'bold'),bd=5)
        self.paintbox_frame.pack(anchor=NW,padx=20)
        self.fill='black'
        self.bg='white'

        self.color1_button=Button(self.paintbox_frame,bg='#ff0000',width=2,relief=RIDGE,command=lambda: self.change_color('#ff0000'))
        self.color1_button.grid(row=0,column=0)

        self.color2_button=Button(self.paintbox_frame,bg='#ff4000',width=2,relief=RIDGE,command=lambda: self.change_color('#ff4000'))
        self.color2_button.grid(row=0,column=1)

        self.color3_button=Button(self.paintbox_frame,bg='#ff8000',width=2,relief=RIDGE,command=lambda: self.change_color('#ff8000'))
        self.color3_button.grid(row=0,column=2)

        self.color4_button=Button(self.paintbox_frame,bg='#ffbf00',width=2,relief=RIDGE,command=lambda: self.change_color('#ffbf00'))
        self.color4_button.grid(row=0,column=3)

        self.color5_button=Button(self.paintbox_frame,bg='#ffbf10',width=2,relief=RIDGE,command=lambda: self.change_color('#ffbf10'))
        self.color5_button.grid(row=0,column=4)

        self.color6_button=Button(self.paintbox_frame,bg='#ffff00',width=2,relief=RIDGE,command=lambda: self.change_color('#ffff00'))
        self.color6_button.grid(row=0,column=5)

        self.color7_button=Button(self.paintbox_frame,bg='#bfff00',width=2,relief=RIDGE,command=lambda: self.change_color('#bfff00'))
        self.color7_button.grid(row=0,column=6)

        self.color8_button=Button(self.paintbox_frame,bg='#80ff00',width=2,relief=RIDGE,command=lambda: self.change_color('#80ff00'))
        self.color8_button.grid(row=0,column=7)

        self.color9_button=Button(self.paintbox_frame,bg='#40ff00',width=2,relief=RIDGE,command=lambda: self.change_color('#40ff00'))
        self.color9_button.grid(row=0,column=8)

        self.color10_button=Button(self.paintbox_frame,bg='#00ff80',width=2,relief=RIDGE,command=lambda: self.change_color('#00ff80'))
        self.color10_button.grid(row=0,column=9)

        self.color11_button=Button(self.paintbox_frame,bg='#00ffbf',width=2,relief=RIDGE,command=lambda: self.change_color('#00ffbf'))
        self.color11_button.grid(row=0,column=10)

        self.color12_button=Button(self.paintbox_frame,bg='#00ffff',width=2,relief=RIDGE,command=lambda: self.change_color('#00ffff'))
        self.color12_button.grid(row=0,column=11)

        self.color13_button=Button(self.paintbox_frame,bg='#00bfff',width=2,relief=RIDGE,command=lambda: self.change_color('#00bfff'))
        self.color13_button.grid(row=1,column=11)

        self.color14_button=Button(self.paintbox_frame,bg='#0080ff',width=2,relief=RIDGE,command=lambda: self.change_color('#0080ff'))
        self.color14_button.grid(row=1,column=10)

        self.color15_button=Button(self.paintbox_frame,bg='#0040ff',width=2,relief=RIDGE,command=lambda: self.change_color('#0040ff'))
        self.color15_button.grid(row=1,column=9)

        self.color16_button=Button(self.paintbox_frame,bg='#0000ff',width=2,relief=RIDGE,command=lambda: self.change_color('#0000ff'))
        self.color16_button.grid(row=1,column=8)

        self.color17_button=Button(self.paintbox_frame,bg='#4000ff',width=2,relief=RIDGE,command=lambda: self.change_color('#4000ff'))
        self.color17_button.grid(row=1,column=7)

        self.color18_button=Button(self.paintbox_frame,bg='#8000ff',width=2,relief=RIDGE,command=lambda: self.change_color('#8000ff'))
        self.color18_button.grid(row=1,column=6)

        self.color19_button=Button(self.paintbox_frame,bg='#8000ff',width=2,relief=RIDGE,command=lambda: self.change_color('#8000ff'))
        self.color19_button.grid(row=1,column=5)

        self.color20_button=Button(self.paintbox_frame,bg='#bf00ff',width=2,relief=RIDGE,command=lambda: self.change_color('#bf00ff'))
        self.color20_button.grid(row=1,column=4)

        self.color21_button=Button(self.paintbox_frame,bg='#ff00ff',width=2,relief=RIDGE,command=lambda: self.change_color('#ff00ff'))
        self.color21_button.grid(row=1,column=3)

        self.color22_button=Button(self.paintbox_frame,bg='#ff00bf',width=2,relief=RIDGE,command=lambda: self.change_color('#ff00bf'))
        self.color22_button.grid(row=1,column=2)

        self.color23_button=Button(self.paintbox_frame,bg='#ff0080',width=2,relief=RIDGE,command=lambda: self.change_color('#ff0080'))
        self.color23_button.grid(row=1,column=1)

        self.color24_button=Button(self.paintbox_frame,bg='#ff0040',width=2,relief=RIDGE,command=lambda: self.change_color('#ff0040'))
        self.color24_button.grid(row=1,column=0)

        self.color25_button=Button(self.paintbox_frame,bg='#ffffff',width=2,relief=RIDGE,command=lambda: self.change_color('#ffffff'))
        self.color25_button.grid(row=2,column=0)

        self.color26_button=Button(self.paintbox_frame,bg='#F5F5F5',width=2,relief=RIDGE,command=lambda: self.change_color('#F5F5F5'))
        self.color26_button.grid(row=2,column=1)

        self.color27_button=Button(self.paintbox_frame,bg='#D3D3D3',width=2,relief=RIDGE,command=lambda: self.change_color('#D3D3D3'))
        self.color27_button.grid(row=2,column=2)

        self.color28_button=Button(self.paintbox_frame,bg='#C0C0C0',width=2,relief=RIDGE,command=lambda: self.change_color('#C0C0C0'))
        self.color28_button.grid(row=2,column=3)

        self.color29_button=Button(self.paintbox_frame,bg='#A9A9A9',width=2,relief=RIDGE,command=lambda: self.change_color('#A9A9A9'))
        self.color29_button.grid(row=2,column=4)

        self.color30_button=Button(self.paintbox_frame,bg='#999999',width=2,relief=RIDGE,command=lambda: self.change_color('#999999'))
        self.color30_button.grid(row=2,column=5)
        
        self.color31_button=Button(self.paintbox_frame,bg='#777777',width=2,relief=RIDGE,command=lambda: self.change_color('#777777'))
        self.color31_button.grid(row=2,column=6)

        self.color32_button=Button(self.paintbox_frame,bg='#666666',width=2,relief=RIDGE,command=lambda: self.change_color('#666666'))
        self.color32_button.grid(row=2,column=7)

        self.color33_button=Button(self.paintbox_frame,bg='#555555',width=2,relief=RIDGE,command=lambda: self.change_color('#555555'))
        self.color33_button.grid(row=2,column=8)

        self.color34_button=Button(self.paintbox_frame,bg='#333333',width=2,relief=RIDGE,command=lambda: self.change_color('#333333'))
        self.color34_button.grid(row=2,column=9)

        self.color35_button=Button(self.paintbox_frame,bg='#111111',width=2,relief=RIDGE,command=lambda: self.change_color('#111111'))
        self.color35_button.grid(row=2,column=10)
        
        self.color36_button=Button(self.paintbox_frame,bg='#000000',width=2,relief=RIDGE,command=lambda: self.change_color('#000000'))
        self.color36_button.grid(row=2,column=11)

    def change_color(self,x):
        self.fill=x


class QPaint:
    def __init__(self,master):
        self.master=master
        self.master.geometry('750x500')
        self.master.title('Q Paint') 
        
        self.painting_tools_frame=Frame(self.master)
        self.painting_tools_frame.pack(anchor=NW)

        self.paintbox=Paintbox(self.painting_tools_frame)
        
        self.penwidth=IntVar()
        self.penwidth.set(7)

        self.penwidth_label=Label(self.painting_tools_frame,text='Pen Width :',font=('',12,'bold'))
        self.penwidth_label.pack(anchor=NW,padx=20)

        self.penwidth_scale=Scale(self.painting_tools_frame,from_=7,to=70,length=150,variable=self.penwidth)
        self.penwidth_scale.pack(anchor=NW,padx=40)

        self.canvas=Canvas(self.master,bd=4,bg=self.paintbox.bg,relief=RIDGE)
        self.canvas.bind('<B1-Motion>',self.draw)
        self.canvas.bind('<B3-Motion>',self.erase)
        self.canvas.bind('<Double-Button-3>',self.clear)
        self.canvas.pack(padx=10,pady=5,fill=BOTH,expand=True)


        self.master.mainloop()

    def draw(self,event):
        x1,y1=(event.x-0.5),(event.y-0.5)
        x2,y2=(event.x+0.5),(event.y+0.5)
        self.canvas.create_line(x1,y1,x2,y2,width=self.penwidth.get(),fill=self.paintbox.fill,capstyle=ROUND,smooth=True)

    def erase(self,event):
        x1,y1=(event.x-0.5),(event.y-0.5)
        x2,y2=(event.x+0.5),(event.y+0.5)
        self.canvas.create_line(x1,y1,x2,y2,width=self.penwidth.get(),fill='white',capstyle=ROUND,smooth=True)
    def clear(self,event):
        self.canvas.delete('all')
    def undo(self,event):
        self.canvas.clipboard_get()

    
   


if __name__ == "__main__":
    root=Tk()
    app=QPaint(root)