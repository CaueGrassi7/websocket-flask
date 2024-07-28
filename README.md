# WebSocket Flask

This project demonstrates how to use WebSockets with Flask for real-time communication.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)

## Introduction

This Flask application showcases the implementation of WebSocket for real-time updates. It includes basic examples of creating and handling WebSocket connections.

## Installation

### Requirements

- Python 3.7+
- Flask
- Flask-SocketIO

### Installation Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/CaueGrassi7/websocket-flask.git
    ```
2. Navigate to the project directory:
    ```sh
    cd websocket-flask
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
6. Run the application:
    ```sh
    python app.py
    ```

## Usage

The application will run at `http://127.0.0.1:5000/`.

### Endpoints

#### Create Pix Payment
- **URL:** `/payments/pix`
- **Method:** `POST`
- **Description:** Creates a new Pix payment.
- **Request Data:**
    ```json
    {
        "value": "amount"
    }
    ```
- **Success Response:**
    ```json
    {
        "message": "Pix payment created!",
        "payment": {
            "id": 1,
            "value": "amount",
            "paid": false,
            "bank_payment_id": null,
            "qr_code": null,
            "expiration_date": "datetime"
        }
    }
    ```

#### Confirm Pix Payment
- **URL:** `/payments/pix/confirmation`
- **Method:** `POST`
- **Description:** Confirms a Pix payment.
- **Request Data:**
    ```json
    {
        "payment_id": 1
    }
    ```
- **Success Response:**
    ```json
    {
        "message": "Pix payment confirmed!",
        "payment": {
            "id": 1,
            "value": "amount",
            "paid": true,
            "bank_payment_id": null,
            "qr_code": null,
            "expiration_date": "datetime"
        }
    }
    ```

#### Get Pix Payment
- **URL:** `/payments/pix/<int:payment_id>`
- **Method:** `GET`
- **Description:** Retrieves details of a Pix payment.
- **Success Response:**
    ```json
    {
        "payment": {
            "id": 1,
            "value": "amount",
            "paid": false,
            "bank_payment_id": null,
            "qr_code": null,
            "expiration_date": "datetime"
        }
    }
    ```

## Contributing

Contributions are welcome! Follow the steps below to contribute:

1. Fork the project.
2. Create a branch for your feature or bugfix (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.
