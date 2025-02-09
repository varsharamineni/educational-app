import argparse
import os
from huggingface_hub import InferenceClient

def get_response(system_text: str, user_text: str, model: str="meta-llama/Llama-3.2-3B-Instruct"):

    HF_TOKEN = os.getenv("HF_TOKEN")

    client = InferenceClient(api_key=HF_TOKEN, model=model)
    
    messages = [{"role": "system", "content": system_text},
                 {"role": "user", "content": user_text}] 

    response = client.chat_completion(messages)
    breakpoint()

    return response.choices[0].message.content
    # parameters= {"return_full_text": False}}

    # response = requests.post(API_URL, json=payload, headers=headers)
    
    # if response.status_code == 200:
    #     generated_text = response.json()[0]['generated_text']

    # else: 
    #     raise Exception("Something went wrong, try again")

    # return generated_text


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--system_text",
        help="The system text to prompt the model with", type=str)

    parser.add_argument("--user_text",
        help="The user text to prompt the model with", type=str)

    args = parser.parse_args()

    system_text = args.system_text
    user_text = args.user_text

    print(get_response(system_text, user_text))


