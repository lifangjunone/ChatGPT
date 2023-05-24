

import openai
openai.api_key = "xxx"
openai.proxy='127.0.0.1:7890'
# list models

# create a chat completion
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

# print the chat completion
print(chat_completion.choices[0].message.content)