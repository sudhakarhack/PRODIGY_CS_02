import cv2
import numpy as np

def encrypt_image(image_path, key):
    """Encrypt an image using pixel manipulation while preserving original structure."""
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found.")
        return None

    # Convert to NumPy array for manipulation
    img_array = np.array(img, dtype=np.uint8)

    # Encrypt each pixel value and prevent overflow
    encrypted_img = (img_array.astype(np.int32) + key) % 256  # Ensure no value goes beyond 255
    encrypted_img = encrypted_img.astype(np.uint8)  # Convert back to uint8

    encrypted_path = "encrypted_image.png"
    cv2.imwrite(encrypted_path, encrypted_img)
    print(f"🔒 Encrypted image saved as: {encrypted_path}")

    return encrypted_path

def decrypt_image(encrypted_path, key):
    """Decrypt an image by reversing the encryption process."""
    encrypted_img = cv2.imread(encrypted_path)

    if encrypted_img is None:
        print("Error: Encrypted image not found.")
        return None

    # Convert to NumPy array for manipulation
    encrypted_array = np.array(encrypted_img, dtype=np.uint8)

    # Decrypt each pixel value and prevent underflow
    decrypted_img = (encrypted_array.astype(np.int32) - key) % 256  # Ensure values don't go below 0
    decrypted_img = decrypted_img.astype(np.uint8)  # Convert back to uint8

    decrypted_path = "decrypted_image.png"
    cv2.imwrite(decrypted_path, decrypted_img)
    print(f"🔓 Decrypted image saved as: {decrypted_path}")

    return decrypted_path

# ===== Example Usage =====
image_path = "images (4).jpg"  # Update this with your image filename
key = 42  # Change this key for different encryption results

encrypted_path = encrypt_image(image_path, key)
if encrypted_path:
    decrypt_image(encrypted_path, key)
