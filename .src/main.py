if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    from gui import MainWindow

# CRIA E EXECUTA A APLICAÇÃO

    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()