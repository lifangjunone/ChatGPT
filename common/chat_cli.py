
import openai
from conf.default import BaseConfig


class ChatGPTCli:

    def __init__(self, model='gpt-3.5-turbo', role='user'):
        self.model = model
        self.role = role
        self._openai = self.config_openai()

    @classmethod
    def config_openai(cls):
        openai.api_key = BaseConfig.OPENAI_API_KEY
        openai.proxy = BaseConfig.HOST_IP + ":" + str(BaseConfig.PROXY_PROT)
        return openai

    def get_result(self, question='hello'):
        res = self._openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": self.role,
                    "content": question}
            ])
        return res.choices[0].message.content

    def get_stream_result(self, question='hello'):
        res = self._openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": self.role,
                    "content": question}
            ],
            stream=True
        )
        return res


ChatCli = ChatGPTCli()
