from http import HTTPStatus

from flask import Blueprint, request
from sqlalchemy import inspect
from src.models import Post, db

app = Blueprint('post', __name__, url_prefix = '/posts')
