# Brawlhalla ModLoader ![Python 3.6](https://img.shields.io/badge/python-3.8-blue.svg)

**ModLoader** - tool for installing mods in Brawlhalla  
**[ModCreator](https://github.com/Farbigoz/BhModCreator)** - tool for creating mods for Brawlhalla

![window](https://github.com/Farbigoz/BhModCreator/blob/main/wiki/readme/window.png)

## Download application
For downloading the app, see [**latest release**](https://github.com/Farbigoz/BhModloader/releases/latest). 
Older versions and pre-releases builds are available on [**releases section**](https://github.com/Farbigoz/BhModloader/releases)

## Project

### Required libraries
    $ pip install JPype1
    $ pip install PySide6
    $ pip install psutil
    $ pip install pywin32   #If your system - Windows
    
### Build
    $ pip install pyinstaller  
    $ pyinstaller main.spec

## Licenses

Brawlhalla ModCreator is licensed with GNU GPL v3, see the [license.txt](license.txt).
It uses modified code of these libraries:

* [FFDec Library](https://github.com/jindrapetrik/jpexs-decompiler) - LGPLv3