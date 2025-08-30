import os
from dotenv import load_dotenv

load_dotenv()

Api_Key = os.getenv('my_api')

print(Api_Key)