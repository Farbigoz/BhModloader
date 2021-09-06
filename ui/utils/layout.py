def ClearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            layout.removeWidget(child.widget())
            child.widget().setParent(None)


def ClearFrame(frame):
    ClearLayout(frame.layout())


def AddToFrame(frame, widget, align=None):
    widget.setParent(frame)
    if align is None:
        frame.layout().addWidget(widget)
    else:
        frame.layout().addWidget(widget, 0, align)
