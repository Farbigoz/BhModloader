import sys


if sys.platform in ["win32", "win64"]:
    import win32api
    import win32con

    def Error(title, message):
        win32api.MessageBox(None, message, title,
                            win32con.MB_ICONERROR | win32con.MB_OK | win32con.MB_DEFBUTTON1)

else:
    def Error(title, message):
        pass
