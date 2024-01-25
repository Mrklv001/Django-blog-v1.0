from django.contrib import admin
from blog.models import Post, User

user = User.objects.get(username='admin')
post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
post.save()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
