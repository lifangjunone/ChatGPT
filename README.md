# ChatGPT
This is ChatGPT project

## quick start 

### Chat api

**A brief description：** 
> This interface returns the interface of chatGPT
- chat api

**Request URL：** 
- ` http://ip:port/api/chat_manage/message/stream?message=xxx`
  
**Request Method：**
- GET 

**Params：** 

| param name | type   | illustrate |
|:-----------|:-------|-----------|
| message    | string | question          |

 **返回示例**

``` json
{
    "msg": "Successful",
    "code": 10000,
    "data": "Go, also known as Golang, is a programming language developed by Google in 2007. It is designed to be fast
}

```

 **Return Params** 

| param name | type    | illustrate     |
|:-----  |:--------|----------------|
|msg | string  | error info     |
|code | integer | status code    |
|data | json    | chatGPT answer |

