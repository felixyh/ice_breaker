# from dotenv import load_dotenv
import os

# load_dotenv()

# Access the environment variables
api_key = os.getenv('OPENAI_API_KEY')

# api_key = os.environ['OPENAI_API_KEY']

if __name__ == '__main__':
    print('hello, world!')
    print(f"API Key: {api_key}")