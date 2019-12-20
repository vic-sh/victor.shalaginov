import datetime

class WriteFile(object):
    def __init__(self, filename):
        pass

class LogFile(WriteFile):
    def write(self, string_to_write):
        self.dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        

class DelimFile(WriteFile):
    pass