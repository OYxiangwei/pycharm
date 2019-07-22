import logging

LOG_FORMART = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG,format=LOG_FORMART,filename='my.log')
logging.debug("debug")
logging.error("error")
logging.warning("warning")
logging.info('info')

def log(func):
    def wrapper(*args,**kwargs):
        logging.error("error2")
        return func(*args,**kwargs)
    return wrapper

@log
def test():
    print("测试结束")
test()