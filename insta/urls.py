from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^',views.display_home,name='home'),
    url('^posts/',views.new_post, name='post'),
    url('comment/<id>', views.add_comment, name='comment'),
    url('search/', views.search, name='search'),
    url('profile/',views.show_profile, name='profile'),
    url('update/<id>', views.update_profile, name='update_profile'),
    url('signup/', views.signup, name='signup'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)