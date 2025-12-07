import logging 

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')


def logger_func(fx):
    def caller(*args,**kwargs):
        logging.info(f"calling the fucntion {fx.__name__}")
        res = fx(*args,**kwargs)
        print(res)
        logging.info(f"executed function {fx.__name__} ")
        return res
    return caller

@logger_func
def add(a:int,b:int):
    return a+b



if __name__ == "__main__":
    add(2,4)


       