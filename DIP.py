from flask import Flask, jsonify

app = Flask(__name__)

# Abstraction (interface)
class UserRepository:
    def get_user(self, user_id):
        pass

# Low-level module
class DatabaseUserRepository(UserRepository):
    def get_user(self, user_id):
        return {'id': user_id, 'name': 'John Doe from DB'}

# High-level module
class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_data(self, user_id):
        return self.user_repository.get_user(user_id)

@app.route('/user/<int:user_id>')
def get_user(user_id):
    service = UserService(DatabaseUserRepository())
    user = service.get_user_data(user_id)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
