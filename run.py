import sys
import traceback

from core import Error


def handle_exception(exc_type, exc_value, exc_traceback):
    Error("ModLoader", "".join(traceback.format_exception(exc_type, exc_value, exc_traceback)))
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


sys.excepthook = handle_exception


if __name__ == "__main__":
    from main import RunApp
    RunApp()
