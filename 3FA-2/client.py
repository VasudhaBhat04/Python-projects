import cv2
import sqlite3
import qrcode
import hashlib
import os
import numpy as np
import socket
import threading


# Database setup
def init_db():
    conn = sqlite3.connect('auth.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT,
                        qr_code TEXT,
                        face_image_path TEXT)''')
    conn.commit()
    conn.close()
import socket

def connect_to_server():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = 'server IP address'  # Same as the server's IP
        server_port = 5000
        client_socket.connect((server_ip, server_port))  # Connect to the server
        print("Connected to the server!")
        message = client_socket.recv(1024).decode()
        print(f"Server: {message}")
        client_socket.close()
    except Exception as e:
        print(f"Failed to connect to the server: {e}")

        
# Helper functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)


def capture_face_data(username):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    print("Look at the camera to capture your face data. Press 'q' to finish.")

    face_data = []
    count = 0
    os.makedirs(f"faces/{username}", exist_ok=True)

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to access the camera.")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            face_resized = cv2.resize(face, (100, 100))
            face_data.append(face_resized)
            count += 1

            # Save the first captured face as an image
            if count == 1:
                face_filename = f"faces/{username}/face.jpg"
                cv2.imwrite(face_filename, face)

            # Draw rectangle around the face in the frame
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 20:  # Capture 20 samples
            break

    cam.release()
    cv2.destroyAllWindows()

    print(f"Captured {count} faces. The image is saved in 'faces/{username}' directory.")
    return f"faces/{username}/face.jpg"  # Return path to the first image


def train_face_recognizer(username):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Create a face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    face_images = []
    labels = []

    # Load the face images stored for the user
    face_folder = f"faces/{username}"

    for face_image in os.listdir(face_folder):
        if face_image.endswith('.jpg'):
            # Read the stored face image
            img = cv2.imread(f"{face_folder}/{face_image}")
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                face = gray[y:y+h, x:x+w]
                face_images.append(face)
                labels.append(0)  # Using 0 as a placeholder label for the user

    # Train the recognizer with the collected faces
    recognizer.train(face_images, np.array(labels))
    recognizer.save(f"faces/{username}/face_recognizer.yml")
    print(f"Face recognizer trained and saved for {username}.")


import time

def recognize_face(username):
    # Load the trained recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(f"faces/{username}/face_recognizer.yml")

    # Initialize face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)

    print("Look at the camera for face recognition.")

    # Set parameters for timeout and max failed attempts
    timeout_duration = 20  # seconds before timing out
    max_failed_attempts = 5
    last_face_time = time.time()  # Track when the last valid face was seen
    failed_attempts = 0  # Track number of wrong face attempts

    no_face_flag = False  # Flag to track if no face has been detected

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to access the camera.")
            return False

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # If no faces are detected
        if len(faces) == 0:
            if not no_face_flag:
                print("No face detected. Please try again.")
                no_face_flag = True  # Set the flag to avoid multiple prints
            elapsed_time = time.time() - last_face_time  # Calculate how long since the last face was seen

            if elapsed_time > timeout_duration:  # If timeout duration has passed
                print("Authentication failed. No face detected for a while.")
                cam.release()
                cv2.destroyAllWindows()
                return False

        else:
            no_face_flag = False  # Reset flag when face is detected
            last_face_time = time.time()  # Update the time when a valid face is detected

            # Process each detected face
            for (x, y, w, h) in faces:
                face = gray[y:y+h, x:x+w]
                label, confidence = recognizer.predict(face)

                # If the confidence is below the threshold, it's a match
                if confidence < 80:  # Threshold value can be adjusted
                    print("Face recognized successfully!")
                    cam.release()
                    cv2.destroyAllWindows()
                    return True
                else:
                    failed_attempts += 1
                    if failed_attempts >= max_failed_attempts:  # If max failed attempts reached
                        print("Authentication failed. Wrong face detected multiple times.")
                        cam.release()
                        cv2.destroyAllWindows()
                        return False

                    print(f"Face recognition failed. Attempt {failed_attempts}/{max_failed_attempts}.")

                    # Draw rectangle around the face and indicate mismatch
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)  # Red rectangle for failed recognition
                    cv2.putText(frame, "Recognition Failed", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        # Display the frame with rectangles and text
        cv2.imshow('Face Recognition', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Face recognition failed.")
            cam.release()
            cv2.destroyAllWindows()
            return False
# Registration
def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)

    # Generate and save QR code
    qr_code_path = f"{username}_qr.png"
    generate_qr_code(username, qr_code_path)
    print(f"QR code saved as {qr_code_path}")

    # Capture and save face data
    face_image_path = capture_face_data(username)

    # Train the face recognizer
    train_face_recognizer(username)

    # Store in database
    conn = sqlite3.connect('auth.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, qr_code, face_image_path) VALUES (?, ?, ?, ?)",
                   (username, hashed_password, qr_code_path, face_image_path))
    conn.commit()
    conn.close()
    print("User registered successfully!")


def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)

    conn = sqlite3.connect('auth.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password, qr_code, face_image_path FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        print("User not found.")
        return False

    db_password, qr_code_path, face_image_path = result

    # Check password
    if db_password != hashed_password:
        print("Incorrect password.")
        return False

    # QR Code Verification
    print(f"Scan your QR code saved at {qr_code_path}")
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to access the camera.")
            return False

        data, bbox, _ = detector.detectAndDecode(frame)
        if data == username:
            print("QR code verified successfully!")
            break

        cv2.imshow("Scan QR Code", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("QR code verification failed.")
            return False

    cap.release()
    cv2.destroyAllWindows()

    # Face Recognition using LBPH
    if recognize_face(username):
        return True
    else:
        return False

# Main
if __name__ == "__main__":
    init_db()
    while True:
        choice = input("Choose an option: [1] Register [2] Login [3] Exit: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user():
                print("Authentication successful!")
                print("connecting to the server....")
                connect_to_server()
            else:
                print("Authentication failed.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
