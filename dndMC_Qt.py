from PySide2 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

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
        ui.entry_ft.setText(str("{0:.2f}".format(float(ui.entry_m.text())*3.28))) #3.28
        ui.entry_mi.setText(str("{0:.2f}".format(float(ui.entry_km.text())*0.62))) #0.62
        ui.entry_in.setText(str("{0:.2f}".format(float(ui.entry_sm.text())*0.39))) #0.39
        ui.entry_lb.setText(str("{0:.2f}".format(float(ui.entry_kg.text())*2.20))) #2.20
    elif r == 2:
        ui.entry_m.setText(str("{0:.2f}".format(float(ui.entry_ft.text())*0.30))) #0.30
        ui.entry_km.setText(str("{0:.2f}".format(float(ui.entry_mi.text())*1.60))) #1.60
        ui.entry_sm.setText(str("{0:.2f}".format(float(ui.entry_in.text())*2.54))) #2.54
        ui.entry_kg.setText(str("{0:.2f}".format(float(ui.entry_lb.text())*0.45))) #0.45
ui.reset_money.clicked.connect(lambda x: reset(0))
ui.reset_other.clicked.connect(lambda x: reset(1))
ui.run_money.clicked.connect(lambda x: run(0))
ui.left_other.clicked.connect(lambda x: run(1))
ui.right_other.clicked.connect(lambda x: run(2))

sys.exit(app.exec_())
