from datetime import datetime
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
                "name": "票氏集团票少",
                "realname": "god001",
                "cellphone": "18812324989",
                "enable": 0,
                "department_Id": 1,
                "roleId": 1,
                "createAt": str(datetime.now()),
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 2,
                "name": "李氏集团李少",
                "realname": "god002",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23T23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 3,
                "name": "刘氏集团刘少",
                "realname": "god003",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 4,
                "name": "策氏集团策少",
                "realname": "god004",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 5,
                "name": "王氏集团王少",
                "realname": "god005",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 6,
                "name": "向氏集团向少",
                "realname": "god006",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 7,
                "name": "杨氏集团杨少",
                "realname": "god007",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 8,
                "name": "高氏集团高少",
                "realname": "god008",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 9,
                "name": "叶氏集团叶少",
                "realname": "god009",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 10,
                "name": "俞氏集团俞少",
                "realname": "god010",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 11,
                "name": "冯氏集团冯少",
                "realname": "god011",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            },
            {
                "id": 12,
                "name": "唐氏集团唐少",
                "realname": "god012",
                "cellphone": "18612324989",
                "enable": 1,
                "department_Id": 1,
                "roleId": 1,
                "createAt": "2021-01-23: 23:34:11",
                "updateAt": "2021-01-24: 23:34:11",
                # "role": {
                #     "id": 1,
                #     "name": "超级管理员",
                #     "intro": "所有权限",
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                # },
                # "department": {
                #     "id": 1,
                #     "name": "研发部",
                #     "parentId": None,
                #     "createAt": "2021-01-23: 23:34:11",
                #     "updateAt": "2021-01-24: 23:34:11",
                #     "leader": "god"
                # }
            }
        ]
        return_data = {
            'list': data,
            'totalCount': 12
        }
        return get_return_data(Success, return_data)

    def post(self):
        return get_return_data(Success)

    def delete(self):
        return get_return_data(Success)

    def patch(self):
        return get_return_data(Success)