from django.contrib import admin
from .models import StudentRegister, StudentContact, StudentChat
# Register your models here.
admin.site.register(StudentRegister)
admin.site.register(StudentContact)
admin.site.register(StudentChat)