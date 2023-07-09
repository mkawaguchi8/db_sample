import os

from dotenv import load_dotenv

load_dotenv()

print(os.environ["SECRET"])
print(os.environ.get("SECRET2"))  # 2つ目のコードで実行することが多い
