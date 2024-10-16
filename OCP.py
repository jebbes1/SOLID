from flask import Flask, jsonify

app = Flask(__name__)

# Open for extension, closed for modification
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class UserSerializer:
    def serialize(self, user):
        return {'id': user.user_id, 'name': user.name}

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = User(user_id, "John Doe")
    return jsonify(UserSerializer().serialize(user))

if __name__ == '__main__':
    app.run(debug=True)
