import base64

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()


def extract_text_from_image(
    image_path
):

    with open(image_path, "rb") as image_file:

        base64_image = base64.b64encode(
            image_file.read()
        ).decode("utf-8")

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "user",

                "content": [

                    {
                        "type": "text",

                        "text": (
                            "Extract all text from this "
                            "insurance document image."
                        )
                    },

                    {
                        "type": "image_url",

                        "image_url": {
                            "url": (
                                f"data:image/png;base64,"
                                f"{base64_image}"
                            )
                        }
                    }
                ]
            }
        ],

        max_tokens=3000
    )

    return response.choices[0].message.content