from calc_rational import Rational
from calc_complex import Complex
from user_view import UserView
from logger import LogTxt

class Config():
    def __init__(self):
        self.rational = Rational()
        self.complex = Complex()
        self.view = UserView()
        self.log = LogTxt()

    def calculate(self):
        print('Введите выражение для вычисления рациональных и комплексных чисел')
        print('В случае комплексных чисел используйте "j" как мнимую единицу')
        try:
            stroka = self.view.get_string().replace(",", ".")
            if 'j' in stroka:
                result = self.complex.calc_c(stroka)
            else:
                result = self.rational.so_skobkami(stroka)
            UserView.result_view(result, stroka)
            self.log.log_true(stroka, result)
        except: 
            UserView.error()
            self.log.log_error(stroka)