from django.db import models
from account.models import Account

# Create your models here.


class TodoModel(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="todo_works")
    start_tme = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = "Works"

    def __str__(self) -> str:
        return self.name + "|" + self.user.username
    

