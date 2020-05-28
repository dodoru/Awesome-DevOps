
## 1.3 服务器安全

### ssh 远程登录
 - Secure Shell Protocol
 - 非对称加密：传输数据前，将数据加密后再传送到网络上，数据传输过程中的安全性提高
 - 配置和使用
 
```bash
# 1. 在本机生成 ssh id_rsa.pub 
ssh-keygen
cat ~/.ssh/id_rsa.pub | pbcopy


# 2. 在服务器把本机生成的 public key 添加到~/.ssh/authorised_keys
#;  root用户把 public key 添加到 /root/.ssh/authorised_keys
cd /home/$USER
mkdir -p .ssh
chmod 700 .ssh 
cat id_rsa.pub >> .ssh/authorized_keys
chmod 600 .ssh/authorized_keys
chown $USER:$USER -R .ssh

# 3. 取消服务器的用户无密码登录，只允许ssh-key登录
cp /etc/ssh/sshd_conf  /root/bak/etc_sshd_conf.yymmdd
vi /etc/ssh/sshd_config
#    把
#    PasswordAuthentication yes
#    改为
#    PasswordAuthentication no
# 修改端口：PORT 32220
            
# 4. 重启服务器的 ssh
service ssh restart
``` 

 - [ssh端口转发：ssh隧道](http://www.zsythink.net/archives/2450/)
 
```bash
# -f: 后台
# -N: 不执行远程命令 
# -L: 使用本地端口转发创建ssh隧道
# -R: 表示使用远程端口转发创建ssh隧道
# A ssh -fPN -L LocalA:PortA:RemoteB:PortB -pPortM user@HostM
# 1. 转发测试环境的MySQL数据存储服务 
ssh -fPN -L localhost:9898:172.18.223.182:3306 -p32220 ningrong@120.79.232.217
# 2. 实时调试生产环境的短信服务 minieye-sms
ssh -fPN -L localhost:9899:localhost:7520 -p32220 nico@120.24.178.188
# 3. 实时调试生产环境的短信服务 minieye-sms
ssh -fPN -L localhost:16330:localhost:16332 -p32220 nico@120.24.178.188

# A ssh -fPN -R LocalA:PortA:RemoteB:PortB  -pPortM user@HostM
# 1. 把本地服务转给测试环境调试
```
 

### 禁止 scp / sftp
#### 禁止 scp
 - `yum remove openssh-clients -y` (不好）
 - `chmod 700 /usr/bin/scp`   (需要在/etc/ssh/sshd_config 禁止 root 登录)
 - [is-it-possible-to-prevent-scp-while-still-allowing-ssh-access](https://serverfault.com/questions/28858/is-it-possible-to-prevent-scp-while-still-allowing-ssh-access)
 - scp : 基于ssh登陆进行安全的远程文件拷贝命令 (secure copy)
 
```bash
# -1： 强制scp命令使用协议ssh1
# -2： 强制scp命令使用协议ssh2
# -4： 强制scp命令只使用IPv4寻址
# -6： 强制scp命令只使用IPv6寻址
# -B： 使用批处理模式（传输过程中不询问传输口令或短语）
# -C： 允许压缩。（将-C标志传递给ssh，从而打开压缩功能）
# -p：保留原文件的修改时间，访问时间和访问权限。
# -q： 不显示传输进度条。
# -r： 递归复制整个目录。
# -v：详细方式显示输出。scp和ssh(1)会显示出整个过程的调试信息。这些信息用于调试连接，验证和配置问题。
# -c cipher： 以cipher将数据传输进行加密，这个选项将直接传递给ssh。
# -F ssh_config： 指定一个替代的ssh配置文件，此参数直接传递给ssh。
# -i identity_file： 从指定文件中读取传输时使用的密钥文件，此参数直接传递给ssh。
# -l limit： 限定用户所能使用的带宽，以Kbit/s为单位。
# -o ssh_option： 如果习惯于使用ssh_config(5)中的参数传递方式，
# -P port：注意是大写的P, port是指定数据传输用到的端口号
# -S program： 指定加密传输时所使用的程序。此程序必须能够理解ssh(1)的选项。
scp -P 32220 nico@120.24.178.188:/home/nico/dst_file local_file
scp -P 32220 local_file nico@120.24.178.188:/home/nico/dst_file

# 建议少用 scp 文件到本地的行为
```

#### 禁止 sftp
```bash
vi /etc/ssh/sshd_config
# 注释: Subsystem      sftp    /usr/libexec/openssh/sftp-server
```

### ssh 认证详细过程

```
> ssh -p32220 -v4 nico@120.79.140.123

OpenSSH_7.9p1, LibreSSL 2.7.3
debug1: Reading configuration data /Users/nico/.ssh/config
debug1: /Users/nico/.ssh/config line 1: Applying options for *
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 48: Applying options for *
debug1: Connecting to 120.79.140.123 [120.79.140.123] port 32220.
debug1: fd 3 clearing O_NONBLOCK
debug1: Connection established.
debug1: identity file /Users/nico/.ssh/id_rsa type 0
debug1: identity file /Users/nico/.ssh/id_rsa-cert type -1
debug1: identity file /Users/nico/.ssh/id_dsa type -1
debug1: identity file /Users/nico/.ssh/id_dsa-cert type -1
debug1: identity file /Users/nico/.ssh/id_ecdsa type -1
debug1: identity file /Users/nico/.ssh/id_ecdsa-cert type -1
debug1: identity file /Users/nico/.ssh/id_ed255ssh -p32220 -v4 nico@120.79.140.123
OpenSSH_7.9p1, LibreSSL 2.7.3
debug1: Reading configuration data /Users/nico/.ssh/config
debug1: /Users/nico/.ssh/config line 1: Applying options for *
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 48: Applying options for *
debug1: Connecting to 120.79.140.123 [120.79.140.123] port 32220.
debug1: fd 3 clearing O_NONBLOCK
debug1: Connection established.
debug1: identity file /Users/nico/.ssh/id_rsa type 0
debug1: identity file /Users/nico/.ssh/id_rsa-cert type -1
debug1: identity file /Users/nico/.ssh/id_dsa type -1
debug1: identity file /Users/nico/.ssh/id_dsa-cert type -1
debug1: identity file /Users/nico/.ssh/id_ecdsa type -1
debug1: identity file /Users/nico/.ssh/id_ecdsa-cert type -1
debug1: identity file /Users/nico/.ssh/id_ed25519 type -1
debug1: identity file /Users/nico/.ssh/id_ed25519-cert type -1
debug1: identity file /Users/nico/.ssh/id_xmss type -1
debug1: identity file /Users/nico/.ssh/id_xmss-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_7.9
debug1: Remote protocol version 2.0, remote software version OpenSSH_7.4p1 Debian-10+deb9u6
debug1: match: OpenSSH_7.4p1 Debian-10+deb9u6 pat OpenSSH_7.0*,OpenSSH_7.1*,OpenSSH_7.2*,OpenSSH_7.3*,OpenSSH_7.4*,OpenSSH_7.5*,OpenSSH_7.6*,OpenSSH_7.7* compat 0x04000002
debug1: Authenticating to 120.79.140.123:32220 as 'nico'
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: ecdsa-sha2-nistp256
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ecdsa-sha2-nistp256 SHA256:LsOkQs6n8bBALwkYey93Spqw2Kke8h9wxSQFbS9FMus
debug1: checking without port identifier
debug1: Host '120.79.140.123' is known and matches the ECDSA host key.
debug1: Found key in /Users/nico/.ssh/known_hosts:20
debug1: found matching key w/out port
debug1: rekey after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey after 134217728 blocks
debug1: Will attempt key: /Users/nico/.ssh/id_rsa RSA SHA256:kuWDNmUxddmO25g0Dg+ycFYKzJAApQHyyKB8hore3Pc
debug1: Will attempt key: /Users/nico/.ssh/id_dsa
debug1: Will attempt key: /Users/nico/.ssh/id_ecdsa
debug1: Will attempt key: /Users/nico/.ssh/id_ed25519
debug1: Will attempt key: /Users/nico/.ssh/id_xmss
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,ssh-rsa,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521>
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey
debug1: Next authentication method: publickey
debug1: Offering public key: /Users/nico/.ssh/id_rsa RSA SHA256:kuWDNmUxddmO25g0Dg+ycFYKzJAApQHyyKB8hore3Pc
debug1: Server accepts key: /Users/nico/.ssh/id_rsa RSA SHA256:kuWDNmUxddmO25g0Dg+ycFYKzJAApQHyyKB8hore3Pc
debug1: Authentication succeeded (publickey).
Authenticated to 120.79.140.123 ([120.79.140.123]:32220).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: pledge: network
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: Sending environment.
debug1: Sending env LC_TERMINAL_VERSION = 3.3.6
debug1: Sending env LANG = en_US.UTF-8
debug1: Sending env LC_TERMINAL = iTerm2
debug1: Sending env LC_ALL = en_US.UTF-8
Linux alidev3 4.9.0-9-amd64 #1 SMP Debian 4.9.168-1+deb9u5 (2019-08-11) x86_64

Welcome to Alibaba Cloud Elastic Compute Service !

Last login: Fri May 29 14:34:58 2020 from 183.15.178.1819 type -1
```

### 如何允许 ssh 隧道长时间有效：
 - [Keep SSH session alive](https://stackoverflow.com/questions/25084288/keep-ssh-session-alive)
 - the client uses ServerAliveInterval while the server uses ClientAliveInterval
 - `vi client:$home/.ssh/config`
 
```text
Host remotehost
    HostName remotehost.com
    ServerAliveInterval 240
```

 - `ssh -o ServerAliveInterval=60 user@server.host`

### 如何通过代理访问 ssh

```bash
# 假设代理是
export http_proxy=http://127.0.0.1:1087;
export https_proxy=http://127.0.0.1:1087;
cp ~/.ssh/config ~/.ssh/config.bak.$yymmdd
#    Host *
#    ServerAliveInterval 120
#    ConnectTimeout 240
#
#    Host bitbucket
#        HostName bitbucket.org
#        User $name1
#        PreferredAuthentications publickey
#        IdentityFile ~/.ssh/id_rsa
#        ProxyCommand nc -X 5 -x 127.0.0.1 1087 %h %p
#
#    Host github.com
#        User $name2
#        ProxyCommand nc -X 5 -x 127.0.0.1:1080 %h %p            
#    # ProxyCommand proxychains4 127.0.0.1 1087 %h %p 
#    # ProxyCommand connect -H 127.0.0.1:1087 %h %p  (?)
```

