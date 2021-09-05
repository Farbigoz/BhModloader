import re


def GetBorderImage(widget, default=None) -> str:
    styleSheet = widget.styleSheet()
    borderImage = re.findall(r"border-image: url\((.+)\)", styleSheet)
    if borderImage:
        return borderImage[0].strip("\"")
    else:
        return default