from flask import Flask, jsonify
app=Flask(__name__)
@app.route('/details', methods=['GET'])
def details():
    return jsonify({
        "message": "My Flask Application hey"
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "OK"
    }),200

if __name__ == '__main__':
    app.run(host="0.0.0.0")