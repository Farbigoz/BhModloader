from typing import List

from ..utils.textformater import TextFormatter


class ModClass:
    def __init__(self,
                 gameVersion: str,
                 name: str,
                 author: str,
                 version: str,
                 description: str,
                 tags: List[str],
                 previewsPaths: List[str],
                 hash: str,
                 platform: str,
                 installed: bool,
                 currentVersion: bool,
                 modFileExist: bool
                 ):
        self.gameVersion = gameVersion
        self.name = name
        self.author = author
        self.version = version
        self.description = TextFormatter.format(description)
        self.tags = tags
        self.previewsPaths = previewsPaths
        self.hash = hash
        self.platform = platform
        self.installed = installed
        self.currentVersion = currentVersion
        self.modFileExist = modFileExist
