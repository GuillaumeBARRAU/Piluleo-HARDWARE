from flask import Flask, jsonify
from Electro_Magnet import Electromagnet

app = Flask(__name__)

electromagnet = Electromagnet(pin=PIN_NUMBER)

@app.route('/pillbox/open', methods=['POST'])
def open_pillbox():
    electromagnet.deactivate()

    return jsonify({'message': 'Pillbox opened successfully'}), 200

@app.route('/pillbox/close', methods=['POST'])
def close_pillbox():
    electromagnet.activate()
    
    return jsonify({'message': 'Pillbox closed successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)