from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from Bad import Bad

if __name__ == "__main__":
    bad = Bad()
    app = QGuiApplication()
    engine = QQmlApplicationEngine()
    qml_file = "main.qml"
    context = engine.rootContext()
    context.setContextProperty("bad",bad)
    engine.load(qml_file)

    app.exec()
