from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User = get_user_model()
class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2) # Всего 10 чисел, из которых после запятой - 2
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, models.CASCADE) # Если Юзер будет удален, то все связанные обьявления тоже будут удалены
    image = models.ImageField('Изображение', upload_to='advertisments')

    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={'pk': self.pk})

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(format_string =f'<span style="color: green; font-weight: bold;">Сегодня в {created_time}</span>')
        return self.created_at.strftime("%d:%M.%Y в %H:%M:%S")

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'