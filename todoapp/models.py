from django.db import models


class TodoappItem(models.Model):
    content = models.TextField(verbose_name='справа')
