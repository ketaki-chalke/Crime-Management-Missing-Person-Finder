from django.contrib import admin

from .models import MissingCase
from .models import CrimeReport
from .models import ContactSubmission


admin.site.register(MissingCase)
# Register your models here.

admin.site.register(CrimeReport)
admin.site.register(ContactSubmission)