
def print_env():
    import os
    import openai
    print(f'OPENAI_API_KEY: {os.environ.get("OPENAI_API_KEY")}')
    print(f'openai.api_key: {openai.api_key.replace(openai.api_key[:-4], "**********")}')
    print(f'openai.api_base: {openai.api_base}')
    print(f'openai.api_type: {openai.api_type}')
    print(f'openai.api_version: {openai.api_version}')


