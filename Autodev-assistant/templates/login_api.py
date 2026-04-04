def get_code():
    return '''
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "1234":
        return {"message": "Login successful"}
    
    return {"message": "Invalid credentials"}, 401

if __name__ == "__main__":
    app.run(debug=True)
'''