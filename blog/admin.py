from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields = ("name","description")
    list_display = ("name","created_at")

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at','updated_at',)
    search_fields = ("title","content","user__username","categories__name")
    list_filter = ("public",)
    list_display = ("title","public","user",'created_at')

    # Detertar usuario
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
