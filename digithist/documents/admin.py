from django.contrib import admin

from documents.models import Document, Folder

class DocumentAdmin(admin.ModelAdmin):  
    list_display = ('path', 'type', 'value') 

class FolderAdmin(admin.ModelAdmin):  
    list_display = ('path', 'name') 


admin.site.register(Document, DocumentAdmin)
admin.site.register(Folder, FolderAdmin)
