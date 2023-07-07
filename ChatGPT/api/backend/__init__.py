from flask_restful import Api
from flask import Blueprint
from .test import TestViewSet
from .login import LoginViewSet
from .user import UserViewSet, UsersViewSet
from .role import RolesViewSet, RoleViewSet
from .shop import ShopsViewSet
from .menu import MenusViewSet
from .department import DepartmentsViewSet


backend_manage_bp = Blueprint("backend_manage", __name__)
backend_manage = Api(backend_manage_bp, catch_all_404s=True)
backend_manage.add_resource(TestViewSet, "/test")
backend_manage.add_resource(LoginViewSet, "/login")
backend_manage.add_resource(UserViewSet, "/user/<int:id>", "/user")
backend_manage.add_resource(UsersViewSet, "/users")
backend_manage.add_resource(RoleViewSet, "/role/<int:id>", "/role")
backend_manage.add_resource(RolesViewSet, "/roles")
backend_manage.add_resource(ShopsViewSet, "/shops")
backend_manage.add_resource(MenusViewSet, "/menus")
backend_manage.add_resource(DepartmentsViewSet, "/departments")
