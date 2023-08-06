import cv2
import numpy as np
from pyzbar.pyzbar import decode

class QRCodeDetector:
    def detect_qr_codes(self, frame):
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find QR codes in the frame
        qr_codes = decode(gray_frame)

        return qr_codes

    def extract_qr_data(self, qr_codes):
        if qr_codes:
            for qr_code in qr_codes:
                # Extract the data from the QR code
                qr_data = qr_code.data.decode('utf-8')
                print("QR Code Data:", qr_data)

    def draw_qr_code_rectangles(self, frame, qr_codes):
        if qr_codes:
            for qr_code in qr_codes:
                # Draw a rectangle around the QR code on the frame
                points = qr_code.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    cv2.polylines(frame, [hull], True, (255, 0, 255), 3)
                else:
                    cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (255, 0, 255), 3)

    def run(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            qr_codes = self.detect_qr_codes(frame)
            self.extract_qr_data(qr_codes)
            self.draw_qr_code_rectangles(frame, qr_codes)

            # Display the frame with detected QR codes
            cv2.imshow("Detect QR Code from Webcam", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    qr_detector = QRCodeDetector()
    qr_detector.run()
