import os
from openai import OpenAI

class OpenAIAPIClient:

    def __init__(self):
        self.client = lient = OpenAI(
        api_key=os.environ['OPENAI_API_KEY']
    )

    def communicate(self, system_prompt='', model='gpt-4o-mini'):
        messages = [
            {'role': 'system', 'content': system_prompt},
        ]
        while True:
            prompt = input('> ')
            current_message = {'role': 'user', 'content': prompt}
            messages.append(current_message)
            response = self.client.chat.completions.create(
                model=model,
                messages=messages
            )
            print(response)
            reply = response.choices[0].message.content
            reply_message = {'role': 'assistant', 'content': reply}
            messages.append(reply_message)
            print('*-*-* history *-*-*')
            for msg in messages:
                print(msg)


def main():
    client = OpenAIAPIClient()
    client.communicate()


if __name__ == "__main__":
    main()
