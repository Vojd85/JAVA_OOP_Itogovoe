from datetime import datetime as dtnow

class LogTxt():
    def log_true(self, string, res):
        with open('log.txt', 'a') as data:
            time = dtnow.now().strftime('%d.%m.%y %H:%M')
            data.write(f'{time}: {string} = {res}\n')

    def log_error(self, string):
        time = dtnow.now().strftime('%d.%m.%y %H:%M')
        with open('log.txt', 'a') as data:
            data.write(f'{time}: {string} Error\n')