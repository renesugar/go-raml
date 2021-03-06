# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import text
from . import files_api


files_if = Blueprint('files_if')


class files_bypathView(HTTPMethodView):

    async def get(self, request, path=""):

        return await files_api.files_byPath_get(request, path)


files_if.add_route(files_bypathView.as_view(), '/files/', strict_slashes=True)
files_if.add_route(files_bypathView.as_view(), '/files/<path:path>')
