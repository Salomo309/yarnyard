from flask import Blueprint
from controllers.todolistControllers import TodolistControllers

todolistRoutes = Blueprint("todolistRoutes", __name__)

# todolistRoutes.route("/", methods=["GET"])(TodolistControllers.getTodolist)
@todolistRoutes.route("/", methods=["GET"])
def get_todolists():
    return TodolistControllers.getTodolist()

@todolistRoutes.route("/<int:idTanaman>", methods=["GET"])
def get_tanaman(idTanaman):
    return TodolistControllers.getTodolistByIdTanaman(idTanaman)

@todolistRoutes.route("/deletetodolist/<int:idTDL>", methods=["DELETE"])
def delete_todolist(idTDL):
    return TodolistControllers.deleteTodolistByIdTDL(idTDL)
