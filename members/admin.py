from django.contrib import admin

# Register your models here.
from .models import *
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'create_date', 'image')


admin.site.register(Member, MemberAdmin)
