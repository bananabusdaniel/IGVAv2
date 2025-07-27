import openai
import base64
from pathlib import Path
import os

images_data = [{}]
bio = ...
'''
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

#Concatanate all this data, give ChatGPT role and have it return JSON with specific keys.

#returns binary image for openai
def encode_image(image_path):
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")
    
def add_image_b64(image_folder_path: str):
    for image in os.listdir(image_folder_path):
        if image.lower().endswith((".png", ".jpg", ".jpeg")):
            full_path = os.path.join(image_folder_path, image)
            b64 = encode_image(full_path)

    
