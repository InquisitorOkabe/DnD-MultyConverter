# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui',
# licensing of 'untitled.ui' applies.
#
# Created: Sun Apr 25 03:08:21 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(378, 315)
        Form.setMinimumSize(QtCore.QSize(378, 315))
        Form.setMaximumSize(QtCore.QSize(378, 315))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("S;GFG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 261, 161))
        self.groupBox.setObjectName("groupBox")
        self.entry_mmoney = QtWidgets.QLineEdit(self.groupBox)
        self.entry_mmoney.setGeometry(QtCore.QRect(10, 20, 80, 20))
        self.entry_mmoney.setObjectName("entry_mmoney")
        self.entry_smoney = QtWidgets.QLineEdit(self.groupBox)
        self.entry_smoney.setGeometry(QtCore.QRect(10, 41, 80, 20))
        self.entry_smoney.setObjectName("entry_smoney")
        self.entry_emoney = QtWidgets.QLineEdit(self.groupBox)
        self.entry_emoney.setGeometry(QtCore.QRect(10, 62, 80, 20))
        self.entry_emoney.setObjectName("entry_emoney")
        self.entry_gmoney = QtWidgets.QLineEdit(self.groupBox)
        self.entry_gmoney.setGeometry(QtCore.QRect(10, 83, 80, 20))
        self.entry_gmoney.setObjectName("entry_gmoney")
        self.entry_pmoney = QtWidgets.QLineEdit(self.groupBox)
        self.entry_pmoney.setGeometry(QtCore.QRect(10, 104, 80, 20))
        self.entry_pmoney.setObjectName("entry_pmoney")
        self.label_mm = QtWidgets.QLabel(self.groupBox)
        self.label_mm.setGeometry(QtCore.QRect(172, 20, 80, 20))
        self.label_mm.setFrameShape(QtWidgets.QFrame.Box)
        self.label_mm.setObjectName("label_mm")
        self.label_sm = QtWidgets.QLabel(self.groupBox)
        self.label_sm.setGeometry(QtCore.QRect(172, 41, 80, 20))
        self.label_sm.setFrameShape(QtWidgets.QFrame.Box)
        self.label_sm.setObjectName("label_sm")
        self.label_em = QtWidgets.QLabel(self.groupBox)
        self.label_em.setGeometry(QtCore.QRect(172, 62, 80, 20))
        self.label_em.setFrameShape(QtWidgets.QFrame.Box)
        self.label_em.setObjectName("label_em")
        self.label_gm = QtWidgets.QLabel(self.groupBox)
        self.label_gm.setGeometry(QtCore.QRect(172, 83, 80, 20))
        self.label_gm.setFrameShape(QtWidgets.QFrame.Box)
        self.label_gm.setObjectName("label_gm")
        self.label_pm = QtWidgets.QLabel(self.groupBox)
        self.label_pm.setGeometry(QtCore.QRect(172, 104, 80, 20))
        self.label_pm.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pm.setObjectName("label_pm")
        self.run_money = QtWidgets.QPushButton(self.groupBox)
        self.run_money.setGeometry(QtCore.QRect(95, 130, 75, 23))
        self.run_money.setObjectName("run_money")
        self.reset_money = QtWidgets.QPushButton(self.groupBox)
        self.reset_money.setGeometry(QtCore.QRect(10, 130, 23, 23))
        self.reset_money.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_money.setIcon(icon1)
        self.reset_money.setObjectName("reset_money")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(91, 41, 80, 20))
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(91, 104, 80, 20))
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(91, 20, 80, 20))
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(91, 83, 80, 20))
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(91, 62, 80, 20))
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 170, 341, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.entry_km = QtWidgets.QLineEdit(self.groupBox_2)
        self.entry_km.setGeometry(QtCore.QRect(91, 40, 80, 20))
        self.entry_km.setObjectName("entry_km")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 40, 80, 20))
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.entry_mi = QtWidgets.QLineEdit(self.groupBox_2)
        self.entry_mi.setGeometry(QtCore.QRect(172, 40, 80, 20))
        self.entry_mi.setObjectName("entry_mi")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(253, 40, 80, 20))
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.entry_sm = QtWidgets.QLineEdit(self.groupBox_2)
        self.entry_sm.setGeometry(QtCore.QRect(91, 61, 80, 20))
        self.entry_sm.setObjectName("entry_sm")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(253, 61, 80, 20))
        self.label_16.setFrameShape(QtWidgets.QFrame.Box)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.entry_in = QtWidgets.QLineEdit(self.groupBox_2)
        self.entry_in.setGeometry(QtCore.QRect(172, 61, 80, 20))
        self.entry_in.setObjectName("entry_in")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(10, 61, 80, 20))
        self.label_17.setFrameShape(QtWidgets.QFrame.Box)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.entry_kg = QtWidgets.QLineEdit(self.groupBox_2)
        self.entry_kg.setGeometry(QtCore.QRect(91, 82, 80, 20))
        self.entry_kg.setObjectName("entry_kg")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(253, 82, 80, 20))
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.entry_lb = QtWidgets.QLineEdit(self.groupBox_2)
        self.entry_lb.setGeometry(QtCore.QRect(172, 82, 80, 20))
        self.entry_lb.setObjectName("entry_lb")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(10, 82, 80, 20))
        self.label_19.setFrameShape(QtWidgets.QFrame.Box)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.reset_other = QtWidgets.QPushButton(self.groupBox_2)
        self.reset_other.setGeometry(QtCore.QRect(10, 110, 23, 23))
        self.reset_other.setText("")
        self.reset_other.setIcon(icon1)
        self.reset_other.setObjectName("reset_other")
        self.left_other = QtWidgets.QPushButton(self.groupBox_2)
        self.left_other.setGeometry(QtCore.QRect(94, 110, 75, 23))
        self.left_other.setObjectName("left_other")
        self.right_other = QtWidgets.QPushButton(self.groupBox_2)
        self.right_other.setGeometry(QtCore.QRect(175, 110, 75, 23))
        self.right_other.setObjectName("right_other")
        self.entry_m = QtWidgets.QLineEdit(self.groupBox_2)
        self.entry_m.setGeometry(QtCore.QRect(91, 19, 80, 20))
        self.entry_m.setObjectName("entry_m")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(253, 19, 80, 20))
        self.label_20.setFrameShape(QtWidgets.QFrame.Box)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.entry_ft = QtWidgets.QLineEdit(self.groupBox_2)
        self.entry_ft.setGeometry(QtCore.QRect(172, 19, 80, 20))
        self.entry_ft.setObjectName("entry_ft")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(10, 19, 80, 20))
        self.label_21.setFrameShape(QtWidgets.QFrame.Box)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "DnD Multy Converter", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Form", "Монеты", None, -1))
        self.entry_mmoney.setText(QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.entry_smoney.setText(QtWidgets.QApplication.translate("Form", "10", None, -1))
        self.entry_emoney.setText(QtWidgets.QApplication.translate("Form", "50", None, -1))
        self.entry_gmoney.setText(QtWidgets.QApplication.translate("Form", "100", None, -1))
        self.entry_pmoney.setText(QtWidgets.QApplication.translate("Form", "1000", None, -1))
        self.label_mm.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.label_sm.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.label_em.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.label_gm.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.label_pm.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.run_money.setText(QtWidgets.QApplication.translate("Form", "Посчитать", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "серебро (см)", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Form", "платина (пм)", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Form", "медь (мм)", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Form", "золото (зм)", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Form", "электрум (эм)", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Form", "Прочее", None, -1))
        self.entry_km.setText(QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Form", "(км) километр", None, -1))
        self.entry_mi.setText(QtWidgets.QApplication.translate("Form", "0.62", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("Form", "миля (mi)", None, -1))
        self.entry_sm.setText(QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("Form", "дюйм (in)", None, -1))
        self.entry_in.setText(QtWidgets.QApplication.translate("Form", "0.39", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Form", "(см) сантиметр", None, -1))
        self.entry_kg.setText(QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("Form", "фунт (lb)", None, -1))
        self.entry_lb.setText(QtWidgets.QApplication.translate("Form", "2.20", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("Form", "(кг) килограмм", None, -1))
        self.left_other.setText(QtWidgets.QApplication.translate("Form", "Посчитать >", None, -1))
        self.right_other.setText(QtWidgets.QApplication.translate("Form", "< Посчитать", None, -1))
        self.entry_m.setText(QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.label_20.setText(QtWidgets.QApplication.translate("Form", "фут (ft)", None, -1))
        self.entry_ft.setText(QtWidgets.QApplication.translate("Form", "3.28", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("Form", "(м) метр", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
