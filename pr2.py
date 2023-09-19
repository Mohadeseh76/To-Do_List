import sys
import pickle
import random
from enum import Enum
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QDateEdit, QFrame
from PyQt5.QtGui import QPalette, QColor, QFont, QPixmap, QIcon  # اضافه کردن QIcon
from PyQt5.QtCore import QDate
import datetime

class TaskStatus(Enum):
    TODO = "To-Do"
    DOING = "Doing.."
    DONE = "Done!"

class KanbanBoardApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 800, 600)

        # اضافه کردن آیکون به برنامه
        app_icon = QIcon("C:\\Users\\MOHADESEH\\Desktop\\pr2\\mm.png")  # مسیر تا فایل آیکون
        self.setWindowIcon(app_icon)

        # تنظیم رنگ بک‌گراند برنامه
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(32, 178, 170))  # رنگ زمینه برنامه
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))  # رنگ متن
        self.setPalette(palette)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()  # تغییر به QHBoxLayout برای المان‌ها در یک خط
        self.central_widget.setLayout(self.layout)

        # اضافه کردن باکس ورودی به بالای پنجره
        self.top_frame = QFrame()
        self.top_frame_layout = QVBoxLayout()  # ایجاد یک QVBoxLayout برای top_frame
        self.top_frame.setLayout(self.top_frame_layout)  # تنظیم لایه top_frame به عنوان QVBoxLayout

        self.layout.addWidget(self.top_frame)

        self.status_frames = {}

        for status in TaskStatus:
            status_frame = QFrame()
            status_frame_layout = QVBoxLayout(status_frame)

            label = QLabel(status.value)

            # تنظیم فونت متن باکس‌های وضعیت به اندازه بزرگ‌تر
            font = QFont()
            font.setPointSize(18)
            label.setFont(font)

            label.setStyleSheet("font-weight: bold;")
            status_frame_layout.addWidget(label)

            list_widget = QListWidget()

            # تنظیم اندازه متن‌های اضافه شده به لیست به 20 پیکسل
            list_widget.setFont(font)

            if status == TaskStatus.TODO:
                list_widget.setStyleSheet("font-size: 18px; font-weight: bold; background-color: lightblue;")
            elif status == TaskStatus.DOING:
                list_widget.setStyleSheet("font-size: 18px; font-weight: bold; background-color: #FFEC8B;")
            elif status == TaskStatus.DONE:
                list_widget.setStyleSheet("font-size: 18px; font-weight: bold; background-color: lightgreen;")
            
            status_frame_layout.addWidget(list_widget)

            self.status_frames[status] = status_frame
            self.layout.addWidget(status_frame)

        self.entry = QLineEdit()
        self.entry.setPlaceholderText("Enter task")

        font = QFont()
        font.setPointSize(18)
        self.entry.setFont(font)

        self.entry.setStyleSheet("padding: 5px; margin-top: 10px;")
        self.top_frame_layout.addWidget(self.entry)  # افزودن باکس ورودی به top_frame_layout به جای self.layout

        # تنظیم تاریخ ابتدایی برابر با تاریخ کامپیوتری
        current_date = datetime.datetime.now()
        self.date_edit = QDateEdit(QDate(current_date.year, current_date.month, current_date.day))
        self.date_edit.setCalendarPopup(True)

        date_font = QFont()
        date_font.setPointSize(14)
        self.date_edit.setFont(date_font)

        self.date_edit.setStyleSheet("font-size: 16px; padding: 5px; margin-top: 10px;")
        self.top_frame_layout.addWidget(self.date_edit)

        # تصویر مورد نظر را بخوانید
        image_paths = [
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\1_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\2_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\3_11zon.png',  # مسیر تصویر دوم را اضافه کنید
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\4_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\5_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\6_11zon.png', 
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\7_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\8_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\9_11zon.png', 
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\10_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\11_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\12_11zon.png', 
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\13_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\14_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\15_11zon.png', 
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\16_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\17_11zon.png',
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\18_11zon.png',  
            'C:\\Users\\MOHADESEH\\Desktop\pr2\\images\\19_11zon.png',                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   # ادامه مسیرهای تصاویر دیگر
        ]

        random_image_path = random.choice(image_paths)

        pixmap = QPixmap(random_image_path)

        # تغییر اندازه تصویر به 200x200 پیکسل
        pixmap = pixmap.scaled(500, 400)

        image_label = QLabel()
        image_label.setPixmap(pixmap)

        image_label.setFixedSize(pixmap.width(), pixmap.height())

        self.top_frame_layout.addWidget(image_label)


        button_layout = QVBoxLayout()

        button_info = [
            ("Add Task", self.add_task),
            ("Clear Selected", self.clear_selected),
            ("Move to Doing", self.move_item),
            ("Move to Done", self.move_item),
            ("SAVE", self.save_data),
            ("Reset", self.reset_data)
        ]

        for text, func in button_info:
            button = QPushButton(text)
            button.clicked.connect(func)

            button.setFont(font)

            button.setStyleSheet("font-size: 16px; padding: 10px; margin-top: 10px;")
            button_layout.addWidget(button)

        self.layout.addLayout(button_layout)

        self.load_data()

        new_day_label = QLabel("Today is a new day ;)")
        new_day_font = QFont()
        new_day_font.setPointSize(24)
        new_day_label.setFont(new_day_font)
        new_day_label.setStyleSheet("font-weight: bold; margin: 20px;")
        self.top_frame_layout.addWidget(new_day_label)

    def add_task(self):
        task = self.entry.text()
        date = self.date_edit.date().toString()
        if task:
            selected_listbox = self.status_frames[TaskStatus.TODO].layout().itemAt(1).widget()
            selected_listbox.addItem(f"{task} ({date})")
            self.entry.clear()

    def clear_selected(self):
        for status in TaskStatus:
            selected_items = self.status_frames[status].layout().itemAt(1).widget().selectedItems()
            for item in selected_items:
                self.status_frames[status].layout().itemAt(1).widget().takeItem(self.status_frames[status].layout().itemAt(1).widget().row(item))

    def move_item(self):
        sender = self.sender()
        if sender is None:
            return

        target_status = TaskStatus.DOING if sender.text() == "Move to Doing" else TaskStatus.DONE
        source_status = TaskStatus.TODO if target_status == TaskStatus.DOING else TaskStatus.DOING

        selected_items = self.status_frames[source_status].layout().itemAt(1).widget().selectedItems()
        for item in selected_items:
            self.status_frames[source_status].layout().itemAt(1).widget().takeItem(self.status_frames[source_status].layout().itemAt(1).widget().row(item))
            self.status_frames[target_status].layout().itemAt(1).widget().addItem(item.text())

    def save_data(self):
        data = {status: [] for status in TaskStatus}
        for status in TaskStatus:
            listbox = self.status_frames[status].layout().itemAt(1).widget()
            data[status] = [listbox.item(i).text() for i in range(listbox.count())]

        with open('kanban_data.pkl', 'wb') as f:
            pickle.dump(data, f)

    def load_data(self):
        try:
            with open('kanban_data.pkl', 'rb') as f:
                data = pickle.load(f)

            for status in TaskStatus:
                listbox = self.status_frames[status].layout().itemAt(1).widget()
                listbox.addItems(data.get(status, []))
        except FileNotFoundError:
            pass

    def reset_data(self):
        for status in TaskStatus:
            listbox = self.status_frames[status].layout().itemAt(1).widget()
            listbox.clear()
        self.entry.clear()
        current_date = datetime.datetime.now()
        self.date_edit.setDate(QDate(current_date.year, current_date.month, current_date.day))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kanban_app = KanbanBoardApp()
    
    kanban_app.resize(1700, 900)
    
    kanban_app.show()
    sys.exit(app.exec_())
