from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/payments/pix', methods=['POST'])
def create_pix_payment():
    return jsonify({'message': 'Pix payment created!'})

@app.route('/payments/pix/confirmation', methods=['POST'])
def confirm_pix_payment():
    return jsonify({'message': 'Pix payment confirmed!'})

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def get_pix_payment(payment_id):
    return jsonify({'payment_id': payment_id})

if __name__ == '__main__':
    app.run(debug=True)
