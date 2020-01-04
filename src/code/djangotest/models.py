
from django.db import models

class Password(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    website = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    pwd = models.CharField(max_length=128)
    time_add = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    time_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'site={},username={}, pwd={}'.format(
            self.website, self.username, self.pwd) 

    class Meta:
        db_table = 'password_tab'


