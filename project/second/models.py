from django.db.models import *


class Month(IntegerChoices):
    JAN = '1', 'январь'
    FEB = '2', 'февраль'
    MAR = '3', 'март'
    APR = '4', 'апрель'
    MAY = '5', 'май'
    JUNE = '6', 'июнь'
    JULY = '7', 'июль'
    AUG = '8', 'август'
    SEPT = '9', 'сентябрь'
    OCT = '10', 'октябрь'
    NOV = '11', 'ноябрь'
    DEC = '12', 'декабрь'


class Accrual(Model):
    date = DateTimeField(verbose_name='Дата')
    month = SmallIntegerField(choices=Month.choices, verbose_name='Месяц')

    class Meta:
        verbose_name = 'Долг'
        verbose_name_plural = 'Долги'
        ordering = ['-date']

    def __str__(self):
        return f'{self.date} | {self.month}'


class Payment(Model):
    date = DateTimeField(verbose_name='Дата')
    month = SmallIntegerField(choices=Month.choices, verbose_name='Месяц')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ['-date']

    def __str__(self):
        return f'{self.date} | {self.month}'
