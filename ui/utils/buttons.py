def AddButtonWidthToTexSize(button, plusSize):
    text_size = button.fontMetrics().boundingRect(button.text()).width()
    button.setMinimumSize(text_size+plusSize, 40)


def ButtonTextSize(button):
    return button.fontMetrics().boundingRect(button.text()).size()
