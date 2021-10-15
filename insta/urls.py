from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^',views.display_home,name='home'),
    url('comment/<id>', views.add_comment, name='comment'),
    url('^posts',views.new_post, name='post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)