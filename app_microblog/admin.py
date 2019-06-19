from django.contrib import admin
from app_microblog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')


admin.site.register(Post, PostAdmin)
admin.site.site_header = 'Сайт Администратора'
admin.site.site_title = 'Сайт Администратора'
admin.site.index_title = 'Администратор сайта'
