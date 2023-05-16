from flask import Blueprint
import pandas as pd

from ...app import mysql


deals_list = Blueprint("deals_list",__name__)

