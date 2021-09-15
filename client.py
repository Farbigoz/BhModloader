import os
import sys
import json
import time
import socket
import argparse
import threading


SOCKET_PORT = 25591
CONFIG_FILE = "startup.json"
CONFIG = {"clientHash": "",  "modLoaderPath": ""}
MODLOADER_CLIENT = "ModLoaderClient.exe"

FROZEN = getattr(sys, 'frozen', False)


class Commands:
    NONE = b"\x00"
    JUST_OPEN = b"\x01"
    OPEN_FILE = b"\x02"
    OPEN_URL = b"\x03"


class Arguments:
    AS_ADMIN = "-asadmin"
    UPDATE = "-update"
    FILE = "-file"
    URL = "-url"


def Run(file=None, url=None, timeout=0.1):
    mlclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mlclient.settimeout(timeout)
    mlclient.connect(("127.0.0.1", SOCKET_PORT))

    if file is not None:
        if os.path.exists(file):
            data = str(file).encode("UTF-8")
            data_size = len(data)
            mlclient.send(Commands.OPEN_FILE + data_size.to_bytes(2, byteorder='big'))
            mlclient.send(data)
        else:
            mlclient.send(Commands.NONE + b"\x00\x00")
    elif url is not None:
        data = str(url).encode("UTF-8")
        data_size = len(data)
        mlclient.send(Commands.OPEN_URL + data_size.to_bytes(2, byteorder='big'))
        mlclient.send(data)

    mlclient.recv(1)
    mlclient.close()


def Update(oldFile, newFile, autoRun=False):
    if None not in (oldFile, newFile) and os.path.exists(oldFile) and os.path.exists(newFile):
        i = 0
        while i < 5:
            try:
                with open(newFile, "rb") as newFileIO:
                    with open(oldFile, "wb") as oldFileIO:
                        oldFileIO.write(newFileIO.read())

                os.remove(newFile)

                if oldFile.endswith(".exe") and autoRun:
                    threading.Thread(target=os.startfile, args=(oldFile,)).start()
                    time.sleep(1)

                break
            except:
                i += 1
                time.sleep(1)


if __name__ == "__main__":
    if FROZEN:
        configPath = os.path.join(os.path.split(sys.argv[0])[0], CONFIG_FILE)
        with open(configPath, "r") as file:
            config = json.loads(file.read())
    else:
        config = CONFIG
        config["modLoaderPath"] = os.path.join("dist", "BrawlhallaModLoader.exe")

    parser = argparse.ArgumentParser()
    parser.add_argument(Arguments.FILE, dest='file', required=False)
    parser.add_argument(Arguments.URL, dest='url', required=False)
    parser.add_argument(Arguments.UPDATE, metavar=("OLD_FILE", "NEW_FILE"), nargs=2, default=None, required=False)
    args = parser.parse_args()

    if args.update is not None:
        old, new = args.update
        Update(old, new, True)

    else:
        try:
            Run(args.file, args.url)
        except (ConnectionRefusedError, socket.timeout):
            if os.path.exists(config["modLoaderPath"]):
                threading.Thread(target=os.startfile, args=(config["modLoaderPath"], )).start()
                i = 0
                while i < 5:
                    try:
                        Run(args.file, args.url, 5)
                        sys.exit(0)
                    except (ConnectionRefusedError, socket.timeout):
                        i += 1
