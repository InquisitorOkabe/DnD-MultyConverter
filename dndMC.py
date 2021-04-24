#-----Import-----
from tkinter import *
class LineFrame:
    def __init__(self,core,lbg='gray25',bg='SystemButtonFace'):
        self.core = core
        self.line = Frame(core,bg=lbg)
        self.frame = Frame(self.line,bg=bg)

    def place(self,x=0,y=0,width=0,height=0,size=1,relx=0,rely=0,bordermode='ignore'):
        self.line.place(x=x,y=y,width=width,height=height,relx=relx,rely=rely)
        self.frame.place(x=size,y=size,width=width-(size*2),height=height-(size*2))

class LineLabel:
    def __init__(self,core,lbg='gray25',bg='SystemButtonFace',fg='gray0',text=''):
        self.core = core
        self.line = Frame(core,bg=lbg)
        self.label = Label(self.line,bg=bg,fg=fg,text=text)
    def place(self,x=0,y=0,width=0,height=0,size=1,relx=0,rely=0,bordermode='ignore'):
        self.line.place(x=x,y=y,width=width,height=height,relx=relx,rely=rely)
        self.label.place(x=size,y=size,width=width-(size*2),height=height-(size*2))
    def bind(self,event,function):
        self.line.bind(event,function)

#-----Root-----

root = Tk()
root.geometry('324x142')
root.resizable(False,False)
root.title('DnD Монетный Конвернер')

#-----Variable-----

#--Money--

size = [120, 80] # 0 - width
money = [1, 10, 50, 100, 1000]
tx = ['медь(мм)', 'серебро(см)','электрум(эм)','золото(зм)','платина(пм)']
m = [Entry(),Entry(),Entry(),Entry(),Entry()]
l = [LineLabel(root),LineLabel(root),LineLabel(root),LineLabel(root),LineLabel(root)]
t = [Label(),Label(),Label(),Label(),Label(),]
rope = Button(text='Сброс')
start = Button(text='Посчитать')

#-----Place-----

wh = 0
while wh != len(m):
    m[wh].insert(END, '0')
    m[wh].place(x=2, y=2+20*wh, width=size[0], height=18)
    l[wh].place(x=size[0]+2+size[1], y=2+20*wh, width=size[0], height=18)
    t[wh].place(x=size[0]+2, y=2+20*wh, width=size[1], height=18)
    t[wh].config(text=tx[wh])
    l[wh].label.config(text='---')
    wh += 1
start.place(x=2,y=122,width=size[0]*2+size[1],height=18)
rope.place(x=2,y=102,width=size[0]*2+size[1],height=18)

#-----Def-----

def calc():
    my = [0,0,0,0,0]
    run(my)
    my[1] = my[0]/money[1]
    my[2] = my[0]/money[2]
    my[3] = my[0]/money[3]
    my[4] = my[0]/money[4]
    wh = 0
    while wh != len(l):
        l[wh].label.config(text=my[wh])
        wh += 1
    # print(my)

def run(my):
    wh = 0
    while wh != len(money):
        my[0] += int(m[wh].get())*int(money[wh])
        print(m[wh].get(), money[wh])
        wh += 1
    return my

def nope():
    wh = 0
    while wh != len(m):
        m[wh].delete(0, END)
        m[wh].insert(END, 0)
        l[wh].label.config(text='')
        wh += 1

#-----Bind-----

root.bind('<Escape>', lambda x: exit())
root.bind('<Return>', lambda x: calc())
start.bind('<1>', lambda x: calc())
rope.bind('<1>', lambda x: nope())

#-----Skript-----
m[0].focus_set()

#-----End-----
root.mainloop()
