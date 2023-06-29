from flask_restful import Resource
from common.return_data import Success, get_return_data


class PermissionViewSet(Resource):
    """
    用户权限CRUD
    """

    def get(self, role_id):
        data = [
            {
                "children": [
                    {
                        "children": None,
                        "id": 2,
                        "name": "核心技术",
                        "parentId": 1,
                        "sort": 1,
                        "type": 2,
                        "url": "/main/analysis/overview"
                    },
                    {
                        "children": None,
                        "id": 3,
                        "name": "核心技术",
                        "parentId": 1,
                        "sort": 2,
                        "type": 2,
                        "url": "/main/analysis/overview"
                    }
                ],
                "icon": "el-icon-monitor",
                "id": 1,
                "name": "系统总览",
                "sort": 1,
                "type": 1,
                "url": "/main/analysis1"
            },
            {
                "children": [
                    {
                        "children": None,
                        "id": 4,
                        "name": "核心技术",
                        "parentId": 2,
                        "sort": 1,
                        "type": 2,
                        "url": "/main/analysis/overview"
                    },
                    {
                        "children": None,
                        "id": 5,
                        "name": "核心技术",
                        "parentId": 2,
                        "sort": 2,
                        "type": 2,
                        "url": "/main/analysis/overview"
                    }
                ],
                "icon": "el-icon-monitor",
                "id": 2,
                "name": "系统总览",
                "sort": 2,
                "type": 1,
                "url": "/main/analysis"
            }
        ]
        return get_return_data(Success, data)

    def post(self):
        return get_return_data(Success, {})

    def delete(self):
        return get_return_data(Success)

    def patch(self):
        return get_return_data(Success)