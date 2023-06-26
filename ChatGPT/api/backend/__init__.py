from flask_restful import Api
from flask import Blueprint
from .test_api import TestViewSet


backend_manage_bp = Blueprint("backend_manage", __name__)
backend_manage = Api(backend_manage_bp, catch_all_404s=True)
backend_manage.add_resource(TestViewSet, "/test")
