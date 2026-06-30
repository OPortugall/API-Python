from flask import Blueprint, request
from src.app import Post, db
from http import HTTPStatus
from sqlalchemy import inspect

app = Blueprint('post', __name__, url_prefix = '/posts')