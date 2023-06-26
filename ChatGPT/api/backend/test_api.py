from flask_restful import Resource
from common.return_data import Success, get_return_data


class TestViewSet(Resource):

    def get(self):
        """
        this test api
        :return:
        """
        data = [
            {
                "name": "战三",
                "age": 29,
                "sex": "女"
            },
            {
                "name": "牛逼",
                "age": 19,
                "sex": "男"
            },
            {
                "name": "霸天",
                "age": 23,
                "sex": "男"
            },
            {
                "name": "秀儿",
                "age": 18,
                "sex": "女"
            },
        ]
        return get_return_data(Success, data)