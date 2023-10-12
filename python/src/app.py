from flask import Flask, jsonify, request

tasks = [
    {'id': 1, 'name': 'Task 1'},
    {'id': 2, 'name': 'Task 2'},
    {'id': 3, 'name': 'Task 3'},
    {'id': 4, 'name': 'Task 4'},
    {'id': 5, 'name': 'Task 5'},
    {'id': 6, 'name': 'Task 6'}
]

app = Flask(__name__)


# curl -v http://localhost:5000/tasks
@app.route('/tasks')
def get_tasks():
    return jsonify(tasks)


# curl -v http://localhost:5000/task/1
@app.route('/task/<int:id>')
def get_task(id):
    task_list = [task for task in tasks if task['id'] == id]
    if len(task_list) == 0:
        return f'Task with id {id} not found', 404
    return jsonify(task_list[0])


# curl --header "Content-Type: application/json" --request POST --data '{"name": "Task 7"}' -v http://localhost:5000/task
@app.route('/task', methods=['POST'])
def post_task():
    # Retrieve the task from the request body
    request_task = request.json

    # Generate an ID for the post
    new_id = max([task['id'] for task in tasks]) + 1

    # Create a new task
    new_task = {
        'id': new_id,
        'name': request_task['name']
    }

    # Append the new task to our task list
    tasks.append(new_task)

    # Return the new task back to the client
    return jsonify(new_task), 201


# curl --header "Content-Type: application/json" --request PUT --data '{"name": "Updated Task 2"}' -v http://localhost:5000/task/2
@app.route('/task/<int:id>', methods=['PUT'])
def put_task(id):
    # Get the request payload
    updated_task = request.json

    # Find the task with the specified ID
    for task in tasks:
        if task['id'] == id:
            # Update the task name
            task['name'] = updated_task['name']
            return jsonify(task), 200

    return f'Task with id {id} not found', 404


# curl --request DELETE -v http://localhost:5000/task/3
@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    # Find the task with the specified ID
    task_list = [task for task in tasks if task['id'] == id]
    if len(task_list_list) == 1:
        tasks.remove(task_list[0])
        return f'Task with id {id} deleted', 200

    return f'Task with id {id} not found', 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
