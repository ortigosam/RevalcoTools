from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QMessageBox
)

from PySide6.QtCore import Qt

from processor import procesar_excel


class DropArea(QLabel):

    def __init__(self, window):

        super().__init__()

        self.window = window

        self.setText(
            "📄\n\nArrastra aquí el Excel de stock"
        )

        self.setAlignment(Qt.AlignCenter)

        self.setAcceptDrops(True)

        self.setStyleSheet("""
        QLabel {
            border: 3px dashed #888;
            border-radius: 15px;
            font-size: 20px;
            padding: 50px;
        }
        """)


    def dragEnterEvent(self, event):

        if event.mimeData().hasUrls():
            event.acceptProposedAction()


    def dropEvent(self, event):

        archivo = (
            event.mimeData()
            .urls()[0]
            .toLocalFile()
        )

        self.window.procesar(archivo)



class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Procesador de pedidos"
        )

        self.resize(600,400)


        layout = QVBoxLayout()


        self.drop = DropArea(self)

        layout.addWidget(self.drop)


        self.setLayout(layout)



    def procesar(self, archivo):

        try:

            self.drop.setText(
                "⏳ Procesando..."
            )

            salida, resumen = procesar_excel(
                archivo
            )

            self.drop.setText(
                f"""✅ Automatizacion completada con exito.

📦 PEDIR: {resumen['PEDIR']}
❌ NO PEDIR: {resumen['NO PEDIR']}
🔍 REVISAR SI PEDIR: {resumen['REVISAR SI PEDIR']}
⚠️ DATOS INCOMPLETOS: {resumen['DATOS INCOMPLETOS']}

El archivo ha sido generado:
{salida}"""
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

            self.drop.setText(
                "❌ Error"
            )