import time
import getpass
import paramiko

ssh = paramiko.SSHClient()
print(type(ssh))
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname':'192.168.75.136', 'port': '22', 'username':'pabs', 'password':'pass123'}
print(f'CONNECTING TO....{linux["hostname"]}')
ssh.connect(**linux, look_for_keys=False, allow_agent=False)
shell = ssh.invoke_shell()
shell.send('cat /etc/passwd\n')
time.sleep(1)
shell.send('sudo cat /etc/shadow\n')
time.sleep(1)
shell.send('pass123\n')
time.sleep(1)
output = shell.recv(10000).decode()
print(output)
ssh.close()