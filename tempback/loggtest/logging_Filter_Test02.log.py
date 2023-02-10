import sys
import logging

class ContextFilter(logging.Filter):

    def filter(self, record):
        try:
            filter_key = record.TASK
        except AttributeError:
            return False

        if filter_key == "logToConsole":
            return True
        else:
            return False

if __name__ == '__main__':
    logger_Filtest02 = logging.getLogger('Filter_Test02')
    logger_Filtest02.setLevel(logging.DEBUG)
    #文件日志处理器配置
    logFile = "Filter02.log"
    file_Handler = logging.FileHandler(logFile)
    file_Handler.setLevel(logging.INFO)
    file_fmt = "%(asctime)-15s %(name)s %(levelname)s [%(filename)s %(lineno)d] %(message)s"
    fileFormat = logging.Formatter(file_fmt)
    file_Handler.setFormatter(fileFormat)
    logger_Filtest02.addHandler(file_Handler)

    #终端日志处理器配置
    console_Handler = logging.StreamHandler(sys.stdout)
    console_Handler.setLevel(logging.WARN)
    console_fmt = "%(asctime)s %(name)s [%(TASK)s] %(message)s"
    console_Formate = logging.Formatter(console_fmt)
    console_Handler.setFormatter(console_Formate)

    console_Filter = ContextFilter()
    console_Handler.addFilter(console_Filter)
    logger_Filtest02.addHandler(console_Handler)
    filter_dict = {'TASK':'logToConsole'}

    logger_Filtest02.debug("debug message")
    logger_Filtest02.info("info message")
    logger_Filtest02.warning("warn message")
    logger_Filtest02.error("error message", extra=filter_dict)
    logger_Filtest02.error("debug message")




