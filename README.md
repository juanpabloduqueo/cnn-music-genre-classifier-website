# Top-n Music Genre Classification Neural Network

This project is a deep learning-based application that classifies music tracks into their respective genres using a Convolutional Neural Network (CNN). The app features a web-based user interface and is periodically deployed on an AWS EC2 instance.

## Overview

The goal of this project is to accurately predict the top-n music genres for a given audio file. The model was trained on the GTZAN dataset, a widely used benchmark in the music genre classification domain.

## Features

- **Dataset**: The model is trained on the [GTZAN dataset], which contains 10 different genres, with 100 tracks per genre.
- **Audio Processing**: Audio data was processed using [Librosa](https://librosa.org/), a Python library for music and audio analysis. The primary features extracted were Mel Frequency Cepstral Coefficients (MFCCs) with a sample rate of 22,050 Hz.
- **Model Architecture**: The neural network used for classification is a Convolutional Neural Network (CNN), designed to handle the high dimensionality and complexity of audio features.
- **Web UI**: A user-friendly web interface was built using [Flask](https://flask.palletsprojects.com/), allowing users to upload audio files and receive genre predictions.
- **Deployment**: The application is deployed sporadically on an AWS EC2 instance. The server is switched on and off to avoid unnecessary charges, so the app may not always be online.

## Usage

1. Clone the repository:    
   git clone https://github.com/yourusername/yourrepository.git

2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the Flask app locally:
   flask run

4. Access the app through your web browser at http://127.0.0.1:5000.

## Future Work

- **Model Optimization**: Explore advanced architectures and hyperparameter tuning to improve classification accuracy.
- **Dataset Expansion**: Incorporate additional datasets to support a wider range of music genres.
- **Continuous Deployment**: Implement a CI/CD pipeline for more consistent and reliable deployment.

## Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, and open pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the creators of the GTZAN dataset and the developers of Librosa and Flask.
- Inspired by the research and applications of music genre classification in machine learning.
- Special thanks to the YouTube channel [Valerio Velardo - The Sound of AI](https://www.youtube.com/@ValerioVelardoTheSoundofAI) for the incredibly helpful tutorials on music AI, which greatly assisted in the development of this project.
