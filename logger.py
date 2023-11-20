#!/usr/bin/python3

from os import (system, path)
from re import match as matches
from time import strftime

class Logger:
    def __init__(self, filename: str = "logfile.log"):
        if not matches(r"\\|\/", filename):
            filename = self.__get_path(filename) + "/" + filename

        self.__filename = filename
        self.__logfile = open(filename, "a")

    def __del__(self):
        if self.__logfile != None:
            self.__logfile.close()
            self.__logfile = None

    def __get_time(self):
        return str("[" + strftime("%H:%M:%S  %d/%m/%Y") + "]")

    def __reopen(self):
        self.__logfile = open(self.__filename, "a")

    def __get_path(from_filename: str, path_format: str = "lunix"):
        curdir = ""

        if path_format in ("unix", "linux", "lunix"):     
            curdir = path.realpath(from_filename).replace("\\", "/")
            curdir = curdir.split("/")
            curdir.pop()
            curdir = "/".join(curdir)

        elif path_format in ("nt", "windows", "win"):
            curdir = curdir.split("\\")
            curdir.pop()
            curdir = "\\".join(curdir)

        return curdir

    def save(self, message: str):
        if self.__logfile != None:
            self.__logfile.write(message)
            self.__logfile.close()
            self.__logfile = None

    def log(self, message):
        if self.__logfile == None:
            self.__reopen()

        message = f"[CONSOLE] {message}\n"
        message = self.__get_time() + str(message)

        self.save(message)

    def inform(self, message):
        if self.__logfile == None:
            self.__reopen()
   
        message = f"[INFO] {message}\n"
        message = self.__get_time() + str(message)

        self.save(message)

    def warn(self, message):
        if self.__logfile == None:
            self.__reopen()

        message = f"[WARNING] {message}\n"
        message = self.__get_time() + str(message)

        self.save(message)

    def error(self, message):
        if self.__logfile == None:
            self.__reopen()
            
        message = f"[ERROR] {message}\n"
        message = self.__get_time() + str(message)

        self.save(message)