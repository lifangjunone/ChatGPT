import logging
import json
import time

from flask import stream_with_context
from flask import Response
from flask_restful import Resource, request
from common.return_data import get_return_data, Success, Unsuccessfully, ParamMissing
from common.chat_cli import ChatCli

_logger = logging.getLogger(__name__)


class ChatViewSet(Resource):

    def get(self):
        """
        聊天接口
        :return:
        """
        try:
            message = request.args.get('message', None)
            if not message:
                return get_return_data(ParamMissing)
            resp = ChatCli.get_result(message)
            return get_return_data(Success, resp)
        except Exception as e:
            _logger.error("Chat GPT si err:  %s", str(e))
            return get_return_data(Unsuccessfully, msg=str(e))


class ChatStreamViewSet(Resource):
    """
    流式返回数据
    """

    def get(self):
        resp = []
        try:
            message = request.args.get('message', None)
            if not message:
                return get_return_data(ParamMissing)
            resp = ChatCli.get_stream_result(message)
        except Exception as e:
            _logger.error("Chat GPT si err:  %s", str(e))
            return get_return_data(Unsuccessfully, msg=str(e))

        def handle_stream():
            for index, chunk in enumerate(resp):
                if index == 0:
                    continue
                chunk_message = chunk['choices'][0]['delta']
                yield json.dumps(chunk_message)
        return Response(handle_stream(), content_type="application/json")

