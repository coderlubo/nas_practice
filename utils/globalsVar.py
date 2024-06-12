from cgi import test
from utils.getData import get_data
from utils.myLog import get_logger


logger = None
train_load, eval_load, test_load = None, None, None

def set_logger():

    global logger
    logger = get_logger()

    return logger

def get_global_logger():

    global logger
    return logger

def set_data():
    
    global train_load
    global eval_load
    global test_load

    train_load, eval_load, test_load = get_data()

    return train_load, eval_load, test_load

def get_train_data():

    global train_load
    return train_load

def get_eval_data():
    global eval_load
    return eval_load

def get_test_data():
    global test_load
    return test_load

