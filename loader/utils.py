from config import UPLOAD_FOLDER, POST_PATH
from exceptions import WrongImgType
import json


def save_picture(picture):
    allowed_type = ["jpg", "png", "jpeg"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in allowed_type:
        raise WrongImgType("Не тот форматик файла")
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)

    return picture_path


def add_post(post_list, post):
    post_list.append(post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(post_list, file)
