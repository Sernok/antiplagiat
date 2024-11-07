from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDoubleSpinBox, QPlainTextEdit, QPushButton, QLabel, QHBoxLayout
import sys


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Антиплагиат v0.0001")

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Threshold setting (QDoubleSpinBox)
        self.alert_value = QDoubleSpinBox()
        self.alert_value.setRange(0, 100)
        self.alert_value.setValue(50.0)
        self.alert_value.setSuffix(" %")
        main_layout.addWidget(QLabel("Порог срабатывания (%)"))
        main_layout.addWidget(self.alert_value)

        # Text areas
        self.text1 = QPlainTextEdit()
        self.text1.setPlaceholderText("Текст 1")
        self.text2 = QPlainTextEdit()
        self.text2.setPlaceholderText("Текст 2")

        text_layout = QHBoxLayout()
        text_layout.addWidget(self.text1)
        text_layout.addWidget(self.text2)
        main_layout.addLayout(text_layout)

        # Result label
        self.result_label = QLabel("Результат появится здесь")
        main_layout.addWidget(self.result_label)

        # Check button
        self.checkBtn = QPushButton("Сравнить")
        self.checkBtn.clicked.connect(self.check_plagiarism)
        main_layout.addWidget(self.checkBtn)

    def check_plagiarism(self):
        # Get unique lines from both texts
        text1_lines = set(self.text1.toPlainText().splitlines())
        text2_lines = set(self.text2.toPlainText().splitlines())

        # Calculate similarity
        common_lines = text1_lines.intersection(text2_lines)
        total_unique_lines = text1_lines.union(text2_lines)

        if total_unique_lines:
            similarity_percentage = (len(common_lines) / len(total_unique_lines)) * 100
        else:
            similarity_percentage = 0.0

        # Display the result
        similarity_text = f"Тексты похожи на {similarity_percentage:.2f}%, "
        similarity_text += "плагиат" if similarity_percentage >= self.alert_value.value() else "не плагиат"
        self.result_label.setText(similarity_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AntiPlagiarism()
    window.show()
    sys.exit(app.exec_())

