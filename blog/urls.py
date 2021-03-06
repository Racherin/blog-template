from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from post.views import index,blog,post,search,post_delete,post_update,post_create


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('blog/',blog,name='post-list'),
    path('post/<id>/',post,name='post-detail'),
    path('create/',post_create,name='post-create'),
    path('post/<id>/delete',post_delete,name='post-delete'),
    path('post/<id>/update',post_update,name='post-update'),
    path('search/',search,name='search'),
    path('tinymce/',include('tinymce.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)