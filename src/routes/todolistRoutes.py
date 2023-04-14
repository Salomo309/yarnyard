from flask import Blueprint
from controllers.todolistControllers import TodolistControllers

todolistRoutes = Blueprint("todolistRoutes", __name__)

todolistRoutes.route("/", methods=["GET"])(TodolistControllers.getTodolist)
# todolistRoutes.route("/<int:id>", methods=["GET"])(TodolistControllers.getTodolistByID)