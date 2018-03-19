import base64
import requests
import jsonpickle
from learn.image_loader import ImageLoader
from learn.const import DATA_DIR


def prepare_request(image):
    with open(image, "rb") as f:
        content = base64.b64encode(f.read())

    data = {
        "requests": [{
            "image": {
                "content": content
            },
            "features": [
                # {"type": "TYPE_UNSPECIFIED", "maxResults": 50},
                # {"type": "LANDMARK_DETECTION", "maxResults": 50},
                # {"type": "FACE_DETECTION", "maxResults": 50},
                # {"type": "LOGO_DETECTION", "maxResults": 50},
                # {"type": "LABEL_DETECTION", "maxResults": 50},
                {"type": "TEXT_DETECTION", "maxResults": 50},
                {"type": "DOCUMENT_TEXT_DETECTION", "maxResults": 50},
                # {"type": "SAFE_SEARCH_DETECTION", "maxResults": 50},
                # {"type": "IMAGE_PROPERTIES", "maxResults": 50},
                # {"type": "CROP_HINTS", "maxResults": 50},
                # {"type": "WEB_DETECTION", "maxResults": 50}
            ],
            "imageContext": {
                "cropHintsParams": {
                    "aspectRatios": [0.8, 1, 1.2]
                }
            }
        }]
    }
    return data


if __name__ == "__main__":
    images = ImageLoader(DATA_DIR)
    for image in images.files[:1]:
        request = prepare_request(image)
        response = requests.post(
            "https://cxl-services.appspot.com/proxy",
            params={"url": "https://vision.googleapis.com/v1/images:annotate"},
            json=request
        )
        print(image, response, response.content, jsonpickle.encode(response))
