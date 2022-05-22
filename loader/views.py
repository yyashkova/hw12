import logging
import json

from flask import Blueprint, render_template, request
from main import utils
from loader.utils import *
from config import POST_PATH

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route("/post", methods=["GET"])
def create_new_post_page():
    return render_template("post_form.html")

@loader_blueprint.route("/post", methods=["POST"])
def create_new_post_by_user():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Нет части информации")
        return "Данных тут нет"

    posts = utils.load_json_data(POST_PATH)

    try:
        new_post = {"pic": save_picture(picture), "content": content}
    except WrongImgType:
        return "Неверный тип этот ваш файл"
    add_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)


