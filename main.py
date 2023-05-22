import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import subprocess
from googlesearch import search


class SQLMapApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('SQLMap OgKr')
        self.resize(500, 300)

        # Заголовки
        url_label = QLabel('URL:')
        data_label = QLabel('Data:')
        d_label = QLabel('Database:')
        t_label = QLabel('Table:')
        search_label = QLabel('Google Dork:')

        # Поля ввода
        self.url_input = QLineEdit()
        self.data_input = QLineEdit()
        self.d_input = QLineEdit()
        self.t_input = QLineEdit()
        self.search_input = QLineEdit()

        # Флажки
        self.use_auth = QCheckBox('Auth')
        self.use_batch = QCheckBox('Batch')
        self.use_threads = QCheckBox('Threads')
        self.use_dbs = QCheckBox('dbs')
        self.use_level = QCheckBox('level')
        self.use_risk = QCheckBox('risk')
        self.use_dump = QCheckBox('dump')
        self.use_tables = QCheckBox('tables')

        # Кнопки
        scan_button = QPushButton('START')
        scan_button.clicked.connect(self.start_scan)
        scan_button.setStyleSheet('QPushButton {background-color: #4CAF50; color: black; border: 1px solid black; height: 40px; font-size: 25px; font-weight: bold;}'
                                   'QPushButton:hover {background-color: #45a049;}'
                                   'QPushButton:pressed {background-color: #29802f;}')
        search_button = QPushButton('SEARCH')
        search_button.clicked.connect(self.perform_search)
        search_button.setStyleSheet('QPushButton {background-color: #4CAF50; color: black; border: 1px solid black; height: 25px; font-size: 22px; font-weight: bold;}'
                                   'QPushButton:hover {background-color: #45a049;}'
                                   'QPushButton:pressed {background-color: #29802f;}')

        layout = QVBoxLayout()
        layout.setSpacing(1)

        # Расположение элементов
        layout = QVBoxLayout()
        layout.addWidget(url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(data_label)
        layout.addWidget(self.data_input)
        layout.addWidget(d_label)
        layout.addWidget(self.d_input)
        layout.addWidget(t_label)
        layout.addWidget(self.t_input)
        layout.addWidget(search_label)
        layout.addWidget(self.search_input)
        layout.addWidget(search_button)
        layout.addWidget(self.use_threads)
        layout.addWidget(self.use_batch)
        layout.addWidget(self.use_dbs)
        layout.addWidget(self.use_tables)
        layout.addWidget(self.use_dump)
        layout.addWidget(self.use_level)
        layout.addWidget(self.use_risk)
        layout.addWidget(self.use_auth)
        layout.addWidget(scan_button)

        self.setLayout(layout)
        self.setStyleSheet('QWidget {background-color: grey;}'
                           'QLabel {font-weight: bold; color: black; font-size: 20px;}'
                           'QLineEdit {padding: 5px; border: 1px solid black; color: black; font-size: 15px;}'
                           'QCheckBox {padding: 5px; color: black; font-size: 18px;}')

        self.show()

    def start_scan(self):
        url = self.url_input.text()
        data = self.data_input.text()
        database = self.d_input.text()
        table = self.t_input.text()
        auth = self.use_auth.isChecked()
        batch = self.use_batch.isChecked()
        threads = self.use_threads.isChecked()
        dbs = self.use_dbs.isChecked()
        level = self.use_level.isChecked()
        risk = self.use_risk.isChecked()
        dump = self.use_dump.isChecked()
        tables = self.use_tables.isChecked()

        command = ['sqlmap', '-u', url]

        if data:
            command.extend(['--data', data])

        if database:
            command.extend(['-D', database])

        if table:
            command.extend(['-T', table])

        if auth:
            command.append('--auth')

        if batch:
            command.append('--batch')

        if threads:
            command.append('--threads=10')

        if dbs:
            command.append('--dbs')

        if level:
            command.append('--level=3')

        if risk:
            command.append('--risk=3')

        if dump:
            command.append('--dump')

        if tables:
            command.append('--tables')

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Error: {e.returncode}')

    def perform_search(self):
        search_query = self.search_input.text()
        results = search(search_query, num_results=5)

        with open("search_results.txt", "w") as f:
            for result in results:
                f.write(result + "\n")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sqlmap_app = SQLMapApp()
    sys.exit(app.exec_())
