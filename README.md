
# Password Manager

A secure application built in **Python** that allows users to safely store, retrieve, and manage their passwords for different services. The application uses encryption techniques to protect sensitive information and requires a master password for access.

## Table of Contents

1. [Features](#features)  
2. [Project Structure](#project-structure)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [How It Works](#how-it-works)  
6. [Security Considerations](#security-considerations)  
7. [Dependencies](#dependencies)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Credits](#credits)


## Features

- Store credentials (username + password) for multiple services  
- Encrypt stored data so it is safe even if database file is leaked  
- Master password authentication  
- Add / retrieve / delete saved entries  
- Easy-to-use command-line interface  


## Project Structure


Password-Manager-project/
│
├── generate\_key.py         # Script to generate encryption key
├── password\_manager.py     # Main program logic
├── key.key                  # Encryption key file (must be kept secret)
├── passwords.db             # Encrypted database of saved passwords
├── Explanation Note.txt     # Notes / explanations
├── Password\_Manager\_Explanation.pdf  # Detailed explanation / design (PDF)
└── README.md                # (You are here)


**Note:** The files `key.key` and `passwords.db` should **not** be shared publicly. You may want to add them to `.gitignore`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rakeshln222/Password-Manager-project.git
   cd Password-Manager-project
````

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate     # On Unix/Mac
   # or
   venv\Scripts\activate        # On Windows
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   > If there is no `requirements.txt`, the main external library you’ll need is likely `cryptography` (or whichever encryption library is used).

4. Generate encryption key (if not already present):

   ```bash
   python generate_key.py
   ```

   This will create a file `key.key` containing the encryption key.


## Usage

1. Run the password manager:

   ```bash
   python password_manager.py
   ```

2. On first run, you will be prompted to set a **master password** (or enter the existing one). This master password is used to derive or unlock the key to encrypt/decrypt stored credentials.

3. After authentication, you can choose from options such as:

   * Add new credentials
   * Retrieve existing credentials
   * Delete credentials
   * Exit

4. The stored credentials are saved (encrypted) in the `passwords.db` file.

## How It Works

* The `generate_key.py` script generates a random symmetric key and saves it to `key.key`.
* `password_manager.py` reads this key (after verifying with user’s master password) to encrypt/decrypt the stored data.
* Credentials are stored in a database (SQLite, or similar) in encrypted form.
* When the user wants to retrieve a credential, the application decrypts the relevant entry.
* Sensitive files like `key.key` and the encrypted DB should be kept secure (never commit them to public repos).


## Security Considerations & Best Practices

* **Never share** the `key.key` file or `passwords.db` publicly.
* Use a **strong, unique master password**.
* Consider adding `key.key` and `passwords.db` to `.gitignore` so they aren’t accidentally committed.
* For improved security, consider using OS-level secure storage or hardware modules (e.g. TPM) instead of file-based key storage.
* Keep your dependencies and Python version up-to-date to avoid vulnerabilities.


## Dependencies

* Python 3.x
* cryptography (or whichever library used for encryption)
* sqlite3 (if using SQLite)
* Any other libraries used (list them, e.g., `tabulate`, `getpass`, etc.)


## Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add feature …"`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please make sure your code follows consistent style and includes tests (if applicable).

## Credits

* Developed by **Rakeshln222**
* Inspiration, ideas, or external resources (cite as needed)
* Any third-party libraries used
