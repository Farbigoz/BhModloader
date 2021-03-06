# -*- mode: python ; coding: utf-8 -*-

VSVersionInfo(
    ffi=FixedFileInfo(
        filevers=(0, 2, 4, 0),
        prodvers=(0, 2, 4, 0),
        mask=0x3f,
        flags=0x2,      #0x2 - Prerelease, 0x0 - Release
        OS=0x40004,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        StringFileInfo(
            [
                StringTable(
                    u'040904B0',
                    [
                        StringStruct(u'CompanyName', u'I_FabrizioG_I'),
                        StringStruct(u'FileDescription', u'Brawlhalla Mod Loader'),
                        StringStruct(u'FileVersion', u'0.2.4version'),
                        StringStruct(u'InternalName', u'BrawlhallaModLoader'),
                        StringStruct(u'LegalCopyright', u'\xa9 I_FabrizioG_I.'),
                        StringStruct(u'OriginalFilename', u'BrawlhallaModLoader.exe'),
                        StringStruct(u'ProductName', u'Brawlhalla Mod Loader'),
                        StringStruct(u'ProductVersion', u'0.2.4.0')
                    ]
                )
            ]), 
        VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)