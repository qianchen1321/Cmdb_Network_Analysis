"""
-*- coding:utf-8 -*-
@File: log.py
@Author:frank yu
@DateTime: 2021.10.12 20:56
@Contact: frankyu112058@gmail.com
@Description:
"""
import logging
import os
import random
import sys
import multiprocessing
import time
from shutil import copyfile
from colorlog import ColoredFormatter

# log directory
LOG_DIR = ".\\testlog\\logs"
# level fot stdout
STD_LEVEL = logging.DEBUG
# level for file
FILE_LEVEL = logging.DEBUG

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


class Log:
    def __init__(self, log_dir=LOG_DIR):
        """
        function:init create log file, judge if log file is too bigger
        :param log_dir: directory of logs
        """
        log_path = log_dir + "/log"
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
            os.chmod(log_dir, 0o777)
        if not os.path.exists(log_path):
            f = open(log_path, mode='w', encoding='utf-8')
            f.close()
            os.chmod(log_path, 0o777)
        # if log file is more than 1MB, copy to a file and clear log file
        if os.path.getsize(log_path) / 1048576 > 1:
            # print(os.path.getsize(log_path))
            copyfile(log_path, log_dir + "/log" + str(time.time()).replace(".", ""))
            with open(log_path, 'w') as f:
                f.truncate()
                f.close()
        self.logger_format = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
        self.c_logger_format = ColoredFormatter(fmt='%(log_color)s%(asctime)s'
                                                    ' - %(log_color)s%(levelname)s: %(log_color)s%(message)s',
                                                reset=True,
                                                secondary_log_colors={},
                                                style='%'
                                                )
        self.logger = logging.getLogger(str(random.random()))
        self.logger.handlers.clear()
        self.logger.setLevel(logging.DEBUG)

        self.filehandler = logging.FileHandler(log_path, mode='a')
        self.filehandler.setLevel(FILE_LEVEL)
        self.filehandler.setFormatter(self.logger_format)

        self.stdouthandler = logging.StreamHandler(sys.stdout)
        self.stdouthandler.setLevel(STD_LEVEL)
        self.stdouthandler.setFormatter(self.c_logger_format)

        self.logger.addHandler(self.stdouthandler)
        self.logger.addHandler(self.filehandler)

        self.__lock = multiprocessing.Lock()

    def __log(self, msg=None, level=logging.INFO):
        if level == logging.DEBUG:
            self.logger.debug(msg)
        elif level == logging.INFO:
            self.logger.info(msg)
        elif level == logging.WARNING:
            self.logger.warning(msg)
        elif level == logging.ERROR:
            self.logger.error(msg)
        elif level == logging.CRITICAL:
            self.logger.critical(msg)

    def log_show_store(self, msg, level):
        """
        function: show logs on screen and store logs into log file
        :param msg:message of log
        :param level:level of log
        return: None
        """
        self.__lock.acquire()
        self.logger.addHandler(self.stdouthandler)
        self.logger.addHandler(self.filehandler)
        self.__log(msg=msg, level=level)
        self.__lock.release()

    def log_show(self, msg, level):
        """
        function:show msg on the screen
        :param msg:message of log
        :param level: level of log
        """
        self.__lock.acquire()
        self.logger.removeHandler(self.filehandler)
        self.logger.addHandler(self.stdouthandler)
        self.__log(msg, level=level)
        self.logger.removeHandler(self.stdouthandler)
        self.logger.addHandler(self.filehandler)
        self.__lock.release()

    def log_store(self, msg, level):
        """
        function:store msg into log file
        :param msg:message of log
        :param level: level of log
        """
        self.__lock.acquire()
        self.logger.removeHandler(self.stdouthandler)
        self.logger.addHandler(self.filehandler)
        self.__log(msg, level=level)
        self.logger.removeHandler(self.filehandler)
        self.logger.addHandler(self.stdouthandler)
        self.__lock.release()

    def log_wrapper(self, *args):
        """
        function: record arg and result of functions
        :param args:
        :return: wrapper
        """
        self.log_store(' '.join(args), FILE_LEVEL)

        def wrapper(func):
            def inner(*args, **kwargs):
                self.log_store(getattr(func, "__name__") + " call " + str(args) + str(kwargs), 10)
                ret = func(*args, **kwargs)
                self.log_store(getattr(func, "__name__") + " return " + str(ret), 10)
                return ret

            return inner

        return wrapper

