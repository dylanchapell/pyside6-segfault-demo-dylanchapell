from PySide6 import QtCore

class Bad(QtCore.QObject):
    @QtCore.Slot(result=QtCore.QObject)
    def bad_fn(self):
        mytuple = ("onething","twothing")
        return mytuple
