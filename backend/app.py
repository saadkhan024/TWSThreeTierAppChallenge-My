import os
from flask import Flask
from flask_cors import CORS
from routes.tasks import tasks
from db import connection

app = Flask(__name__)
CORS(app)

# Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "*"}})

connection()

@app.route('/ok')
def ok():
    return 'ok', 200

app.register_blueprint(tasks, url_prefix='/api/tasks')

port = int(os.environ.get('PORT', 8080))
app.run(host='0.0.0.0', port=port)

