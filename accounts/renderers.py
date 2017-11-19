import json

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import OrganizerUser


class OrganizerUserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        token = data.get('token', None)
        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        return json.dumps({'user': data})


class ListActiveJSONRenderer(JSONRenderer): # TODO view to ListActive
    charset = 'utf-8'

    def user_count_view(request, format=None):
        user_count = OrganizerUser.objects.filter(active=True).count()
        content = {'user_count': user_count}
        return Response(content)