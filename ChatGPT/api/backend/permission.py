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
                        "icon": "\ue658",
                        "children": None,
                        "id": 3,
                        "name": "核心技术",
                        "parentId": 1,
                        "sort": 1,
                        "type": 2,
                        "url": "/main/analysis/overview"
                    },
                    {
                        "icon": "\ue66c",
                        "children": None,
                        "id": 4,
                        "name": "商品统计",
                        "parentId": 1,
                        "sort": 2,
                        "type": 2,
                        "url": "/main/analysis/dashboard"
                    }
                ],
                "icon": "\ue612",
                "id": 1,
                "name": "系统总览",
                "sort": 1,
                "type": 1,
                "url": "/main/analysis"
            },
            {
                "children": [
                    {
                        "icon": "\ue8c8",
                        "children": None,
                        "id": 5,
                        "name": "用户管理",
                        "parentId": 2,
                        "sort": 1,
                        "type": 2,
                        "url": "/main/system/user"
                    },
                    {
                        "icon": "\ue608",
                        "children": None,
                        "id": 6,
                        "name": "部门管理",
                        "parentId": 2,
                        "sort": 3,
                        "type": 2,
                        "url": "/main/system/department"
                    },
                    {
                        "icon": "\ue64d",
                        "children": None,
                        "id": 7,
                        "name": "菜单管理",
                        "parentId": 2,
                        "sort": 4,
                        "type": 2,
                        "url": "/main/system/menu"
                    },
                    {
                        "icon": "\ue6a0",
                        "children": None,
                        "id": 8,
                        "name": "角色管理",
                        "parentId": 2,
                        "sort": 5,
                        "type": 2,
                        "url": "/main/system/role"
                    }
                ],
                "icon": "\ue617",
                "id": 2,
                "name": "系统管理",
                "sort": 2,
                "type": 1,
                "url": "/main/system"
            },
            {
                "children": [
                    {
                        "icon": "\ue603",
                        "children": None,
                        "id": 10,
                        "name": "商品类别",
                        "parentId": 9,
                        "sort": 1,
                        "type": 2,
                        "url": "/main/product/category"
                    },
                    {
                        "icon": "\ue62b",
                        "children": None,
                        "id": 11,
                        "name": "商品信息",
                        "parentId": 9,
                        "sort": 3,
                        "type": 2,
                        "url": "/main/product/goods"
                    }
                ],
                "icon": "\ue60a",
                "id": 9,
                "name": "商品中心",
                "sort": 3,
                "type": 1,
                "url": "/main/product"
            },
            {
                "children": [
                    {
                        "icon": "\ueaf5",
                        "children": None,
                        "id": 13,
                        "name": "你的故事",
                        "parentId": 12,
                        "sort": 1,
                        "type": 2,
                        "url": "/main/story/chat"
                    },
                    {
                        "icon": "\ue624",
                        "children": None,
                        "id": 14,
                        "name": "故事列表",
                        "parentId": 12,
                        "sort": 2,
                        "type": 2,
                        "url": "/main/story/list"
                    }
                ],
                "icon": "\ue638",
                "id": 12,
                "name": "随便聊聊",
                "sort": 4,
                "type": 1,
                "url": "/main/story"
            }
        ]
        return get_return_data(Success, data)

    def post(self):
        return get_return_data(Success, {})

    def delete(self):
        return get_return_data(Success)

    def patch(self):
        return get_return_data(Success)