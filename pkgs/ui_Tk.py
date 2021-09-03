from tkinter import *

# Кастомный класс ярлыка с рамкой и "рамки" с рамкой.
# Класс говно, так что обращаться к нему напрямую можно только костылями.
# Если потребуется что-то достать - пишем class.line/label/frame
# В зависимости от того, к чему обращаемся. Line - рамка.
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

# Класс интерфейса.
class Ui_Form:
    def __init__(self):
        # Размеры некоторых объектов.
        self.size = [80, 86, 90]
        # Само окно.
        self.root = Tk()
        self.root.bind('<Escape>', lambda x: exit())
        self.root.geometry('346x240')
        try:
            self.root.iconbitmap('S;GFG2.ico')
        except:
            pass
        self.root.resizable(False, False)
        #-----
        # Поля ввода денег.
        self.entry_mmoney = Entry()
        self.entry_smoney = Entry()
        self.entry_emoney = Entry()
        self.entry_gmoney = Entry()
        self.entry_pmoney = Entry()

        # Ярлыки с выводом денег.
        self.label_mm = LineLabel(self.root)
        self.label_sm = LineLabel(self.root)
        self.label_em = LineLabel(self.root)
        self.label_gm = LineLabel(self.root)
        self.label_pm = LineLabel(self.root)

        # Ярлыки с текстом.
        self.label_tm = LineLabel(self.root, text='медь (мм)')
        self.label_ts = LineLabel(self.root, text='серебро (см)')
        self.label_te = LineLabel(self.root, text='электрум (эм)')
        self.label_tg = LineLabel(self.root, text='золото (зм)')
        self.label_tp = LineLabel(self.root, text='платина (пм)')

        # Поля ввода левого края.
        self.entry_m = Entry()
        self.entry_km = Entry()
        self.entry_sm = Entry()
        self.entry_kg = Entry()

        # Поля ввода правого края.
        self.entry_ft = Entry()
        self.entry_mi = Entry()
        self.entry_in = Entry()
        self.entry_lb = Entry()

        # Кнопки.
        self.reset_money = Button(text='Сброс')
        self.reset_other = Button(text='Сброс')
        self.run_money = Button(text='Посчитать')
        self.left_other = Button(text='Посчитать >')
        self.right_other = Button(text='< Посчитать')

        # Ярлыки с текстом.
        self.text_m = LineLabel(self.root, text='метр (м)')
        self.text_km = LineLabel(self.root, text='километр (км)')
        self.text_sm = LineLabel(self.root, text='сантиметр (см)')
        self.text_kg = LineLabel(self.root, text='килограмм (кг)')

        self.text_ft = LineLabel(self.root, text='фут (ft)')
        self.text_mi = LineLabel(self.root, text='миля (mi)')
        self.text_in = LineLabel(self.root, text='дюйм (in)')
        self.text_lb = LineLabel(self.root, text='фунт (lb)')
        #-----
        # Отрисовка всей этой хуеты сверху.
        # Поля ввода монет.
        self.entry_mmoney.place(x=2, y=2, width=self.size[0], height=18)
        self.entry_smoney.place(x=2, y=2+19, width=self.size[0], height=18)
        self.entry_emoney.place(x=2, y=2+19*2, width=self.size[0], height=18)
        self.entry_gmoney.place(x=2, y=2+19*3, width=self.size[0], height=18)
        self.entry_pmoney.place(x=2, y=2+19*4, width=self.size[0], height=18)

        # Ярлыки вывода монет.
        self.label_mm.place(x=4+self.size[0]+self.size[1]+1, y=2, width=self.size[0], height=18)
        self.label_sm.place(x=4+self.size[0]+self.size[1]+1, y=2+19, width=self.size[0], height=18)
        self.label_em.place(x=4+self.size[0]+self.size[1]+1, y=2+19*2, width=self.size[0], height=18)
        self.label_gm.place(x=4+self.size[0]+self.size[1]+1, y=2+19*3, width=self.size[0], height=18)
        self.label_pm.place(x=4+self.size[0]+self.size[1]+1, y=2+19*4, width=self.size[0], height=18)

        # Ярлыки с текстом.
        self.label_tm.place(x=4+self.size[0], y=2, width=self.size[1], height=18)
        self.label_ts.place(x=4+self.size[0], y=2+19, width=self.size[1], height=18)
        self.label_te.place(x=4+self.size[0], y=2+19*2, width=self.size[1], height=18)
        self.label_tg.place(x=4+self.size[0], y=2+19*3, width=self.size[1], height=18)
        self.label_tp.place(x=4+self.size[0], y=2+19*4, width=self.size[1], height=18)

        # Кнопки.
        self.reset_money.place(x=2, y=2+19*5, width=80, height=18)
        self.run_money.place(x=84, y=2+19*5, width=167, height=18)

        # Поля ввода левого края.
        self.entry_m.place(x=3+self.size[2], y=140, width=self.size[0], height=18)
        self.entry_km.place(x=3+self.size[2], y=140+19, width=self.size[0], height=18)
        self.entry_sm.place(x=3+self.size[2], y=140+19*2, width=self.size[0], height=18)
        self.entry_kg.place(x=3+self.size[2], y=140+19*3, width=self.size[0], height=18)

        # Поля ввода правого края.
        self.entry_ft.place(x=3+self.size[2]+self.size[0], y=140, width=self.size[0], height=18)
        self.entry_mi.place(x=3+self.size[2]+self.size[0], y=140+19, width=self.size[0], height=18)
        self.entry_in.place(x=3+self.size[2]+self.size[0], y=140+19*2, width=self.size[0], height=18)
        self.entry_lb.place(x=3+self.size[2]+self.size[0], y=140+19*3, width=self.size[0], height=18)

        # Ярлыки с текстом.
        self.text_m.place(x=2, y=140, width=self.size[2], height=18)
        self.text_km.place(x=2, y=140+19, width=self.size[2], height=18)
        self.text_sm.place(x=2, y=140+19*2, width=self.size[2], height=18)
        self.text_kg.place(x=2, y=140+19*3, width=self.size[2], height=18)

        self.text_ft.place(x=4+self.size[2]+self.size[0]*2, y=140, width=self.size[2], height=18)
        self.text_mi.place(x=4+self.size[2]+self.size[0]*2, y=140+19, width=self.size[2], height=18)
        self.text_in.place(x=4+self.size[2]+self.size[0]*2, y=140+19*2, width=self.size[2], height=18)
        self.text_lb.place(x=4+self.size[2]+self.size[0]*2, y=140+19*3, width=self.size[2], height=18)

        # Кнопки.
        self.left_other.place(x=82, y=140+19*4, width=90, height=18)
        self.right_other.place(x=174, y=140+19*4, width=90, height=18)
        self.reset_other.place(x=2, y=140+19*4, width=78, height=18)
        #-----

# Отрисовать окно, если запущено отдельно от логики.
# Т.е., считай, предпросмотр.
if __name__ == '__main__':
    ui = Ui_Form()
    # -----Skript-----

    # -----End-----
    ui.root.mainloop()
