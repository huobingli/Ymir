import os
import sys
import logging

g_log_logger  = None
g_log_dir = os.path.dirname(__file__) + "\\..\\";
def set_log_dir(_dir):
    global g_log_dir
    g_log_dir = os.path.abspath(_dir) + "\\"; 

def log_file_name():
    return g_log_dir + "/log.txt";
    
def _get_logger():
    global g_log_dir
    global g_log_logger
    if g_log_logger == None:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(g_log_dir + "/log.txt", mode='a')
        formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        g_log_logger = logger;

    return g_log_logger;


def log_write_info(_key, _info):
    __logger = _get_logger()
    __log_str = _key + "=" + _info;
    print(__log_str)
    __logger.info(__log_str);
    

def log_write_error(_key, _info):
    __logger = _get_logger()
    __log_str = _key + "=" + _info;
    print(__log_str)
    __logger.error(__log_str);
    

if __name__ == "__main__":
    test()

# for test
def test():
    log_write_info("key" , "info1")
    log_write_error("key" , "info2")