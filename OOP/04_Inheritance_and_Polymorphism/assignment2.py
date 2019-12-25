import datetime

class WriteFile(object):
    def __init__(self, filename):
        self.filename = filename
    def writetofile(self, filename, linetowrite):
        with open(self.filename) as file:
            file.write(linetowrite)

class LogFile(WriteFile):
    def form_string_towrite(self, string_to_write):
        self.dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')


class DelimFile(WriteFile):
    pass