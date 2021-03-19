from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('allpost/', views.Postlistview.as_view(), name = 'allpost'),    
    path('createpost/create',views.CreatePost.as_view(),name='createpost'),
    path('createcat/create',views.CreateCategory.as_view(),name='createcat'),
    path('createpost/<int:pk>/new',views.DetailPost.as_view(),name='post-detail'),
    path('postupdate/<int:pk>/update',views.UpdatePost.as_view(),name='post-update'),
    path('postdelete/<int:pk>/delete',views.DeletePost.as_view(),name='post-delete'),   
    path('createpost/<int:pk>/create',views.CreateComment.as_view(),name='createcomment'),
    path('allpost/<str:cats>',views.CatPost,name='catpost'),
    path('like/<int:pk>',views.LikeView,name='like_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)