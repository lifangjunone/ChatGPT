from flask_restful import Resource
from common.return_data import Success, get_return_data


class PermissionViewSet(Resource):
    """
    用户权限CRUD
    """

    def get(self, id):
        data = [
            {
                "children": [
                    {
                        "children": [
                            {"permission": "system:overview:create", "type": 3},
                            {"permission": "system:overview:delete", "type": 3},
                            {"permission": "system:overview:update", "type": 3},
                            {"permission": "system:overview:query", "type": 3},
                        ],
                        "icon": "\ue658",
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
                        "children": [
                            {"permission": "system:user:create", "type": 3},
                            {"permission": "system:user:delete", "type": 3},
                            {"permission": "system:user:update", "type": 3},
                            {"permission": "system:user:query", "type": 3},
                        ],
                        "icon": "\ue8c8",
                        "id": 5,
                        "name": "用户管理",
                        "parentId": 2,
                        "sort": 1,
                        "type": 2,
                        "url": "/main/system/user",
                    },
                    {
                        "children": [
                            {"permission": "system:department:create", "type": 3},
                            {"permission": "system:department:delete", "type": 3},
                            {"permission": "system:department:update", "type": 3},
                            {"permission": "system:department:query", "type": 3},
                        ],
                        "icon": "\ue608",
                        "id": 6,
                        "name": "部门管理",
                        "parentId": 2,
                        "sort": 3,
                        "type": 2,
                        "url": "/main/system/department"
                    },
                    {
                        "children": [
                            {"permission": "system:menu:create", "type": 3},
                            {"permission": "system:menu:delete", "type": 3},
                            {"permission": "system:menu:update", "type": 3},
                            {"permission": "system:menu:query", "type": 3},
                        ],
                        "icon": "\ue64d",
                        "id": 7,
                        "name": "菜单管理",
                        "parentId": 2,
                        "sort": 4,
                        "type": 2,
                        "url": "/main/system/menu"
                    },
                    {
                        "children": [
                            {"permission": "system:role:create", "type": 3},
                            {"permission": "system:role:delete", "type": 3},
                            {"permission": "system:role:update", "type": 3},
                            {"permission": "system:role:query", "type": 3},
                        ],
                        "icon": "\ue6a0",
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
                        "children": [
                            {"permission": "system:category:create", "type": 3},
                            {"permission": "system:category:delete", "type": 3},
                            {"permission": "system:category:update", "type": 3},
                            {"permission": "system:category:query", "type": 3},
                        ],
                        "icon": "\ue603",
                        "id": 10,
                        "name": "商品类别",
                        "parentId": 9,
                        "sort": 1,
                        "type": 2,
                        "url": "/main/product/category"
                    },
                    {
                        "children": [
                            {"permission": "system:shop:create", "type": 3},
                            {"permission": "system:shop:delete", "type": 3},
                            {"permission": "system:shop:update", "type": 3},
                            {"permission": "system:shop:query", "type": 3},
                        ],
                        "icon": "\ue62b",
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
                        "children": [
                            {"permission": "system:chat:create", "type": 3},
                            {"permission": "system:chat:delete", "type": 3},
                            {"permission": "system:chat:update", "type": 3},
                            {"permission": "system:chat:query", "type": 3},
                        ],
                        "icon": "\ueaf5",
                        "id": 13,
                        "name": "你的故事",
                        "parentId": 12,
                        "sort": 1,
                        "type": 2,
                        "url": "/main/story/chat"
                    },
                    {
                        "children": [
                            {"permission": "system:story:create", "type": 3},
                            {"permission": "system:story:delete", "type": 3},
                            {"permission": "system:story:update", "type": 3},
                            {"permission": "system:story:query", "type": 3},
                        ],
                        "icon": "\ue624",
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


class PermissionsViewSet(Resource):
    """
    用户角色批量操作
    """

    def get(self):
        data = [
            {"id": 1, "name": "超级管理员", "intro": "所有权限", "createAt": "2023-03-23 22:23:22"},
            {"id": 2, "name": "运营", "intro": "日常事务", "createAt": "2023-03-23 22:23:22"},
            {"id": 3, "name": "人事", "intro": "所有权限", "createAt": "2023-03-23 22:23:22"},
            {"id": 4, "name": "前端", "intro": "所有权限", "createAt": "2023-03-23 22:23:22"},
            {"id": 5, "name": "后端", "intro": "所有权限", "createAt": "2023-03-23 22:23:22"},
            {"id": 6, "name": "算法", "intro": "所有权限", "createAt": "2023-03-23 22:23:22"},
            {"id": 7, "name": "UI设计", "intro": "所有权限", "createAt": "2023-03-23 22:23:22"}
        ]
        return_data = {
            'list': data,
            'totalCount': 12
        }
        return get_return_data(Success, return_data)