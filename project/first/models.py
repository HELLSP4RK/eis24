import string
from random import choices

from django.db.models import *


class Account(Model):
    number = AutoField(primary_key=True, verbose_name='Номер')
    name = CharField(max_length=20, verbose_name='Имя')

    class Meta:
        verbose_name = 'Учетная запись'
        verbose_name_plural = 'Учетные записи'

    def __str__(self):
        return f'{self.name} #{self.number}'


session_id_max_length = 55


class Session(Model):
    user = ForeignKey(Account, on_delete=CASCADE, related_name='sessions', verbose_name='Пользователь')
    session_id = CharField(max_length=session_id_max_length, blank=True, editable=False, unique=True, verbose_name='ID сессии')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'

    def __str__(self):
        return f'{self.user} | {self.created_at} | {self.session_id}'

    @classmethod
    def exists(cls, session_id):
        return cls.objects.filter(session_id=session_id).exists()

    def save(self, *args, **kwargs):
        # Генерируем случайный session_id
        self.session_id = ''.join(choices(string.ascii_letters + string.digits, k=session_id_max_length))
        # Если сессии с таким session_id не существует, ...
        if not Session.exists(self.session_id):
            # то сохраняем сессию, ...
            return super(Session, self).save(*args, **kwargs)
        # иначе все сначала
        return self.save(self, *args, **kwargs)


class Action(Model):

    class Type(TextChoices):
        CREATE = 'create', 'Создание'
        READ = 'read', 'Чтение'
        UPDATE = 'update', 'Изменение'
        DELETE = 'delete', 'Удаление'

    session = ForeignKey(Session, on_delete=CASCADE, related_name='actions', verbose_name='Сессия')
    type = CharField(max_length=6, choices=Type.choices, verbose_name='Тип')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Действие'
        verbose_name_plural = 'Действия'

    def __str__(self):
        return f'{self.session.user} | {self.type} | {self.session.session_id}'
