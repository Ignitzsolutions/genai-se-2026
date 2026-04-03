
@app.route('/login', methods=['POST'])

def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Missing credentials'}), 400
    # TODO: verify credentials against your user store
    if username == 'admin' and password == 'secret':
        token = create_jwt({'user': username})
        return jsonify({'token': token})
    return jsonify({'error': 'Invalid credentials'}), 401