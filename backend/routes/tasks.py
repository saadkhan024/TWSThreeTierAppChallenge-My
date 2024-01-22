from flask import Blueprint, request, jsonify
from models.task import Task

tasks = Blueprint('tasks', __name__)

@tasks.route("/", methods=["POST"])
def create_task():
    try:
        task_data = request.get_json()
        task = Task(**task_data).save()
        return jsonify(task), 201
    except Exception as error:
        return jsonify({"error": str(error)}), 500

@tasks.route("/", methods=["GET"])
def get_tasks():
    try:
        tasks = Task.objects().to_json()
        return jsonify(tasks)
    except Exception as error:
        return jsonify({"error": str(error)}), 500

@tasks.route("/<id>", methods=["PUT"])
def update_task(id):
    try:
        Task.objects.get(id=id).update(**request.get_json())
        return jsonify({"message": "Task updated successfully"})
    except Exception as error:
        return jsonify({"error": str(error)}), 500

@tasks.route("/<id>", methods=["DELETE"])
def delete_task(id):
    try:
        task = Task.objects.get(id=id).delete()
        return jsonify(task)
    except Exception as error:
        return jsonify({"error": str(error)}), 500

