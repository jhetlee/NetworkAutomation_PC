import time
import getpass
import paramiko

ssh = paramiko.SSHClient()
print(type(ssh))

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router1 = {'hostname':'192.168.75.132', 'port': '22', 'username':'cisco', 'password':'eve'}
router2 = {'hostname':'192.168.75.133', 'port': '22', 'username':'cisco', 'password':'eve'}
router3 = {'hostname':'192.168.75.134', 'port': '22', 'username':'cisco', 'password':'eve'}

routers = [router1, router2, router3]
for router in routers:
    print(f'CONNECTING TO....{router["hostname"]}')
    ssh.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh.invoke_shell() # create a shell terminal for the connection
    shell.send('enable\n')
    shell.send('cisco\n') # send a command through shell terminal
    shell.send('copy run start\n')
    shell.send('\n')

    #with open('ssh_log.txt', 'w') as file:
    #    f = file.write(str(writeme))
    #    file.close()
    time.sleep(1) # delay in seconds
    output = shell.recv(10000).decode()
    print(output)

    print(ssh.get_transport().is_active())

#sending command

ssh.close()
