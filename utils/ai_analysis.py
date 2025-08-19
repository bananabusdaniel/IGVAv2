import openai
import base64
from pathlib import Path
import os
from dotenv import load_dotenv

DELIMITER = "####"

images_data = [{}]
bio = ...

system_message = "Here you write the role of GPT in returning the response as requested"

'''
Example of User message
{
        "type": "image_url",
        "photo": "post"
        "caption": image.caption
        "image_url": {
            "url": f"data:image/jpeg;base64,{encode_image('image1.jpg')}"
        }
    },
    {
        "type": "image_url",
        "photo": "profile"
        "caption": image.caption - if relevant.
        "image_url": {
            "url": f"data:image/jpeg;base64,{encode_image('image2.jpg')}"
        }
}
'''

#Defines GPT Client and connects through API Key
def chatgpt_setup():
    openai.api_key = os.environ["OPENAI_API_KEY"]
    # Declare global client
    global client
    client = openai.OpenAI()

# returns API response: concatanates model messages and calls helper function
def prompt_gpt(user_message, system_message):
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{DELIMITER}{user_message}{DELIMITER}"},
    ]
    return get_completion(messages)

# returns API response: helper function with request to GPT's API
def get_completion(messages, temperature=0, max_completion_tokens=None):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=temperature,
        max_completion_tokens=max_completion_tokens,
    )
    return response.choices[0].message.content

#Concatanate all this data, give ChatGPT role and have it return JSON with specific keys.

def concatanate_profile_data_to_user_message():... 

def isFemale():
    load_dotenv() #????
    chatgpt_setup()
    global ai_profile_data
    ai_profile_data = prompt_gpt(concatanate_profile_data_to_user_message(), system_message)
    # return ai_profile_data.isFemale

#returns binary image for openai
def encode_image(image_path):
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")
    
def add_image_b64(image_folder_path: str):
    for image in os.listdir(image_folder_path):
        if image.lower().endswith((".png", ".jpg", ".jpeg")):
            full_path = os.path.join(image_folder_path, image)
            b64 = encode_image(full_path)

    
