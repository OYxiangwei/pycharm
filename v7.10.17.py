import logging

logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

debug_handler = logging.FileHandler("1024debug.log")
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

error_handler = logging.FileHandler('1024error.log')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(debug_handler)
logger.addHandler(error_handler)

def log(func):
    def wrapper(*args,**kwargs):
        logger.debug("this is a debug info")
        logger.error("this is a error info")
        return func(*args,**kwargs)
    return wrapper
def loghigher(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            logger.debug(text)
            logger.error(text)
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log
def test1():
    print("test1 done")
@loghigher('this is test done')
def test2():
    print("test2 done")
@loghigher('this main done')
def main():
    print("main done")

test1()
main()