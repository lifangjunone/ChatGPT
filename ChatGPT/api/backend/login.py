from flask_restful import Resource
from common.return_data import Success, get_return_data


class LoginViewSet(Resource):

    def post(self):
        data = {
            "id": 1,
            "name": "god",
            "token": "god chatgpt"
        }
        return get_return_data(Success, data)