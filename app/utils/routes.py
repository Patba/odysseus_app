from flask import Blueprint
from app import db, bcrypt

utils = Blueprint("utils", __name__)

