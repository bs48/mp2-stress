from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        subprocess.Popen(['python', 'stress_cpu.py'])
        return jsonify({'message': 'CPU stress initiated'})

    elif request.method == 'GET':
        private_ip = socket.gethostname()
        return str(private_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

