from flask_restful import Resource
from common.return_data import get_return_data, Success


class DepartmentsViewSet(Resource):
    """
    部门批量操作
    """

    def get(self):
        data = [
            {
                "id": 1,
                "name": "人事部",
                "leader": "李天霸",
                "parentId": None,
                "createAt": "2023-02-23 12:23:33",
                "updateAt": "2023-03-23 12:34:33"
            },
            {
                "id": 2,
                "name": "市场部",
                "leader": "赵日天",
                "parentId": None,
                "createAt": "2023-02-23 12:23:33",
                "updateAt": "2023-03-23 12:34:33"
            },
            {
                "id": 3,
                "name": "研发部",
                "leader": "李研发",
                "parentId": 2,
                "createAt": "2023-02-23 12:23:33",
                "updateAt": "2023-03-23 12:34:33"
            },
            {
                "id": 4,
                "name": "运维部",
                "leader": "栾天刀",
                "parentId": 3,
                "createAt": "2023-02-23 12:23:33",
                "updateAt": "2023-03-23 12:34:33"
            },
        ]
        return_data = {
            'list': data,
            'totalCount': 12
        }
        return get_return_data(Success, return_data)