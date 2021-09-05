import os
import PySide6

uiSourcesPath = os.path.dirname(__file__)

translatePath = os.path.join(uiSourcesPath, "translate")
if not os.path.exists(translatePath):
    os.mkdir(translatePath)

translateSourcesPath = os.path.join(translatePath, "sources")
if not os.path.exists(translateSourcesPath):
    os.mkdir(translateSourcesPath)

lstFilePath = os.path.join(translatePath, "ui.txt")

lupdatePath = os.path.join(os.path.dirname(PySide6.__file__), "lupdate.exe")
lreleasePath = os.path.join(os.path.dirname(PySide6.__file__), "lrelease.exe")


def MakeLstFile():
    with open(lstFilePath, "w") as lstFile:
        for file in os.listdir(uiSourcesPath):
            if file.endswith(".ui"):
                lstFile.write(os.path.join(uiSourcesPath, file) + "\n")


def MakeTsFile(lang="en_EU"):
    if not os.path.exists(lstFilePath):
        raise FileExistsError(f"File {lstFilePath} not exists!. Use 'MakeLstFile' function")

    os.system(f"{lupdatePath} @{lstFilePath} -ts {translateSourcesPath}\\{lang}.ts")


def CompileTsFiles():
    for ts in os.listdir(translateSourcesPath):
        os.system(f"{lreleasePath} {translateSourcesPath}\\{ts} -qm {translatePath}\\{ts.replace('.ts', '.qm')}")


def GetLangs():
    return {
        file.replace(".qm", ""): os.path.join(translatePath, file)
        for file in os.listdir(translatePath)
        if file.endswith(".qm")
    }


# MakeLstFile()
# MakeTsFile("ru_RU")
# CompileTsFiles()
