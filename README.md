# ssh-paramiko-toolkit
This Python script enables SSH interaction with remote servers using Paramiko. Features include brute-force login, interactive shell, SSH key generation, and adding keys to servers. Efficient for server management and automation.

**Description:**

This Python script provides functionalities to interact with remote servers via SSH using the Paramiko library. It includes features such as brute-force SSH login, interactive shell session, SSH key pair generation, and adding SSH keys to servers. The `brute_force_ssh` function allows attempting to log in to a server by trying various combinations of usernames and passwords. The `interact_with_remote_shell` function facilitates an interactive shell session with the remote server. Additionally, the script provides options for generating SSH key pairs and adding them to servers for more secure authentication.

## Features

- **Brute-force SSH Login:** Attempt to log in to a server by trying various combinations of usernames and passwords.
- **Interactive Shell Session:** Establish an interactive shell session with the remote server to execute commands.
- **SSH Key Pair Generation:** Generate RSA key pairs for secure authentication.
- **Adding SSH Keys to Servers:** Add generated SSH public keys to server's `authorized_keys` file for secure authentication.

## Usage

1. Clone the repository:

```
git clone https://github.com/your_username/ssh-paramiko-toolkit.git
```

2. Navigate to the project directory:

```
cd ssh-paramiko-toolkit
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the script:

```
python ssh_toolkit.py
```

Follow the on-screen instructions to choose the desired functionality and provide the required information.

## Requirements

- Python 3.x
- Paramiko library

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```


