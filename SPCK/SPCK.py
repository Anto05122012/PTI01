import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import json
import re         

#Đọc dữ liệu từ tệp JSON
with open('./account.json', 'r') as file:
    data_account = json.load(file) 

class LoginPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("PyQT/signin.ui",self)
        self.btn_Login.clicked.connect(self.checkLogin)
        self.btn_Register.clicked.connect(self.register)
    def checkLogin(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        found = False
        for account in data_account:
            if account['email'] == email and account['password'] == password:
                msg_box.setText("Right")
                msg_box.exec()
                MainPage.show()
                self.close()
                found = True
                break

            if not found:
                msg_box.setText("Incorrect email or Password")
                msg_box.exec()
    def register(self):
        RegisterPage.show()
        self.close()
        return

class MainPage(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("PyQT/main.ui",self)

class RegisterPage(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("PyQT/register.ui", self)
        self.btn_Register.clicked.connect(self.checkRegister)
    def checkRegister(self):
        name = self.txtName.text()
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if name == '':
            msg_box.setText('Vui lòng nhập tên.')
            msg_box.exec()
            return
        
        if email == '':
            msg_box.setText('Vui lòng nhập tài khoản.')
            msg_box.exec()
            return
        
        if not re.match(email_regex, email):
            msg_box.setText('Tài khoản chưa nhập đúng định dạng')
            msg_box.exec()
            return

        for account in data_account:
            if email == account['email']:
                msg_box.setText('Tài khoản đã tồn tại')
                msg_box.exec()
                return
            
        if len(password) <8:
            msg_box.setText("Password must be at least 8 character long")
            msg_box.exec()
            return
        
        if not re.search(r"\d", password):
            msg_box.setText("Password must be at least one digit")
            msg_box.exec()
            return
        
        if not re.search(r"[A-Z]", password):
            msg_box.setText("Password must be at least one uppercase letter")
            msg_box.exec()
            return
        
        if not re.search(r"[a-z]", password):
            msg_box.setText("Password must be at least one innercase letter")
            msg_box.exec()
            return
        
        if not re.search(r"[!@#$%^&*()]", password):
            msg_box.setText("Password must be at least one special character long")
            msg_box.exec()
            return
        
        new_account = {
        'email': email,
        "password": password
        }
        data_account.append(new_account)
        with open('account.json', 'w') as json_file:
            json.dump(data_account, json_file, indent=4)
        LoginPage.show()
        self.close()
        
        msg_box.setText('Registeration successful! Welcome, '+ name +'!')
        msg_box.exec()
        MainPage.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    LoginPage = LoginPage()
    RegisterPage = RegisterPage()
    MainPage = MainPage()
    LoginPage.show()
    sys.exit(app.exec())