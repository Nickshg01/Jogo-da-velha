if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    from PySide6.QtGui import QIcon
    from gui import MainWindow
    from values import ICON

# CRIA E EXECUTA A APLICAÇÃO

    app = QApplication()
    app.setWindowIcon(QIcon(str(ICON)))
    window = MainWindow()
    window.show()
    app.exec()