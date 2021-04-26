from tkinter import *
import sys
from ui_Tk import Ui_Form

ui = Ui_Form()

# Кнопка "Сброс"
def clear(tar, text):
    tar.delete('0', 'end')
    tar.insert('0', text)
def reset(r):
    # Сброс монет.
    if r == 0:
        clear(ui.entry_mmoney, '0')
        clear(ui.entry_smoney, '0')
        clear(ui.entry_emoney, '0')
        clear(ui.entry_gmoney, '0')
        clear(ui.entry_pmoney, '0')

        ui.label_mm.label['text'] = '0'
        ui.label_sm.label['text'] = '0'
        ui.label_em.label['text'] = '0'
        ui.label_gm.label['text'] = '0'
        ui.label_pm.label['text'] = '0'
    # Сброс прочего.
    elif r == 1:
        clear(ui.entry_m, '0')
        clear(ui.entry_km, '0')
        clear(ui.entry_sm, '0')
        clear(ui.entry_kg, '0')

        clear(ui.entry_ft, '0')
        clear(ui.entry_mi, '0')
        clear(ui.entry_in, '0')
        clear(ui.entry_lb, '0')

# Подсчёт.
def run(r):
    # Подсчёт монет.
    if r == 0:
        money = 0
        money += float(ui.entry_mmoney.get())
        money += float(ui.entry_smoney.get())*10
        money += float(ui.entry_emoney.get())*50
        money += float(ui.entry_gmoney.get())*100
        money += float(ui.entry_pmoney.get())*1000

        ui.label_mm.label['text'] = str(money)
        ui.label_sm.label['text'] = str(money/10)
        ui.label_em.label['text'] = str(money/50)
        ui.label_gm.label['text'] = str(money/100)
        ui.label_pm.label['text'] = str(money/1000)
    # Подсчёт левой кнопки.
    elif r == 1:
        # Метры в футы.
        clear(ui.entry_ft, str("{0:.2f}".format(float(ui.entry_m.get())*3.28))) #3.28
        # Километры в мили.
        clear(ui.entry_mi, str("{0:.2f}".format(float(ui.entry_km.get())*0.62))) #0.62
        # Сантиметры в люймы.
        clear(ui.entry_in, str("{0:.2f}".format(float(ui.entry_sm.get())*0.39))) #0.39
        # Килограммы в фунты.
        clear(ui.entry_lb, str("{0:.2f}".format(float(ui.entry_kg.get())*2.20))) #2.20
    # Подсчёт правой кнопки.
    elif r == 2:
        # Футы в метры.
        clear(ui.entry_m, str("{0:.2f}".format(float(ui.entry_ft.get())*0.30))) #0.30
        # Мили в километры.
        clear(ui.entry_km, str("{0:.2f}".format(float(ui.entry_mi.get())*1.60))) #1.60
        # Дюймы в сатниметры.
        clear(ui.entry_sm, str("{0:.2f}".format(float(ui.entry_in.get())*2.54))) #2.54
        # Фунты в килограммы.
        clear(ui.entry_kg, str("{0:.2f}".format(float(ui.entry_lb.get())*0.45))) #0.45
        #

# Бинды.
reset(0)
reset(1)
ui.reset_money.bind('<1>', lambda x: reset(0))
ui.reset_other.bind('<1>', lambda x: reset(1))
ui.run_money.bind('<1>', lambda x: run(0))
ui.left_other.bind('<1>', lambda x: run(1))
ui.right_other.bind('<1>', lambda x: run(2))

ui.root.mainloop()
