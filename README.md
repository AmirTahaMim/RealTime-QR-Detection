
# RealTime-QR-Detection

This is a Python script that uses OpenCV and pyzbar to detect and decode QR codes from a webcam feed.

## Requirements

Before running the script, make sure you have the following libraries installed:

- OpenCV (`opencv-python`)
- pyzbar (`pyzbar`)

You can install the required libraries using `pip`:


```pip install opencv-python pyzbar```


## How to Use

1. Clone this repository or download the script `RealTimeQR_Detector.py` to your local machine.

2. Make sure you have a webcam connected to your computer.

3. Open a terminal or command prompt and navigate to the directory containing the script.

4. Run the script using the following command:


```python RealTimeQR_Detector.py```


5. The script will start the webcam feed, and it will continuously search for QR codes in the video frames.

6. When a QR code is detected, it will draw a rectangle around it and print the decoded data in the console.

7. To quit the program, press the 'q' key.

## Acknowledgements

- The script uses the `pyzbar` library to decode QR codes: [https://pypi.org/project/pyzbar/](https://pypi.org/project/pyzbar/)
- The webcam access is achieved using the `opencv-python` library: [https://pypi.org/project/opencv-python/](https://pypi.org/project/opencv-python/)

## License

This project is licensed under the MIT License. Feel free to use and modify it according to your needs.

