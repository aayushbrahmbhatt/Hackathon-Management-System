from django.db import models

class User(models.Model):
    user_id = models.CharField(primary_key=True , max_length=100)
    email_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    mobile = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'User'

class Hackathon(models.Model):
    hack_id = models.CharField(primary_key=True , max_length=100)
    date = models.DateField()
    s_time = models.TimeField()
    e_time = models.TimeField()
    duration = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Hackathon'

class Participant(models.Model):
    user_id = models.CharField(primary_key=True , max_length=100)
    hack_id = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'Participant'
