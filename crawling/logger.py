from datetime import datetime

class Logger:

    def __init__(self,name,time = None):
        self.name = name
        if time is None:
            time = datetime.now()
        print(time, self.name,'class 생성!')

    def error(self,message,time = None):
        """
        message get error message
        """
        if time is None:
            time = datetime.now()
        print(time,'Error: ',self.name, message)
        
    def info(self,message,time = None):
        """
        message get log message
        """
        if time is None:
            time = datetime.now()
        print(time,'Info: ',self.name, message)


if __name__== "__main__":
    log = Logger('logger')