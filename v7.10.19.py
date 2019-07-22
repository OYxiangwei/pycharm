import logging

LOG_FORMART = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=LOG_FORMART,filename='my2.log')

def log(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            logging.error(text)
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log("ce1")
def test():
    print("ce111")
@log("ce2")
def main():
    print("main done")

test()
main()