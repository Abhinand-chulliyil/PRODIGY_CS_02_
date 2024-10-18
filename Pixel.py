from PIL import Image
import os

# Encryption key
KEY = 123  # You can change this value to any integer

# Encrypt Image
def encrypt_image(input_image_path, output_image_path):
    print(f"Encrypting the file: {input_image_path}")
    
    if not os.path.exists(input_image_path):
        print(f"Error: The file '{input_image_path}' does not exist.")
        return

    image = Image.open(input_image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Enhanced encryption using addition and XOR with a key
            r = (r + 50) % 256
            g = (g + 50) % 256
            b = (b + 50) % 256

            r = (r ^ KEY) % 256
            g = (g ^ KEY) % 256
            b = (b ^ KEY) % 256

            pixels[i, j] = (r, g, b)

    image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

# Decrypt Image
def decrypt_image(encrypted_image_path, output_image_path):
    print(f"Decrypting the file: {encrypted_image_path}")
    
    if not os.path.exists(encrypted_image_path):
        print(f"Error: The file '{encrypted_image_path}' does not exist.")
        return

    image = Image.open(encrypted_image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]

            # Reverse the encryption
            r = (r ^ KEY) % 256
            g = (g ^ KEY) % 256
            b = (b ^ KEY) % 256

            r = (r - 50) % 256
            g = (g - 50) % 256
            b = (b - 50) % 256

            pixels[i, j] = (r, g, b)

    image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

if __name__ == "__main__":
    input_image = r"C:\Users\acer\Downloads\pic.jpg"
    encrypted_image = "encrypted_pic.png"
    decrypted_image = "decrypted_pic.png"

    # Encrypt the image
    encrypt_image(input_image, encrypted_image)

    # Decrypt the image (to check if we get the original back)
    decrypt_image(encrypted_image, decrypted_image)
