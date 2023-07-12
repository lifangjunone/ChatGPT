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


class ShopsCategorySaleViewSet(Resource):
    """
    商品分类数量
    """
    def get(self):
        data = [
            {
                "id": 1,
                "name": "上衣",
                "goodsCount": 142323,
            },
            {
                "id": 2,
                "name": "下衣",
                "goodsCount": 2423432,
            },
            {
                "id": 3,
                "name": "T恤",
                "goodsCount": 723523,
            },
            {
                "id": 4,
                "name": "防晒衣",
                "goodsCount": 4423432,
            },
            {
                "id": 5,
                "name": "短裤",
                "goodsCount": 3923432,
            },
            {
                "id": 6,
                "name": "风衣",
                "goodsCount": 932433,
            },
        ]
        return get_return_data(Success, data)


class ShopsCategoryCountViewSet(Resource):
    """
    商品销量
    """
    def get(self):
        data = [
            {
                "id": 1,
                "name": "上衣",
                "goodsCount": 14,
            },
            {
                "id": 2,
                "name": "下衣",
                "goodsCount": 24,
            },
            {
                "id": 3,
                "name": "T恤",
                "goodsCount": 7,
            },
            {
                "id": 4,
                "name": "防晒衣",
                "goodsCount": 44,
            },
            {
                "id": 5,
                "name": "短裤",
                "goodsCount": 39,
            },
            {
                "id": 6,
                "name": "风衣",
                "goodsCount": 9,
            },
        ]
        return get_return_data(Success, data)


class ShopsCategoryFavorViewSet(Resource):
    """
    商品收藏
    """
    def get(self):
        data = [
            {
                "id": 1,
                "name": "上衣",
                "goodsCount": 13244,
            },
            {
                "id": 2,
                "name": "下衣",
                "goodsCount": 24324,
            },
            {
                "id": 3,
                "name": "T恤",
                "goodsCount": 3437,
            },
            {
                "id": 4,
                "name": "防晒衣",
                "goodsCount": 4344,
            },
            {
                "id": 5,
                "name": "短裤",
                "goodsCount": 339,
            },
            {
                "id": 6,
                "name": "风衣",
                "goodsCount": 9434,
            },
        ]
        return get_return_data(Success, data)


class ShopsCitySaleViewSet(Resource):
    """
    商品在不同城市的销量
    """
    def get(self):
        data = [
            {
                "address": "北京",
                "goodsCount": 13244,
            },
            {
                "address": "上海",
                "goodsCount": 23244,
            },
            {
                "address": "广州",
                "goodsCount": 44244,
            },
            {
                "address": "深圳",
                "goodsCount": 32244,
            },
            {
                "address": "天津",
                "goodsCount": 99244,
            },
            {
                "address": "杭州",
                "goodsCount": 77244,
            },
        ]
        return get_return_data(Success, data)