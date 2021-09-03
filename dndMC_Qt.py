import sys, os

scriptdir, script = os.path.split(__file__)
installdir = scriptdir  # for compatibility with commands
pkgdir = os.path.join(scriptdir, 'pkgs')
sys.path.insert(0, pkgdir)

from PySide2 import QtCore, QtGui, QtWidgets
from ui_Qt import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

ui.mode_switcher.setEnabled(0) # Функция пока недоступна
version = 'v0.6_Qt'
c2 = {
      # Множители: Фут = метров, метр = футов
     'ft_m':[0.3048, 3.28083989501],
     'mi_km':[1.609344, 0.62137119224],
     'in_sm':[0.3937007874, 2.54],
     'lb_kg':[0.37324, 2.67923]
}

# print('Фут = '+str(c2['ft_m'][0])+' метров')
# print('Метр = '+str(c2['ft_m'][1])+' футов')
# print('Миля = '+str(c2['mi_km'][0])+' километров')
# print('Километр = '+str(c2['mi_km'][1])+' миль')
# print('Дюйм = '+str(c2['in_sm'][0])+' сантиметров')
# print('Сантиметр = '+str(c2['in_sm'][1])+' дюймов')
# print('Фунт = '+str(c2['lb_kg'][0])+' килограммов')
# print('Килогрмм = '+str(c2['lb_kg'][1])+' фунтов')

def mode():
    # 0/True - Нет галочки
    # 1/False - Есть галочка
    if ui.mode_switcher.isTristate() == 0:
        # Включить сдачу
        ui.mode_switcher.setTristate(y=1)
        ui.trader_mm.setEnabled(0)
        ui.trader_sm.setEnabled(0)
        ui.trader_em.setEnabled(0)
        ui.trader_gm.setEnabled(0)
        ui.trader_pm.setEnabled(0)

        ui.trader_mm.setText('0')
        ui.trader_sm.setText('0')
        ui.trader_em.setText('0')
        ui.trader_gm.setText('0')
        ui.trader_pm.setText('0')
    else:
        # Выключить сдачу
        ui.mode_switcher.setTristate(y=0)
        ui.trader_mm.setEnabled(1)
        ui.trader_sm.setEnabled(1)
        ui.trader_em.setEnabled(1)
        ui.trader_gm.setEnabled(1)
        ui.trader_pm.setEnabled(1)

def reset(r):
    if r == 0:
        ui.entry_mmoney.setText('0')
        ui.entry_smoney.setText('0')
        ui.entry_emoney.setText('0')
        ui.entry_gmoney.setText('0')
        ui.entry_pmoney.setText('0')

        ui.label_mm.setText('0')
        ui.label_sm.setText('0')
        ui.label_em.setText('0')
        ui.label_gm.setText('0')
        ui.label_pm.setText('0')
    elif r == 1:
        ui.entry_m.setText('0')
        ui.entry_km.setText('0')
        ui.entry_sm.setText('0')
        ui.entry_kg.setText('0')

        ui.entry_ft.setText('0')
        ui.entry_mi.setText('0')
        ui.entry_in.setText('0')
        ui.entry_lb.setText('0')

def clearint():
    t1 = int(ui.entry_mmoney.text())
    t2 = int(ui.entry_smoney.text())
    t3 = int(ui.entry_emoney.text())
    t4 = int(ui.entry_gmoney.text())
    t5 = int(ui.entry_pmoney.text())
    ui.entry_mmoney.setText(str(t1))
    ui.entry_smoney.setText(str(t2))
    ui.entry_emoney.setText(str(t3))
    ui.entry_gmoney.setText(str(t4))
    ui.entry_pmoney.setText(str(t5))
def run(r):
    if r == 0:
        clearint()
        money = 0
        money += float(ui.entry_mmoney.text())
        money += float(ui.entry_smoney.text())*10
        money += float(ui.entry_emoney.text())*50
        money += float(ui.entry_gmoney.text())*100
        money += float(ui.entry_pmoney.text())*1000

        ui.label_mm.setText(str(money))
        ui.label_sm.setText(str(money/10))
        ui.label_em.setText(str(money/50))
        ui.label_gm.setText(str(money/100))
        ui.label_pm.setText(str(money/1000))
    elif r == 1:
        ui.entry_ft.setText(str("{0:.2f}".format(float(ui.entry_m.text())*c2['ft_m'][1]))) #3.28
        ui.entry_mi.setText(str("{0:.2f}".format(float(ui.entry_km.text())*c2['mi_km'][1]))) #0.62
        ui.entry_in.setText(str("{0:.2f}".format(float(ui.entry_sm.text())*c2['in_sm'][1]))) #0.39
        ui.entry_lb.setText(str("{0:.2f}".format(float(ui.entry_kg.text())*c2['lb_kg'][1]))) #2.20
    elif r == 2:
        ui.entry_m.setText(str("{0:.2f}".format(float(ui.entry_ft.text())*c2['ft_m'][0]))) #0.30
        ui.entry_km.setText(str("{0:.2f}".format(float(ui.entry_mi.text())*c2['mi_km'][0]))) #1.60
        ui.entry_sm.setText(str("{0:.2f}".format(float(ui.entry_in.text())*c2['in_sm'][0]))) #2.54
        ui.entry_kg.setText(str("{0:.2f}".format(float(ui.entry_lb.text())*c2['lb_kg'][0]))) #0.45
    elif r == 3:
        trader = []
        ui.trader.append(ui.trader_mm.text())
        ui.trader.append(ui.trader_sm.text())
        ui.trader.append(ui.trader_gm.text())
        ui.trader.append(ui.trader_em.text())
        ui.trader.append(ui.trader_pm.text())
        money = 0
        money += float(ui.entry_mmoney.text())
        money += float(ui.entry_smoney.text())*10
        money += float(ui.entry_emoney.text())*50
        money += float(ui.entry_gmoney.text())*100
        money += float(ui.entry_pmoney.text())*1000

        ui.label_mm.setText(str(money))
        ui.label_sm.setText(str(money/10))
        ui.label_em.setText(str(money/50))
        ui.label_gm.setText(str(money/100))
        ui.label_pm.setText(str(money/1000))

ui.reset_money.clicked.connect(lambda x: reset(0))
ui.reset_other.clicked.connect(lambda x: reset(1))
ui.run_money.clicked.connect(lambda x: run(3) if ui.mode_switcher.isTristate() == 0 else run(0))
ui.left_other.clicked.connect(lambda x: run(1))
ui.right_other.clicked.connect(lambda x: run(2))
ui.mode_switcher.stateChanged.connect(lambda x: mode())

Form.setWindowTitle('DnD Multy Converter '+version)
run(1)

sys.exit(app.exec_())
