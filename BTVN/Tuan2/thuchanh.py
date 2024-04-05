import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class BookManagementApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()

        label_title = QLabel('Quản lý Sách và Tài Liệu Tham Khảo')
        layout.addWidget(label_title)

        self.input_book_title = QLineEdit()
        self.input_book_author = QLineEdit()
        self.input_book_publisher = QLineEdit()

        layout.addWidget(QLabel('Tiêu đề sách:'))
        layout.addWidget(self.input_book_title)
        layout.addWidget(QLabel('Tác giả:'))
        layout.addWidget(self.input_book_author)
        layout.addWidget(QLabel('Nhà xuất bản:'))
        layout.addWidget(self.input_book_publisher)

        btn_add_book = QPushButton('Thêm Sách')
        btn_add_book.clicked.connect(self.addBook)
        layout.addWidget(btn_add_book)

        self.setLayout(layout)
        self.setWindowTitle('Ứng dụng Quản lý Sách và Tài Liệu Tham Khảo')
        self.show()

    def addBook(self):

        book_title = self.input_book_title.text()
        book_author = self.input_book_author.text()
        book_publisher = self.input_book_publisher.text()

        print(f'Sách đã thêm vào danh sách: {book_title} - {book_author} ({book_publisher})')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BookManagementApp()
    sys.exit(app.exec_())
