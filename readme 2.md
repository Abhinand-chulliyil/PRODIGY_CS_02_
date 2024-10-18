# IMAGE ENCRYPTION & DECRYPTION USING XOR

## Description
This project is a Python program that implements an image encryption and decryption mechanism using the XOR operation. The program allows users to encrypt an image by modifying its pixel values based on a specified key and then decrypt it to retrieve the original image.

## Features
- **Image Encryption**: Encrypts images by altering pixel values using a customizable key and a defined algorithm.
- **Image Decryption**: Restores the original image by reversing the encryption process.
- **User-Friendly Interface**: Offers clear console output for the encryption and decryption processes.

## How It Works
### Encryption Process
1. Each pixel's RGB values are modified:
   - An additive offset is applied (in this case, +50).
   - The modified values are then XORed with a predefined key.
2. The encrypted pixel values are saved to a new image file.

### Decryption Process
1. The process reverses the encryption:
   - The pixel values are XORed again with the same key.
   - The additive offset is subtracted (in this case, -50).
2. The original pixel values are restored and saved to a new image file.

## How to Run
1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/Abhinand-chulliyil/PRODIGY_CS_02_.git
2 Install Dependencies: Ensure you have the Pillow library installed:

bash
Copy code
pip install pillow
3 Run the Program: Modify the image paths in the script and execute it:

bash
Copy code
python your_script_name.py
Code Example
Here is the core part of the implementation:

python
Copy code
from PIL import Image
import os

# Encryption key
KEY = 123  # You can change this value to any integer

# Encrypt Image
def encrypt_image(input_image_path, output_image_path):
    ...
    
# Decrypt Image
def decrypt_image(encrypted_image_path, output_image_path):
    ...

if __name__ == "__main__":
    input_image = r"C:\Users\acer\Downloads\pic.jpg"
    encrypted_image = "encrypted_pic.png"
    decrypted_image = "decrypted_pic.png"

    # Encrypt the image
    encrypt_image(input_image, encrypted_image)

    # Decrypt the image (to check if we get the original back)
    decrypt_image(encrypted_image, decrypted_image)
Technologies Used
Python 3.x
Pillow (for image processing)
Author
Abhinand C
www.linkedin.com/in/abhinand-chulliyi

License
This project is licensed under the MIT License.







