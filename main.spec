# -*- mode: python ; coding: utf-8 -*-
import os

client_a = Analysis(['client.py'],
                    binaries=[],
                    datas=[],
                    hiddenimports=[],
                    hookspath=[],
                    runtime_hooks=[],
                    excludes=['unittest', 'email', 'html', 'http', 'urllib',
                    'xml', 'pydoc', 'doctest', 'datetime', 'zipfile',
                    'pickle', 'calendar', 'tkinter',
                    'bz2', 'getopt', 'string', 'quopri', 'copy', 'imp',
                    'aioflask', 'aiohttp', 'cairo', 'cython', 'flask', 'PIL', 'wand',
                    'java.lang', 'xml.parsers', 'datetime', 'java', 'pickle'],
                    win_no_prefer_redirects=False,
                    win_private_assemblies=False,
                    noarchive=False)

client_pyz = PYZ(client_a.pure, client_a.zipped_data,
                 cipher=None)

client_exe = EXE(client_pyz,
                 client_a.scripts,
                 client_a.binaries,
                 client_a.zipfiles,
                 client_a.datas,
                 name='ModLoaderClient',
                 debug=False,
                 bootloader_ignore_signals=False,
                 strip=False,
                 upx=True,
                 upx_exclude=['vcruntime140.dll', 'ucrtbase.dll'],
                 runtime_tmpdir=None,
                 console=False)


app_a = Analysis(['run.py'],
                 binaries=[],
                 datas=[],
                 hiddenimports=[],
                 hookspath=[],
                 runtime_hooks=[],
                 excludes=['tkinter', '_tkinter'],
                 win_no_prefer_redirects=False,
                 win_private_assemblies=False,
                 noarchive=True)
app_a.datas += [('file_icon.ico','file_icon.ico','DATA'),
                (os.path.split(client_exe.name)[1], client_exe.name, 'DATA'),
                ('unrar.exe', 'libs\\unrar.exe', 'DATA')]

app_pyz = PYZ(app_a.pure, app_a.zipped_data)

app_splash = Splash('splash.png',
                    binaries=app_a.binaries,
                    datas=app_a.datas,
                    text_pos=(153, 231),
                    text_font="Exo",
                    text_size=13,
                    text_color='#92B7D1')

app_exe = EXE(app_pyz,
              app_a.scripts,
              app_a.binaries,
              app_a.zipfiles,
              app_a.datas,
              Tree("ui", "ui", excludes=["*.ttf", "*.png", "*.jpg", "*.ui", "*.txt", "*.pyc", "*.pyo"]),
              Tree("core", "core", excludes=["*.pyc", "*.pyo"]),
              app_splash,
              app_splash.binaries,
              name='BrawlhallaModLoader',
              debug=False,
              bootloader_ignore_signals=False,
              strip=False,
              upx=False,
              upx_exclude=['vcruntime140.dll', 'ucrtbase.dll'],
              runtime_tmpdir=None,
              version='version.spec',
              console=False,
              icon='ui/ui_sources/resources/icons/App.ico')

#os.remove(client_exe.name)
