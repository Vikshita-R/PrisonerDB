from django.contrib import admin
from .views import Prisoner, Crime, FIR, Court, Visitor, Lawyer

admin.site.register(Prisoner)
admin.site.register(Crime)
admin.site.register(FIR)
admin.site.register(Court)
admin.site.register(Visitor)
admin.site.register(Lawyer)

# Register your models here.

admin.site.site_title = "PrisonerDB"
admin.site.site_header = "PrisonerDB Administration"
admin.site.index_title = "PrisonerDB Administration"
