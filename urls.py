from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from todo import views as main_views


urlpatterns = [
    url(r'^$', main_views.home, name='home'),
    url(r'^about/$', main_views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^budget/', include('budget.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^diary/', include('diary.urls')),
    url(r'^password/', include('password.urls')),
    url(r'^task/', include('task.urls')),
    url(r'^dj-auth/', include('django.contrib.auth.urls')),
    url(r'^soc-auth/', include('social_django.urls', namespace='soc-auth')),
    url(r'^api-auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^api/login/', include('rest_social_auth.urls_session')),
    url(r'^api/login/', include('rest_social_auth.urls_token')),
    url(r'^api/login/', include('rest_social_auth.urls_jwt')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
