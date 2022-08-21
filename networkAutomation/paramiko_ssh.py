import time
import getpass
import paramiko

ssh = paramiko.SSHClient()
print(type(ssh))

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#method 1 in connecting to a device
#ssh.connect(hostname='192.168.75.132', port='22', username='cisco', password='eve',
#            look_for_keys=False, allow_agent=False)

#method 2 in connecting to a device

password = getpass.getpass('Enter password:')
router = {'hostname':'192.168.75.132', 'port': '22', 'username':'cisco', 'password':password}
print(f'CONNECTING TO....{router["hostname"]}')
ssh.connect(**router, look_for_keys=False, allow_agent=False)

shell = ssh.invoke_shell() # create a shell terminal for the connection
shell.send('terminal length 0\n')
shell.send('show version\n') # send a command through shell terminal
shell.send('show int brief\n')

#with open('ssh_log.txt', 'w') as file:
#    f = file.write(str(writeme))
#    file.close()

time.sleep(1) # delay in seconds
output = shell.recv(10000) # display output in bytes format
output = output.decode('utf-8') # decode from bytes to string
print(output)

print(ssh.get_transport().is_active())

#sending command
if ssh.get_transport().is_active() == True:
    print('Clossing connection...')
    ssh.close()
