from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^acc/', include('django.contrib.auth.urls')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^budget/', include('budget.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^diary/', include('diary.urls')),
    url(r'^organizer/', include('todo.urls')),
    url(r'^passorg/', include('password.urls')),
    url(r'^task/', include('task.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)