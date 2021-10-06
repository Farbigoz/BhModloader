import threading

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget


class _Signal(QWidget):
    signal = Signal(tuple, dict)

    def connectSignal(self, call):
        self.signal.connect(call)

    def call(self, *args, **kwargs):
        self.signal.emit(args, kwargs)


class QExecMainThread:
    _execs = []

    def __init__(self, method):
        self.method = method
        self.initClass = None
        self.signal = None

        self._execs.append(self)

    @classmethod
    def init(cls, initClass):
        for name in dir(initClass):
            selfClass = getattr(initClass, name)
            if selfClass.__class__ == cls:
                selfClass.initClass = initClass
                selfClass.signal = _Signal()
                selfClass.signal.connectSignal(selfClass.call)

    def __call__(self, *args, **kwargs):
        if threading.main_thread() != threading.current_thread():
            if self.signal is not None:
                self.signal.call(*args, **kwargs)
        else:
            self.method(self.initClass, *args, **kwargs)

    def call(self, args, kwargs):
        if self.initClass is not None:
            self.method(self.initClass, *args, **kwargs)
