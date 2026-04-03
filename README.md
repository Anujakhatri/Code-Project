# Code-Project

Welcome to **Code-Project**! This repository is a diverse collection of short Python scripts, mini-games, AI integrations, and deep learning practice notebooks. It serves as a playground for experimenting with new concepts and building fun, small-scale applications.

## 📂 Project Structure and Features

### 1. AI & Chatbots
* **`main.py`** (Gemini Pro Chatbot UI): A fully functional web-based chatbot built with Streamlit and powered by Google's Generative AI (`gemini-pro`). It features a user-friendly chat interface and maintains conversational memory.
* **`chatbot.py`**: A simple, rule-based command-line interface (CLI) chatbot for practicing basic text processing and user input logic.

### 2. Mini-Games & Generators
* **`#1.Tic_Tac_Toe.py`**: A classic command-line Tic-Tac-Toe game for two players.
* **`madlibs_generator.py`** & **`story.txt`**: A fun Madlibs CLI game. It reads a story template from `story.txt`, identifies the placeholders (enclosed in brackets), and prompts the user to fill in the words before generating the final funny story.
* **`QrCodeGen.py`**: A handy utility script that uses the `qrcode` library to generate a customized, styled QR code image (with a default setup to link to a LinkedIn profile).

### 3. Deep Learning Exercises
* **`Deep-Learning/`**: A dedicated directory containing Jupyter Notebooks for practicing machine learning and deep learning concepts. Includes files like `DL practice.ipynb` and `TensorCoreConcepts.ipynb` for hands-on TensorFlow learning.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed on your system. To install the required dependencies for all the projects, run:

```bash
pip install -r requirements.txt
```

*(Note: Depending on the specific script you want to run, verify you have the corresponding libraries, such as `qrcode` and `pillow` for `QrCodeGen.py`.)*

### Running the Streamlit AI Chatbot (`main.py`)
To run the Gemini Chatbot, you will need a valid Google API Key:
1. Create a `.env` file in the root directory.
2. Add your Google API key to the `.env` file as follows:
   ```env
   Your Api Key=YOUR_ACTUAL_API_KEY
   ```
3. Boot up the Streamlit application:
   ```bash
   streamlit run main.py
   ```

### Running CLI Scripts
You can easily run any of the command-line scripts directly using Python:
```bash
python chatbot.py
python madlibs_generator.py
python "#1.Tic_Tac_Toe.py"
python QrCodeGen.py
```
