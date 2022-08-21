import time
import paramiko
import getpass


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname': '192.168.75.136', 'port':'22', 'username': 'pabs', 'password': 'pass123'}
ssh.connect(**linux, look_for_keys=False, allow_agent=False)
shell = ssh.invoke_shell()
shell.send('who\n')
time.sleep(1)
output = shell.recv(10000).decode()
print(output)
shell.close()