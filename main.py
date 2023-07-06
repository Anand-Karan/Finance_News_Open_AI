import openai
import secret_key

openai.api_key = secret_key.openai_api_key

def poem_on_chicago():
    prompt = "Write a poem on Chicago in 4 lines only."

    response = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo",
                    messages = [
                        {"role":"user", "content": prompt}
                    ]
                )
    print(response.choices[0]['message']['content'])






if __name__ == '__main__':
    poem_on_chicago()