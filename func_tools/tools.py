import traceback
import sys,os
sys.path.append(r"D:\Code\Ymir\comm")
sys.path.append(r"D:\Code\Ymir")
from logger import logger

class InnerExceprtion(Exception):
    def __init__(self, id:int, message:str):
        self.id = id
        self.message = message
    
    @staticmethod
    def RaiseInnerExceprtion(cls, id:int, message:str):
        raise InnerExceprtion(id, message)

def funcWrap(func):
    def runfunc(*args, **kwargs):
        try:
            func(args, kwargs)
        except InnerExceprtion as iner:
            logger.error(f"{iner.id}:{iner.message}")
        except Exception as e:
            logger.error(f"{traceback.format_exc()}")
    return runfunc
