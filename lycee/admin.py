from django.contrib import admin

from .models import Student, Cursus

class StudentAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email", "phone")

class CursusAdmin(admin.ModelAdmin):
  list_display = ("scholar_year", "name", "year_from_bac")
  fieldsets = [
    ('nom_zone1', {'fields': ['name']}),
    ('nom_zone2', {'fields':
    ['scholar_year','year_from_bac'], 'classes':
    ['collapse']}),
  ]

admin.site.register(Student, StudentAdmin)
admin.site.register(Cursus, CursusAdmin)