from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^token-auth/', obtain_jwt_token, name='token-auth'),              # rest_framework_jwt
    url(r'^token-refresh/', refresh_jwt_token, name='token-refresh'),       # rest_framework_jwt
    url(r'^token-verify/', verify_jwt_token, name='token-verify'),          # rest_framework_jwt
    url(r'^budget/', include('budget.urls')),

    # url(r'^contacts/', include('contacts.urls')),
    # url(r'^diary/', include('diary.urls')),
    # url(r'^password/', include('password.urls')),
    # url(r'^task/', include('task.urls')),
    url(r'^dj-auth/', include('django.contrib.auth.urls')),
    url(r'^soc-auth/', include('social_django.urls', namespace='soc-auth')),

    # url(r'^api/login/', include('rest_social_auth.urls_session')),
    # url(r'^api/login/', include('rest_social_auth.urls_token')),
    # url(r'^api/login/', include('rest_social_auth.urls_jwt')),

    url(r'^oauth/', include('rest_framework_social_oauth2.urls'))                # django-rest-framework-social-oauth2

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
