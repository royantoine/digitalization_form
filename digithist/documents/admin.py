from django.contrib import admin

from documents.models import Document, Folder, Sale

class DocumentAdmin(admin.ModelAdmin):  
    list_display = ('path', 'type', 'value') 

class FolderAdmin(admin.ModelAdmin):  
    list_display = ('path', 'name') 

class SaleAdmin(admin.ModelAdmin):  
    list_display = ('name', 'value') 


admin.site.register(Document, DocumentAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(Sale, SaleAdmin)
