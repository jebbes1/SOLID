from flask import Flask, jsonify

app = Flask(__name__)

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name)
        self.admin_level = admin_level

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = Admin(user_id, "Jane Doe", 5)  # Using Admin class, but behaving like User
    return jsonify({'id': user.user_id, 'name': user.name})

if __name__ == '__main__':
    app.run(debug=True)
