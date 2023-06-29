from flask_restful import Resource
from common.return_data import Success, get_return_data


class UserViewSet(Resource):
    """
    用户CRUD
    """

    def get(self, user_id):
        data = {
            "id": user_id,
            "name": "god",
            "realname": "god" + str(user_id),
            "cellphone": "18812324989",
            "enable": 1,
            "createAt": "2021-01-23: 23:34:11",
            "updateAt": "2021-01-24: 23:34:11",
            "role": {
                "id": 1,
                "name": "超级管理员",
                "intro": "所有权限",
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
            },
            "department": {
                "id": 1,
                "name": "研发部",
                "parentId": None,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                "leader": "god"
            },
        }
        return get_return_data(Success, data)

    def post(self):
        data = {
            "id": 1,
            "name": "god",
            "token": "god chatgpt"
        }
        return get_return_data(Success, data)

    def delete(self):
        return get_return_data(Success)

    def patch(self):
        return get_return_data(Success)


class UsersViewSet(Resource):
    """
    用户批量操作
    """

    def get(self):
        data = [
            {
                "id": 1,
                "name": "god",
                "realname": "god001",
                "cellphone": "18812324989",
                "enable": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                "role": {
                    "id": 1,
                    "name": "超级管理员",
                    "intro": "所有权限",
                    "createAt": "2021-01-23: 23:34:11",
                    "updateAt": "2021-01-24: 23:34:11",
                },
                "department": {
                    "id": 1,
                    "name": "研发部",
                    "parentId": None,
                    "createAt": "2021-01-23: 23:34:11",
                    "updateAt": "2021-01-24: 23:34:11",
                    "leader": "god"
                }
            },
            {
                "id": 2,
                "name": "god",
                "realname": "god002",
                "cellphone": "18612324989",
                "enable": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                "role": {
                    "id": 1,
                    "name": "超级管理员",
                    "intro": "所有权限",
                    "createAt": "2021-01-23: 23:34:11",
                    "updateAt": "2021-01-24: 23:34:11",
                },
                "department": {
                    "id": 1,
                    "name": "研发部",
                    "parentId": None,
                    "createAt": "2021-01-23: 23:34:11",
                    "updateAt": "2021-01-24: 23:34:11",
                    "leader": "god"
                }
            }
        ]
        return get_return_data(Success, data)

    def post(self):
        return get_return_data(Success)

    def delete(self):
        return get_return_data(Success)

    def patch(self):
        return get_return_data(Success)