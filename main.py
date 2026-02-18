import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget, 
                               QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QTextEdit, QLabel, 
                               QLineEdit, QMessageBox)
from PySide6.QtCore import Qt

from generators import NoteGenerator, MultipleOfThreeGenerator
from email_validator import EmailValidator

#И всем привет, дорогие друзья!
#Сегодня я покажу вам, как сделать небольшой проект по Теории алгоритмов буквально за несколько минут
#Начнём с простого
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генераторы нот, чисел и валидатор email")
        self.setGeometry(100, 100, 700, 500)
        
        # Создаем генераторы и валидатор
        self.note_generator = NoteGenerator()
        self.number_generator = MultipleOfThreeGenerator()
        self.email_validator = EmailValidator()
        
        # Создаем вкладки
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        
        # Вкладка для генератора нот
        self.notes_tab = QWidget()
        self.setup_notes_tab()
        self.tab_widget.addTab(self.notes_tab, "Генератор нот")
        
        # Вкладка для генератора чисел
        self.numbers_tab = QWidget()
        self.setup_numbers_tab()
        self.tab_widget.addTab(self.numbers_tab, "Генератор чисел")
        
        # Вкладка для валидатора email
        self.email_tab = QWidget()
        self.setup_email_tab()
        self.tab_widget.addTab(self.email_tab, "Валидатор email")
    
    def setup_notes_tab(self):
        """Настройка вкладки генератора нот"""
        layout = QVBoxLayout()
        
        # Описание
        description = QLabel(
            "Генератор случайных нот. Генерирует 1 000 000 нот и показывает первые 20.\n"
            "Список нот: до, ре, ми, фа, соль, ля, си"
        )
        description.setWordWrap(True)
        layout.addWidget(description)
        
        # Кнопка генерации
        self.notes_button = QPushButton("Сгенерировать ноты")
        self.notes_button.clicked.connect(self.generate_notes)
        layout.addWidget(self.notes_button)
        
        # Поле для вывода результатов
        self.notes_output = QTextEdit()
        self.notes_output.setReadOnly(True)
        layout.addWidget(self.notes_output)
        
        self.notes_tab.setLayout(layout)
    
    def setup_numbers_tab(self):
        """Настройка вкладки генератора чисел"""
        layout = QVBoxLayout()
        
        # Описание
        description = QLabel(
            "Генератор чисел, кратных 3. Начинает с заданного значения и показывает первые 20 чисел."
        )
        description.setWordWrap(True)
        layout.addWidget(description)
        
        # Поле для ввода начального значения
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Начальное значение (a):"))
        self.number_input = QLineEdit()
        self.number_input.setText("-100")
        input_layout.addWidget(self.number_input)
        input_layout.addStretch()
        layout.addLayout(input_layout)
        
        # Кнопка генерации
        self.numbers_button = QPushButton("Сгенерировать числа")
        self.numbers_button.clicked.connect(self.generate_numbers)
        layout.addWidget(self.numbers_button)
        
        # Поле для вывода результатов
        self.numbers_output = QTextEdit()
        self.numbers_output.setReadOnly(True)
        layout.addWidget(self.numbers_output)
        
        self.numbers_tab.setLayout(layout)
    
    def setup_email_tab(self):
        """Настройка вкладки валидатора email"""
        layout = QVBoxLayout()
        
        # Описание
        description = QLabel(
            "Валидатор email-адресов. Введите адреса через пробел.\n"
            "Критерии валидности:\n"
            "- Используются только латинские буквы, цифры и символ подчеркивания\n"
            "- Обязательно присутствует символ @\n"
            "- После @ должна быть точка\n"
            "- Между @ и точкой должны быть другие символы"
        )
        description.setWordWrap(True)
        layout.addWidget(description)
        
        # Поле для ввода email
        input_layout = QVBoxLayout()
        input_layout.addWidget(QLabel("Введите email-адреса через пробел:"))
        self.email_input = QTextEdit()
        self.email_input.setMaximumHeight(100)
        self.email_input.setPlaceholderText("example@test.com test@domain.org invalid-email")
        input_layout.addWidget(self.email_input)
        layout.addLayout(input_layout)
        
        # Кнопка валидации
        self.email_button = QPushButton("Проверить email-адреса")
        self.email_button.clicked.connect(self.validate_emails)
        layout.addWidget(self.email_button)
        
        # Поле для вывода результатов
        self.email_output = QTextEdit()
        self.email_output.setReadOnly(True)
        layout.addWidget(self.email_output)
        
        self.email_tab.setLayout(layout)
    
    def generate_notes(self):
        """Обработчик генерации нот"""
        try:
            # Генерируем ноты
            generator = self.note_generator.generate_notes()
            
            # Получаем первые 20 нот
            first_20_notes = []
            for i, note in enumerate(generator):
                if i >= 20:
                    break
                first_20_notes.append(note)
            
            # Выводим результат
            result = "Первые 20 сгенерированных нот:\n\n"
            result += ", ".join(first_20_notes)
            self.notes_output.setText(result)
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")
    
    def generate_numbers(self):
        """Обработчик генерации чисел"""
        try:
            # Получаем начальное значение
            a_text = self.number_input.text()
            if not a_text:
                QMessageBox.warning(self, "Предупреждение", "Введите начальное значение")
                return
            
            a = int(a_text)
            
            # Генерируем числа
            generator = self.number_generator.generate_multiples(a)
            
            # Получаем первые 20 чисел
            first_20_numbers = []
            for i in range(20):
                first_20_numbers.append(str(next(generator)))
            
            # Выводим результат
            result = f"Первые 20 чисел, кратных 3, начиная с {a}:\n\n"
            result += ", ".join(first_20_numbers)
            self.numbers_output.setText(result)
            
        except ValueError:
            QMessageBox.warning(self, "Ошибка ввода", "Введите корректное целое число")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")
    
    def validate_emails(self):
        """Обработчик валидации email-адресов"""
        try:
            # Получаем введенные email
            emails_text = self.email_input.toPlainText()
            if not emails_text.strip():
                QMessageBox.warning(self, "Предупреждение", "Введите email-адреса")
                return
            
            # Фильтруем валидные email
            valid_emails = self.email_validator.filter_valid_emails(emails_text)
            
            # Выводим результат
            if valid_emails:
                result = f"Найдено {len(valid_emails)} корректных email-адресов:\n\n"
                result += "\n".join(valid_emails)
            else:
                result = "Корректные email-адреса не найдены."
            
            self.email_output.setText(result)
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
