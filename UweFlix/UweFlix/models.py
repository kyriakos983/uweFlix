from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    student_name = models.CharField(max_length=50, null=True)
    student_email = models.EmailField(max_length=100, null=True)

class ClubRep(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    clubRep_name = models.CharField(max_length=30)#
    club_rep_number = models.CharField(max_length=11)
    club_rep_email = models.EmailField(max_length=100, null=True)

class CinemaManager(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)



class Club(models.Model):
    club_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200)
    postCode = models.CharField(max_length=10)
    house_num = models.IntegerField(max_length=10)
    city = models.CharField(max_length=50)
    phone_num = models.IntegerField(max_length=11)
    email = models.EmailField(max_length= 100)

