from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.display_home,name='home'),
    url(r'^posts/',views.new_post, name='post'),
    url(r'comment/<int:id>', views.add_comment, name='comment'),
    url(r'search/',views.search, name='search'),
    url(r'profile/',views.show_profile, name='profile'),
    url('update/<int:id>',views.update_profile,name='update_profile'),
    url(r'signup/', views.signup, name='signup'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)