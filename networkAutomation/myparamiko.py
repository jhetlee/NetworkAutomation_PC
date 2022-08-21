import paramiko
import time
def connect(server_ip, server_port, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'connecting to{ server_ip }')
    ssh.connect(hostname=server_ip, port=server_port, username=user, password=password, look_for_keys=False, allow_agent=False)
    return ssh

def get_shell(ssh):
    shell = ssh.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    shell.send(command+'\n')
    time.sleep(timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh):
    if ssh.get_transport().is_active() == True:
        print('Clossing connection...')
        ssh.close()



client = connect('192.168.75.132', '22', 'cisco', 'eve')
shell = get_shell(client)
send_command(shell, 'enable')
send_command(shell, 'cisco')
send_command(shell, 'term len 0')
send_command(shell, 'sho version')
send_command(shell, 'show ip int brief')
output = show(shell)
print(output)
