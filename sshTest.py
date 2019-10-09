#! python3
import paramiko

# 存取帳密表
users = []
with open('login.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split(',')
        users.append(line)

# 呼叫路由器清單
hostnames = []
with open('hosts.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        hostnames.append(line)

#服务器信息，主机名（IP地址）、端口号、用户名及密码
port = 22
username = users[0][0]
password = users[0][1]

#创建SSH对象  
client = paramiko.SSHClient()

#自动添加策略，保存服务器的主机名和密钥信息
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
for hostname in hostnames:
    client.connect(hostname, port, username, password, compress=True)
    print('\n' + 'Routing Table from ' + hostname + ':')
    # 执行命令
    stdin, stdout, stderr = client.exec_command('show ip route summary')
    result = stdout.readlines()
    for line in result:
        print(line.strip('\n'))

'''
stdin, stdout, stderr = ssh.exec_command('ls')  # 執行命令
result = stdout.read()  # 獲取命令結果
print (str(result,encoding='utf-8'))
stdin, stdout, stderr = client.exec_command('show ip route summary')
result = stdout.readlines()
for line in result:
    print(line.strip('\n'))
stdin, stdout, stderr = client.exec_command('term len 0')
stdin, stdout, stderr = client.exec_command('show version')
result = stdout.readlines()
for line in result:
    print(line.strip('\n'))
'''