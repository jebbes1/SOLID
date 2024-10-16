from flask import Flask, jsonify

app = Flask(__name__)

# Violating SRP by handling both logic and data fetching
@app.route('/user/<int:user_id>')
def get_user(user_id):
    # Handling multiple responsibilities
    user = {'id': user_id, 'name': 'John Doe'}
    return jsonify(user)

# Refactor: SRP Compliant
class UserService:
    @staticmethod
    def get_user_data(user_id):
        return {'id': user_id, 'name': 'John Doe'}

@app.route('/user/<int:user_id>')
def get_user(user_id):
    # Now only handling the route
    user = UserService.get_user_data(user_id)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
