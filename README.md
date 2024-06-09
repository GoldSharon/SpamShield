# SpamShield: Spam Detection Flask Application

## Overview
SpamShield is a web-based application designed to detect spam messages using a machine learning model. It leverages Flask for the web framework and a Naive Bayes classifier for the spam detection model. The application provides an easy-to-use interface where users can input their messages and receive instant feedback on whether the message is spam or not.

## Features
- **User-Friendly Interface**: Clean and intuitive design for easy interaction.
- **Real-Time Spam Detection**: Immediate results upon message submission.
- **Advanced AI Technology**: Utilizes a Naive Bayes classifier for accurate spam detection.
- **Privacy Assurance**: No data is stored or shared; user inputs are processed in real-time and discarded.

## Project Structure

SpamShield/<br>
│<br>
├── app.py # Main application file <br>
├── templates/<br>
│ ├── index.html # Home page template<br>
│ └── predict.html # Result page template<br>
├── models/<br>
│ ├── Spam_Model.joblib # Pre-trained model<br>
│ └── Vectorizer.joblib # Vectorizer for text transformation<br>
├── README.md # Project README file<br>
└── requirements.txt # Python dependencies<br>


## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/GoldSharon/SpamShield.git
    cd SpamShield
    ```

2. **Set up a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Download the pre-trained model and vectorizer**:
    - Place `Spam_Model.joblib` and `Vectorizer.joblib` in the `models/` directory.

## Usage
1. **Run the application**:
    ```sh
    python app.py
    ```

2. **Access the web interface**:
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Check for spam**:
    - Enter the message you want to check in the provided text box.
    - Click the "Check" button to get the result.

## Dependencies
- Flask
- scikit-learn
- joblib
- numpy

Install dependencies using:
```sh
pip install -r requirements.txt
```
## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or suggestions.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
The Naive Bayes model and TF-IDF vectorizer were trained using the scikit-learn library.
Flask framework for the web application.
