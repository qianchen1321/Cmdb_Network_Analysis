from CustLogger.CustLog import Log
import logging

thislogger = Log(".")
thislogger.log_show("test", level=logging.DEBUG)
thislogger.log_show_store("SECtest", level=logging.DEBUG)
