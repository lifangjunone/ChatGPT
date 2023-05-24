from flask_restful import Api
from flask import Blueprint

from .chat_api import ChatViewSet, ChatStreamViewSet
from ChatGPT.api.common.version import ApiVersion

chat_manage_bp = Blueprint("chat_manage", __name__)
chat_manage = Api(chat_manage_bp, catch_all_404s=True)
chat_manage.add_resource(ChatViewSet, "/message")
chat_manage.add_resource(ChatStreamViewSet, "/message/stream")
chat_manage.add_resource(ApiVersion, "/version")
