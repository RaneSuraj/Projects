from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Defaults to localhost if not running in a container, but expects a database URI via environment variable
default_db_uri = 'postgresql://admin:password123@localhost:5432/microapp_db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', default_db_uri)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# Initialize tables
with app.app_context():
    db.create_all()

# API Endpoints
@app.route('/api/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([{'id': m.id, 'content': m.content} for m in messages])

@app.route('/api/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    if not data or not data.get('content'):
        return jsonify({'error': 'Content is required'}), 400
        
    new_message = Message(content=data['content'])
    db.session.add(new_message)
    db.session.commit()
    
    return jsonify({'id': new_message.id, 'content': new_message.content}), 201

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# Adding comment to check if linter workflow working or not
if __name__ == '__main__':
    # Backend runs on port 5001
    app.run(host='0.0.0.0', port=5001)
