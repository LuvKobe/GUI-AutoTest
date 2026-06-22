import logging
import os.path
import time

class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO

class ErrFileter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR

class Logger:
    logger = None
    @classmethod
    def getlog(cls):
        #创建日志对象
        if cls.logger is None:
            cls.logger = logging.getLogger(__name__)
            #设置日志级别
            cls.logger.setLevel(logging.DEBUG)

            LOG_PATH = "logs/"
            if not os.path.exists(LOG_PATH):
                os.mkdir(LOG_PATH)

            #2025-06-30.log  2025-06-30_err.log  2025-06-30_info.log
            now = time.strftime("%Y-%m-%d")

            logname = LOG_PATH +  now + ".log"
            info_logname = LOG_PATH + now + "_info.log"
            err_logname = LOG_PATH + now + "_err.log"

            #创建总日志文件处理器
            handler = logging.FileHandler(logname,encoding="utf-8")

            #创建info日志文件处理器
            info_handler = logging.FileHandler(info_logname,encoding="utf-8")
            #添加文件过滤
            info_handler.addFilter(InfoFilter())

            #创建err日志文件处理器
            err_handler = logging.FileHandler(err_logname,encoding="utf-8")
            err_handler.addFilter(ErrFileter())

            #设置日志格式
            formatter = logging.Formatter(
                "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
            )

            handler.setFormatter(formatter)
            info_handler.setFormatter(formatter)
            err_handler.setFormatter(formatter)

            #给logger对象添加handler
            cls.logger.addHandler(handler)
            cls.logger.addHandler(info_handler)
            cls.logger.addHandler(err_handler)
        return cls.logger