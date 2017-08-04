from django.contrib import admin
from models import Question,Choice
# Register your models here.
class Qadmin(admin.TabularInline):
    model = Choice
    extra = 3
class SuperAdmin(admin.ModelAdmin):
    inlines = [Qadmin]
    list_display = ['question_text','pubtime']


admin.site.register(Question,SuperAdmin)
admin.site.register(Choice)
