import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
from analizador_lexico import prueba
from analizador_sintactico import prueba_sintactica

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interfaz.ui", self)
        self.home.pb_lexico.clicked.connect(self.ev_lexico)
        self.home.pb_sintactico.clicked.connect(self.ev_sintactico)
        self.home.pb_archivo.clicked.connect(self.ev_archivo)
        self.home.pb_limpiar.clicked.connect(self.ev_limpiar)

    def ev_lexico(self):
        '''Manejo de analisis lexico'''
        self.home.tx_lexico.setText('')
        datos = self.home.tx_ingreso.toPlainText().strip()
        resultado_lexico = prueba(datos)
        cadena = ''
        for lex in resultado_lexico:
            cadena += lex + "\n"
        self.home.tx_lexico.setText(cadena)

    def ev_sintactico(self):
        '''Manejo de analisis gramatico'''
        self.home.tx_sintactico.setText('')
        datos = self.home.tx_ingreso.toPlainText().strip()
        resultado_sintactico = prueba_sintactica(datos)
        cadena = ''
        for item in resultado_sintactico:
            cadena += item + "\n"
        self.home.tx_sintactico.setText(cadena)

    def ev_archivo(self):
        '''Manejo de subir archivo'''
        dlg = QFileDialog()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read().strip()
                if data:
                    self.home.tx_ingreso.setText(data + "\n")

    def ev_limpiar(self):
        '''Manejo de limpieza de campos'''
        self.home.tx_ingreso.setText('')
        self.home.tx_lexico.setText('')
        self.home.tx_sintactico.setText('')

def iniciar():
    app = QApplication(sys.argv)
    ventana = Main()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    iniciar()
