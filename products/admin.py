from django.contrib import admin
from . import models

#customize tables
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","active"]
    list_display_links = ["name","active"]
    list_editable = ['price']
    search_fields = ['name']
    list_filter = ['name','price']
    # fields=['name','price']
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Female)
admin.site.register(models.Male)
admin.site.register(models.User)
admin.site.register(models.Login)

admin.site.site_header = "My Admin"
admin.site.site_title = "Admin Page"



