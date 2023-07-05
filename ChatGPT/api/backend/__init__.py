from flask_restful import Api
from flask import Blueprint
from .test import TestViewSet
from .login import LoginViewSet
from .user import UserViewSet, UsersViewSet
from .permission import PermissionViewSet, PermissionsViewSet
from .shop import ShopsViewSet


backend_manage_bp = Blueprint("backend_manage", __name__)
backend_manage = Api(backend_manage_bp, catch_all_404s=True)
backend_manage.add_resource(TestViewSet, "/test")
backend_manage.add_resource(LoginViewSet, "/login")
backend_manage.add_resource(UserViewSet, "/user/<int:user_id>")
backend_manage.add_resource(UsersViewSet, "/users")
backend_manage.add_resource(PermissionViewSet, "/role/<int:role_id>")
backend_manage.add_resource(PermissionsViewSet, "/roles")
backend_manage.add_resource(ShopsViewSet, "/shops")
