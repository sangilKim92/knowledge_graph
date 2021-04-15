from datetime import datetime

class Logger:

    def __init__(self,name,time = None):
        self.name = name
        if time is None:
            time = datetime.now()
        print(time, '\033[33m' + self.name + ' 생성!'+'\033[0m')

    def error(self,message,time = None):
        """ message get error message

        Args:
            message is error message
            time is the execution time
        """
        if time is None:
            time = datetime.now()
        print(time,'\033[31m'+'Error: ' + self.name + " -> " + message ,'\033[0m')
        
    def info(self,message,time = None):
        """
        message get log message
        """
        if time is None:
            time = datetime.now()
        print(time,'\033[96m'+'Info: '+self.name+" -> "+ message + '\033[0m')


if __name__== "__main__":
    log = Logger('logger')