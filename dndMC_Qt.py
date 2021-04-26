from PySide2 import QtCore, QtGui, QtWidgets
import sys
from ui_Qt import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

version = 'v0.3_Qt'
windowsize = [378, 315]
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

def run(r):
    if r == 0:
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

ui.reset_money.clicked.connect(lambda x: reset(0))
ui.reset_other.clicked.connect(lambda x: reset(1))
ui.run_money.clicked.connect(lambda x: run(0))
ui.left_other.clicked.connect(lambda x: run(1))
ui.right_other.clicked.connect(lambda x: run(2))

Form.setWindowTitle('DnD Multy Converter '+version)
run(1)

sys.exit(app.exec_())
