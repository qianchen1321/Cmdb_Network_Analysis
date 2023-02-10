import logging
import logging.handlers
import glob

LOG_FILENAME = "logging_rotatingfile_example.out"
my_logger = logging.getLogger('Mylogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20,backupCount=5,)
my_logger.addHandler(handler)

for i in range(20):
    my_logger.debug("i = %d: " % i)

logfiles = glob.glob('%s*' %LOG_FILENAME)
for filename in logfiles:
    print(filename)
#logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,)
# logging.debug('This message should go to the log file')
# with open(LOG_FILENAME, 'rt') as f:
#     body = f.read()
# print("File:")
# print(body)