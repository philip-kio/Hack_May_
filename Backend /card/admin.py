from django.contrib import admin
from .models import CardDetail


# Register your models here.
# Register your models here.
admin.site.site_header = 'E-Card BACKEND'
admin.site.site_title = 'ADMIN'
admin.site.index_title = 'E-Card API'


class CardAdmin(admin.ModelAdmin):
    list_display = (('user','uuid','slug','first_name','last_name','employment_title','company'))
    prepopulated_fields = {'slug': ('first_name',)}

admin.site.register(CardDetail,CardAdmin)