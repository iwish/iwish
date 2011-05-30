from django.db import models

# user table keeps user related info, including:
#   id, user name, email, MD5(passwd), privacy

class User(models.Model):
    id = models.AutoField(primary_key = True)
    userName = models.CharField(max_length = 128)
    email = models.EmailField()
    md5Passwd = models.CharField(max_length = 50)
    privacy = models.CharField(max_length = 50)
