import os

import zai
from zai import ZhipuAiClient

print(zai.__version__)

# 从环境变量读取 API Key
client = ZhipuAiClient(api_key=os.getenv("ZAI_API_KEY"))

# 或者直接使用（如果已设置环境变量）
client = ZhipuAiClient()
