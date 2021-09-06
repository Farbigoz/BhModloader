from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget

from ..ui_sources.ui_loading import Ui_Loading


class Loading(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Loading()
        self.ui.setupUi(self)

        self.movie = QMovie(":/icons/resources/icons/Loading.gif")
        self.ui.anim.setMovie(self.movie)
        self.movie.start()

    def setText(self, text):
        self.ui.label.setText(text)

