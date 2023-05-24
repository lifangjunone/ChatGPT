"""
@api {post} /api/v2/users 注册
@apiVersion 2.0.0
@apiName register_user
@apiGroup Users
@apiDescription 手机用户注册
@apiParam {String} mobile 用户手机号
@apiParam {String} password 用户密码
@apiParam {String} sms_code 用户短信验证码
@apiParam {String} [remark] 备注信息
@apiParamExample {json} Request-Example:
 {
  mobile: "13000000000",
  password: "123456",
  sms_code: "907896"
 }
@apiSuccess (回参) {int} user_id 用户注册id
@apiSuccess (回参) {String} name 用户昵称
@apiSuccess (回参) {String} mobile 用户注册手机号
@apiSuccess (回参) {String} avatar 用户头像地址
@apiSuccess (回参) {String} create_time 用户创建时间
@apiSuccessExample {json} Success-Response:
 {
  "error_code": 0,
  "error_msg": "注册成功！",
  "data": {
   "user_id": 1,
   "name": "jizhen",
   "mobile": "13000000000",
   "avatar": "http://xxxxx",
   "create_time": "2018-1-1 12:12:12"
  }
 }
@apiErrorExample {json} Error-Response:
 {
  "error_code":4001,
  "error_msg":"数据库查询错误！"
 }
"""
