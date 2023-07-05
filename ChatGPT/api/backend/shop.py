from flask_restful import Resource
from common.return_data import get_return_data, Success


class ShopsViewSet(Resource):
    """
    商品CRUD
    """

    def get(self):
        data = [
            {
                "id": 1,
                "name": "夏装女2023新款上衣",
                "oldPrice": "127",
                "newPrice": "89",
                "desc": "非常好看的女款上衣",
                "enable": 1,
                "imageUrl": "https://go-learn.oss-cn-beijing.aliyuncs.com/%E4%B8%8B%E8%BD%BD2.jpeg",
                "inventoryCount": 99090,
                "saleCount": 234,
                "favorCount": 234,
                "address": "上海",
                "categoryId": 1,
                "createAt": "2023-04-23 11:12:34",
                "updateAt": "2023-04-23 11:12:34"
            },
            {
                "id": 2,
                "name": "夏装女2023新款上衣",
                "oldPrice": "127",
                "newPrice": "89",
                "desc": "非常好看的女款上衣",
                "enable": 0,
                "imageUrl": "https://go-learn.oss-cn-beijing.aliyuncs.com/%E4%B8%8B%E8%BD%BD3.jpeg",
                "inventoryCount": 99090,
                "saleCount": 234,
                "favorCount": 234,
                "address": "上海",
                "categoryId": 1,
                "createAt": "2023-04-23 11:12:34",
                "updateAt": "2023-04-23 11:12:34"
            },
            {
                "id": 3,
                "name": "夏装女2023新款上衣",
                "oldPrice": "127",
                "newPrice": "89",
                "desc": "非常好看的女款上衣",
                "enable": 1,
                "imageUrl": "https://go-learn.oss-cn-beijing.aliyuncs.com/%E4%B8%8B%E8%BD%BD4.jpeg",
                "inventoryCount": 99090,
                "saleCount": 234,
                "favorCount": 234,
                "address": "上海",
                "categoryId": 1,
                "createAt": "2023-04-23 11:12:34",
                "updateAt": "2023-04-23 11:12:34"

            },
            {
                "id": 4,
                "name": "夏装女2023新款上衣",
                "oldPrice": "127",
                "newPrice": "89",
                "desc": "非常好看的女款上衣",
                "enable": 1,
                "imageUrl": "https://go-learn.oss-cn-beijing.aliyuncs.com/%E4%B8%8B%E8%BD%BD2.jpeg",
                "inventoryCount": 99090,
                "saleCount": 234,
                "favorCount": 234,
                "address": "上海",
                "categoryId": 1,
                "createAt": "2023-04-23 11:12:34",
                "updateAt": "2023-04-23 11:12:34"
            },
            {
                "id": 5,
                "name": "夏装女2023新款上衣",
                "oldPrice": "127",
                "newPrice": "89",
                "desc": "非常好看的女款上衣",
                "enable": 0,
                "imageUrl": "https://go-learn.oss-cn-beijing.aliyuncs.com/%E4%B8%8B%E8%BD%BD3.jpeg",
                "inventoryCount": 99090,
                "saleCount": 234,
                "favorCount": 234,
                "address": "上海",
                "categoryId": 1,
                "createAt": "2023-04-23 11:12:34",
                "updateAt": "2023-04-23 11:12:34"
            },
            {
                "id": 6,
                "name": "夏装女2023新款上衣",
                "oldPrice": "127",
                "newPrice": "89",
                "desc": "非常好看的女款上衣",
                "enable": 1,
                "imageUrl": "https://go-learn.oss-cn-beijing.aliyuncs.com/%E4%B8%8B%E8%BD%BD4.jpeg",
                "inventoryCount": 99090,
                "saleCount": 234,
                "favorCount": 234,
                "address": "上海",
                "categoryId": 1,
                "createAt": "2023-04-23 11:12:34",
                "updateAt": "2023-04-23 11:12:34"

            },
            {
                "id": 7,
                "name": "夏装女2023新款上衣",
                "oldPrice": "127",
                "newPrice": "89",
                "desc": "非常好看的女款上衣",
                "enable": 1,
                "imageUrl": "https://go-learn.oss-cn-beijing.aliyuncs.com/%E4%B8%8B%E8%BD%BD3.jpeg",
                "inventoryCount": 99090,
                "saleCount": 234,
                "favorCount": 234,
                "address": "上海",
                "categoryId": 1,
                "createAt": "2023-04-23 11:12:34",
                "updateAt": "2023-04-23 11:12:34"
            },
            {
                "id": 8,
                "name": "夏装女2023新款上衣",
                "oldPrice": "127",
                "newPrice": "89",
                "desc": "非常好看的女款上衣",
                "enable": 0,
                "imageUrl": "https://go-learn.oss-cn-beijing.aliyuncs.com/%E4%B8%8B%E8%BD%BD4.jpeg",
                "inventoryCount": 99090,
                "saleCount": 234,
                "favorCount": 234,
                "address": "上海",
                "categoryId": 1,
                "createAt": "2023-04-23 11:12:34",
                "updateAt": "2023-04-23 11:12:34"
            },
            {
                "id": 9,
                "name": "夏装女2023新款上衣",
                "oldPrice": "127",
                "newPrice": "89",
                "desc": "非常好看的女款上衣",
                "enable": 1,
                "imageUrl": "https://go-learn.oss-cn-beijing.aliyuncs.com/%E4%B8%8B%E8%BD%BD2.jpeg",
                "inventoryCount": 99090,
                "saleCount": 234,
                "favorCount": 234,
                "address": "上海",
                "categoryId": 1,
                "createAt": "2023-04-23 11:12:34",
                "updateAt": "2023-04-23 11:12:34"

            },
            {
                "id": 10,
                "name": "夏装女2023新款上衣",
                "oldPrice": "127",
                "newPrice": "89",
                "desc": "非常好看的女款上衣",
                "enable": 1,
                "imageUrl": "https://go-learn.oss-cn-beijing.aliyuncs.com/%E4%B8%8B%E8%BD%BD3.jpeg",
                "inventoryCount": 99090,
                "saleCount": 234,
                "favorCount": 234,
                "address": "上海",
                "categoryId": 1,
                "createAt": "2023-04-23 11:12:34",
                "updateAt": "2023-04-23 11:12:34"

            },
        ]

        return_data = {
            'list': data,
            'totalCount': 12
        }
        return get_return_data(Success, return_data)
