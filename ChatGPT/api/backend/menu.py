from flask_restful import Resource
from common.return_data import get_return_data, Success


class MenusViewSet(Resource):
    """
    菜单CRUD
    """
    def get(self):
        data = [
            {

                "children": [
                    {
                        "icon": "\ue66c",
                        "children": None,
                        "id": 4,
                        "name": "商品统计",
                        "parentId": 1,
                        "sort": 2,
                        "type": 2,
                        "url": "/main/analysis/dashboard"
                    },
                    {
                        "children": [
                            {"permission": "system:overview:create", "type": 3, "name": "创建核心技术", "id": 1},
                            {"permission": "system:overview:delete", "type": 3, "name": "删除核心技术", "id": 2},
                            {"permission": "system:overview:update", "type": 3, "name": "修改核心技术", "id": 3},
                            {"permission": "system:overview:query", "type": 3, "name": "查看核心技术", "id": 4},
                        ],
                        "icon": "\ue658",
                        "id": 3,
                        "name": "核心技术",
                        "parentId": 1,
                        "sort": 1,
                        "type": 2,
                        "url": "/main/analysis/overview"
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
                            {"permission": "system:user:create", "type": 3, "name": "创建用户", "id": 5},
                            {"permission": "system:user:delete", "type": 3, "name": "删除用户", "id": 6},
                            {"permission": "system:user:update", "type": 3, "name": "修改用户", "id": 7},
                            {"permission": "system:user:query", "type": 3, "name": "查看用户", "id": 8},
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
                            {"permission": "system:department:create", "type": 3, "name": "创建部门", "id": 9},
                            {"permission": "system:department:delete", "type": 3, "name": "删除部门", "id": 10},
                            {"permission": "system:department:update", "type": 3, "name": "修改部门", "id": 11},
                            {"permission": "system:department:query", "type": 3, "name": "查看部门", "id": 12},
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
                            {"permission": "system:menu:create", "type": 3, "name": "创建菜单", "id": 13},
                            {"permission": "system:menu:delete", "type": 3, "name": "删除菜单", "id": 14},
                            {"permission": "system:menu:update", "type": 3, "name": "修改菜单", "id": 15},
                            {"permission": "system:menu:query", "type": 3, "name": "查看菜单", "id": 16},
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
                            {"permission": "system:role:create", "type": 3, "name": "创建角色", "id": 17},
                            {"permission": "system:role:delete", "type": 3, "name": "删除角色", "id": 18},
                            {"permission": "system:role:update", "type": 3, "name": "修改角色", "id": 19},
                            {"permission": "system:role:query", "type": 3, "name": "查看角色", "id": 20},
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
                            {"permission": "system:category:create", "type": 3, "name": "创建商品类别", "id": 21},
                            {"permission": "system:category:delete", "type": 3, "name": "删除商品类别", "id": 22},
                            {"permission": "system:category:update", "type": 3, "name": "修改商品类别", "id": 23},
                            {"permission": "system:category:query", "type": 3, "name": "查看商品类别", "id": 24},
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
                            {"permission": "system:shop:create", "type": 3, "name": "创建商品", "id": 25},
                            {"permission": "system:shop:delete", "type": 3, "name": "删除商品", "id": 26},
                            {"permission": "system:shop:update", "type": 3, "name": "修改商品", "id": 27},
                            {"permission": "system:shop:query", "type": 3, "name": "查看商品", "id": 28},
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
                            {"permission": "system:chat:create", "type": 3, "name": "创建故事", "id": 29},
                            {"permission": "system:chat:delete", "type": 3, "name": "删除故事", "id": 30},
                            {"permission": "system:chat:update", "type": 3, "name": "修改故事", "id": 31},
                            {"permission": "system:chat:query", "type": 3, "name": "查看故事", "id": 32},
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
                            {"permission": "system:story:create", "type": 3, "name": "创建故事列表", "id": 33},
                            {"permission": "system:story:delete", "type": 3, "name": "删除故事列表", "id": 34},
                            {"permission": "system:story:update", "type": 3, "name": "修改故事列表", "id": 35},
                            {"permission": "system:story:query", "type": 3, "name": "查看故事列表", "id": 36},
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
        return_data = {
            'list': data,
            'totalCount': 12
        }
        return get_return_data(Success, return_data)