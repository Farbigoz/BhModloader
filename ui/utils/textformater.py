import re

from typing import List


class TextFormatter:
    mnemonics = {
        "&": "&amp;",
        "''": "&#039;",
        "\"\"": "&quot;",
        "<<": "&lt;",
        ">>": "&gt;",
        "\t": "&nbsp;"*4
    }

    regularMap = {
        "size": "<size ?= ?[\"']([0-9px]*)[\"']>".replace('\"', '"'),
        "/size": "</size>",
        "color": "<color ?= ?[\"'](#[0-9A-Fa-f]{6})[\"']>".replace('\"', '"'),
        "/color": "</color>",
        "bgcolor": "<bgcolor ?= ?[\"'](#[0-9A-Fa-f]{6})[\"']>".replace('\"', '"'),
        "/bgcolor": "</bgcolor>",
        "url": "<url ?= ?[\"'](.*)[\"']>".replace('\"', '"'),
        "/url": "</url>",
        "tooltip": "<tooltip ?= ?[\"'](.*)[\"']>".replace('\"', '"'),
        "/tooltip": "</tooltip>",
        "b": "<b>",  # Полужирный
        "/b": "</b>",
        "i": "<i>",  # Курсив
        "/i": "</i>",
        "u": "<u>",  # Подчёркнутый
        "/u": "</u>",
        "s": "<s>",  # Зачёркнутый текст
        "/s": "</s>",
        "sup": "<sup>",  # Верхний регистр
        "/sup": "</sup>",
        "sub": "<sub>",  # Нижний регистр
        "/sub": "</sub>",
        "center": "<center>",  # Выровнять по центру
        "/center": "</center>",
        "right": "<right>",  # Выровнять по правой стороне
        "/right": "</right>",
        "nlist": "<nlist>",  # Нумерованный список
        "/nlist": "</nlist>",
        "plist": "<plist>",  # Маркированный список
        "/plist": "</plist>",
        "el": "<el>",  # Элемент списка
        "/el": "</el>",
        "tab": "<tab>",
        "table": "<table>",  # Таблица
        "/table": "</table>",
        "tr": "<tr>",  # Строка таблицы
        "/tr": "</tr>",
        "td": "<td>",  # Элемент строки
        "/td": "</td>"
    }

    @classmethod
    def table(cls, table: List[List[str]], *, newLine=True):
        ret = ""

        n = "\n" if newLine else ""

        for row in table:
            ret += f"<tr>{n}"
            for el in row:
                ret += "<td>{}</td>{}".format(el or "\t", n)
            ret += f"</tr>{n}"

        return f"<table>{n}{ret}</table>"

    @classmethod
    def format(cls, text: str, textSize="14px"):
        text = text.strip()

        for symbol, mnemonic in cls.mnemonics.items():
            text = text.replace(symbol, mnemonic)

        text = text.replace("\n\n", "<p>&nbsp;</p>")
        #text = "<p>" + text.replace("\n", "</p>\n<p>") + "</p>"
        text = "<p>" + re.sub(r"\n(?!<el>|<plist>|<\/plist>|<nlist>|<\/nlist>)", "</p>\n<p>", text) + "</p>"

        split_text = re.split(r'(\<.*?\>)', text)

        for n, string in enumerate(split_text):
            for tag, regular in cls.regularMap.items():
                find = re.findall(regular, string)

                if find:
                    select = ""

                    if tag == "size":
                        if size := find[0].casefold():
                            select = f"<span style=\"font-size:{size}\">"
                    elif tag == "color":
                        select = f"<span style=\"color:{find[0]}\">"
                    elif tag == "bgcolor":
                        select = f"<span style=\"background-color:{find[0]}\">"
                    elif tag == "url":
                        select = f"<a href=\"{find[0]}\" style=\"text-decoration: none; color:#3498db\" title=\"{find[0]}\">"
                    elif tag == "/url":
                        select = f"</a>"
                    elif tag == "tooltip":
                        select = f"<span title=\"{find[0]}\">"
                    elif tag == "b":
                        select = f"<strong>"
                    elif tag == "/b":
                        select = f"</strong>"
                    elif tag == "i":
                        select = f"<em>"
                    elif tag == "/i":
                        select = f"</em>"
                    elif tag == "u":
                        select = f"<u>"
                    elif tag == "/u":
                        select = f"</u>"
                    elif tag == "s":
                        select = f"<s>"
                    elif tag == "/s":
                        select = f"</s>"
                    elif tag == "sup":
                        select = f"<sup>"
                    elif tag == "/sup":
                        select = f"</sup>"
                    elif tag == "sub":
                        select = f"<sub>"
                    elif tag == "/sub":
                        select = f"</sub>"
                    elif tag == "center":
                        select = f"<p style=\"text-align:center\">"
                    elif tag == "right":
                        select = f"<p style=\"text-align:right\">"
                    elif tag == "nlist":
                        select = f"<ol>"
                    elif tag == "/nlist":
                        select = f"</ol>"
                    elif tag == "plist":
                        select = f"<ul>"
                    elif tag == "/plist":
                        select = f"</ul>"
                    elif tag == "el":
                        select = f"<li>"
                    elif tag == "/el":
                        select = f"</li>"
                    elif tag == "tab":
                        select = "&nbsp;"*4
                    elif tag == "table":
                        select = f"<table width=\"100%\">"
                    elif tag == "/table":
                        select = f"</table>"
                    elif tag == "tr":
                        select = f"<tr>"
                    elif tag == "/tr":
                        select = f"</tr>"
                    elif tag == "td":
                        select = f"<td>"
                    elif tag == "/td":
                        select = f"</td>"
                    elif tag in ["/size", "/color", "/tooltip", "/bgcolor"]:
                        select = "</span>"
                    elif tag in ["/center", "/right"]:
                        select = f"</p>"

                    if select:
                        split_text[n] = select
                    break

        return ('<html>'
                '<head><style>'
                'p {margin-top: 0.1em;'
                'margin-bottom: 0.1em;}'
                '</style></head>'
                f'<body><span style="color:#eeeeee; font-size:{textSize}">\n{"".join(split_text)}\n</span></body>'
                '</html>')
