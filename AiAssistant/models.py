from django.db import models
# specifying the choices - [(Value, DisplayText)] or [(V,((V,DT),(V,DT))] 
from django.core.validators import MinLengthValidator

class StudentRegister(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField() 
    studentid = models.CharField(max_length=10)
    gender = models.CharField(
        max_length=10,  
        choices = GENDER_CHOICES,
        default = 'Not Mentioned')
    email = models.EmailField()
    password = models.CharField(max_length=32, validators=[MinLengthValidator(8)])
    mobile = models.IntegerField()
    college = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="images/") 
    percentage = models.SmallIntegerField()
    def __str__(self):
        return self.name

class StudentContact(models.Model):
    name = models.CharField(max_length=48)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
    def __str__(self):
        return  self.name
    
class StudentChat(models.Model):
    user_message = models.CharField(max_length=1000)
    chat_message = models.CharField(max_length=1000)
    def __str__(self):
        return self.user_message