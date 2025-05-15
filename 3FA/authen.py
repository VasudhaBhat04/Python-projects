import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

otp = None
image_auth_passed = False

def level1_authentication():
    correct_password = "Your_password"
    attempts = 3

    for attempt in range(attempts):
        password = input(f"Attempt {attempt + 1}/{attempts} - Enter your password: ") #upto 3 attempts

        if password == correct_password:
            messagebox.showinfo("Authentication", "Level 1 Passed! Proceeding to Image Authentication.")
            return True
        else:
            messagebox.showerror("Authentication", "Incorrect Password! Try again.")

    print("Authentication Failed! Too many incorrect attempts.")
    return False



def level2_authentication(selected_image, correct_image="img2.jpeg"):  #choose a image of your choice & remember for authentication
    global image_auth_passed

    if selected_image == correct_image:
        image_auth_passed = True
        messagebox.showinfo("Authentication", "Level 2 Passed! Proceeding to OTP.")
        root.quit() 
    else:
        messagebox.showerror("Authentication", "Incorrect Image! Try again.")


def send_otp_email(receiver_email):
    global otp
    otp = ''.join(random.choices(string.digits, k=6))  
    sender_email = "your_gmail@gmail.com"  #Sender gmail 
    password = "An app password"
    subject = "Your OTP for Authentication"
    body = f"Your OTP is: {otp}"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    for _ in range(3):
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"OTP sent to {receiver_email}. Please check your email!")
            return True  
        except Exception as e:
            print(f"Error sending OTP: {e}")
    
            print("Retrying OTP sending...")


    print("Failed to send OTP after 3 attempts.")
    otp = None
    return False  



def level3_authentication():
  
    user_otp = input(f"Enter the OTP sent to your email: ")

    if user_otp == otp:
        messagebox.showinfo("Authentication", "Level 3 Passed! Authentication Complete.")
        return True
    else:
        messagebox.showerror("Authentication", "Incorrect OTP! Try again.")
        print("Authentication Failed! Incorrect OTP.")
        return False



def load_image(image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((150, 150))
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        print(f"Error: {image_path} not found!")
        return None


def level2_gui():
    global root
    root = tk.Tk()
    root.title("Image-Based Authentication")

    label = tk.Label(root, text="Select the correct image:")
    label.pack()

    img_imag1 = load_image("images/img1.jpeg") #path to images can add upto many images
    img_imag2 = load_image("images/img2.jpeg")
    img_imag3 = load_image("images/img3.jpeg")
    img_imag4 = load_image("images/img4.jpeg")

    if not all([img_imag1, img_imag2, img_imag3, img_imag4]):
        messagebox.showerror("Error", "One or more images are missing. Please check the directory.")
        return

    tk.Button(root, image=img_imag1, command=lambda: level2_authentication("img1.jpeg")).pack(side=tk.LEFT)
    tk.Button(root, image=img_imag2, command=lambda: level2_authentication("img2.jpeg")).pack(side=tk.LEFT)
    tk.Button(root, image=img_imag3, command=lambda: level2_authentication("img3.jpeg")).pack(side=tk.LEFT)
    tk.Button(root, image=img_imag4, command=lambda: level2_authentication("img4.jpeg")).pack(side=tk.LEFT)

    root.mainloop()



def full_authentication():
 
    if not level1_authentication():
        return


    level2_gui()
    if not image_auth_passed:
        print("Image authentication failed!")
        return


    receiver_email = input("Enter your email: ") #Enter reciever email
    if not send_otp_email(receiver_email):
        print("Failed to send OTP. Check email setup.")
        return

    if level3_authentication():
        print("Authentication Successful!")
    else:
        print("Authentication Failed! Exiting program.")


if __name__ == "__main__":
    full_authentication()
