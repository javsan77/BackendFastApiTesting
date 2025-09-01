# ChatBot API

This project is a RESTful API built with **FastAPI** that serves as the backend for a chatbot. Currently, the API receives a message and returns a test response. The architecture is designed to progressively allow for the integration of Large Language Models (LLMs).

-----

## 🚀 Features

  * **Asynchronous Backend**: Built with FastAPI, ensuring fast, asynchronous performance.
  * **CORS Handling**: Configured to accept requests from any origin (`*`), making it easy to integrate with different frontends.
  * **Chat Endpoint**: A `/chat` endpoint that accepts messages in JSON format.
  * **Scalable Structure**: The codebase is ready for the incorporation of an LLM to generate dynamic and advanced responses.

-----

## 🛠️ Requirements

Make sure you have **Python 3.8+** installed.

-----

## ⚙️ Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  Install the necessary dependencies:
    ```bash
    pip install fastapi uvicorn pydantic python-multipart
    ```

-----

## ▶️ Usage

To start the API in development mode, run the following command from the project's root directory:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

  * `main:app`: Tells Uvicorn to look for the `app` instance inside the `main.py` file.
  * `--reload`: Automatically restarts the server when it detects code changes.
  * `--host 0.0.0.0`: Makes the API accessible from other machines on your network.
  * `--port 8000`: Sets the API's port to 8000.

-----

## 🧪 API Endpoints

### `GET /`

  * **Description**: A simple endpoint to check if the API is running.
  * **Example Response**:
    ```json
    {
      "message": "API is working correctly"
    }
    ```

### `POST /chat`

  * **Description**: Sends a chat message to the API.
  * **Request Body**:
    ```json
    {
      "message": "Hello, how are you?"
    }
    ```
  * **Example Response**:
    ```json
    {
      "response": "Received your message: Hello, how are you?"
    }
    ```

-----

## 🛣️ Next Steps

The next phase of development includes **integrating an LLM** to replace the static response logic and turn the API into a true conversational chatbot. Options such as the OpenAI API, Hugging Face, or local models will be explored.
