class UserView():
    @staticmethod
    def get_string():
        return input('Введите выражение: ')
    @staticmethod
    def result_view(res, text):
        print(f'{text} = {res}')
    @staticmethod
    def error():
        print('Ошибка ввода!')