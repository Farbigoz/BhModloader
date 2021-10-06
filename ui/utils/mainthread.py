import threading

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget


class QExecMainThread(QWidget):
    _execs = []

    signal = Signal(tuple)

    def __init__(self, method):
        args = method.__code__.co_varnames[:method.__code__.co_argcount]
        if len(args) > 0 and args[0] == "self":
            self.args = args[1:]
        else:
            self.args = args

        self.method = method
        self.initClass = None

        self._initFlag = False

        self._execs.append(self)

    def _init(self, initClass):
        self.initClass = initClass

        if not self._initFlag:
            super().__init__()
            self._initFlag = True

    @classmethod
    def init(cls, initClass):
        for _exec in cls._execs:
            _exec._init(initClass)

            if getattr(initClass.__class__, _exec.method.__code__.co_name).method == _exec.method:
                _exec.signal.connect(_exec.call)

    def __call__(self, *args, **kwargs):
        if threading.main_thread() != threading.current_thread():
            if self.signal is not None:
                self.signal.emit((args, kwargs))
        else:
            self.method(self.initClass, *args, **kwargs)

    def call(self, _args):
        args, kwargs = _args
        if self.initClass is not None:
            self.method(self.initClass, *args, **kwargs)
