## Secure Password Storage App

A simple Python-based application that demonstrates the use of **AES encryption** to securely store and retrieve passwords. This project aims to provide a foundational understanding of how to safely handle sensitive user data, like passwords, using encryption techniques.

### Features
- **Password Encryption**: Encrypts passwords using AES (Advanced Encryption Standard) with a 256-bit key.
- **Password Decryption**: Decrypts the encrypted passwords back to their original form using the same key.
- **Random Initialization Vector (IV)**: Each password is encrypted with a unique initialization vector (IV) to ensure the encryption is secure and different each time.
- **Base64 Encoding**: Encrypted passwords and IV are encoded in **base64** format for safe storage or transmission.

### Technologies Used
- **Python**: The main programming language used for the app.
- **cryptography library**: This library provides the necessary tools for encryption and decryption using AES.
  - **AES (Advanced Encryption Standard)**: Used for encrypting and decrypting passwords.
  - **PKCS7 Padding**: Used to ensure the password data is a multiple of the block size required by AES.
- **Base64 Encoding**: Used for converting binary data to a readable format.

### Setup and Usage

#### Requirements
- **Python** (version 3.7 or higher recommended)
- **cryptography library** for Python

#### Installation

1. **Clone the Repository**
   - Clone the project to your local machine:
     ```bash
     git clone https://github.com/mahtabintushi/secure-password-storage.git
     ```

2. **Set Up a Python Environment**
   - It's recommended to create a **virtual environment** to manage dependencies for the project. To do this, run the following commands:
     ```bash
     # On Windows
     python -m venv venv
     .\venv\Scripts\activate

     # On MacOS/Linux
     python3 -m venv venv
     source venv/bin/activate
     ```

   - If you prefer to skip the virtual environment, ensure Python is installed on your machine.

3. **Install Dependencies**
   - Install the required dependencies by running:
     ```bash
     pip install cryptography
     ```

4. **Run the Script**
   - Run the main Python script, which is usually named something like `password_encryption.py`:
     ```bash
     python password_encryption.py
     ```

### Example Output
```bash
Encrypted password: <encrypted_password>
Decrypted password: my_secret_password
