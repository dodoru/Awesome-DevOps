
# Linux 文件权限、用户和组

## 文件权限 rwx

```
文件权限    文件类型 用户 用户组 文件大小  修改日期     文件名
-rw-rw-r--  1       dev dev     10     11/09 20:28  f.py 
drwxrwxr-x  2       dev dev     4096   11/09 20:28  tmp

文件类型    是否可读  是否可写  是否可执行
d           r       w           x
-           r       w           x

三组 rwx 分表代表 所属用户|同组用户|其他用户

rwx 可以用数字表示为 421
于是乎
r-- 就是 4
rw- 就是 6
rwx 就是 7
r-x 就是 5
```

- `chown` 改变文件的所属用户 （change owner)

    
    chown dev:dev -R /srv/services
    chown dev:dev /home/dev/.ssh/ssh_config
    chown dev authorized_keys
    
- chmod 修改文件的权限  （change mode)


    chmod 700 /home/dev/.ssh
    chmod +x /opt/scripts/ossutil
    chmod -x tmp

## 用户和组
- useradd/adduser, 推荐使用 `useradd -m dev` / `adduser >`
- userdel/deluser, 推荐使用 `userdel -f dev` / `deluser dev --remove-home`
- usermod -aG group user, 把用户加入组
- usermod -d /new/home -m user

## 修改默认配置和安装使用 oh-my-zsh 

```bash
# 安装常用软件
apt-get update
apt-get install -y build-essential checkinstall
apt-get install -y gcc g++ make
apt-get install -y nginx aria2 axel
apt-get install -y vim tree ufw wget curl git supervisor psmisc
apt-get install -y screen
apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
apt-get install -y python3 python3-pip python3-setuptools

#4. 安装 oh-my-zsh
#apt-get install -y zsh && wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
apt-get install -y zsh && wget https://gitee.com/dodoru/ohmyzsh/raw/master/tools/install.sh -O - | sh

mv /root/.oh-my-zsh /usr/share/oh-my-zsh
cp /usr/share/oh-my-zsh/templates/zshrc.zsh-template  /usr/share/oh-my-zsh/templates/zshrc.zsh-template.origin
vi /usr/share/oh-my-zsh/templates/zshrc.zsh-template
# wget ../conf/zshrc.txt
# cp zshrc.sample /etc/skel/.zshrc
# 修改 oh-my-zsh 主题
#
# vi ~/.zshrc
#   """
#   export PATH=$HOME/bin:/usr/local/bin:$PATH
#   export ZSH=/usr/share/oh-my-zsh
#   ZSH_THEME="candy"
#
#   # locale
#   export LANG=en_US.UTF-8
#   export LANGUAGE=en_US.UTF-8
#   export LC_ALL=en_US.UTF-8
#   """
cp /usr/share/oh-my-zsh/templates/zshrc.zsh-template /etc/skel/.zshrc


#5. 修改默认配置
mkdir /root/bak
#cp /usr/share/oh-my-zsh/templates/zshrc.zsh-template /etc/skel/.zshrc
cp /etc/default/useradd /root/bak/etc_default_useradd
#vi /etc/default/useradd
#    # SHELL=/bin/sh
#    SHELL=/usr/bin/zsh

cp /etc/adduser.conf /root/bak/etc_adduser.conf
#vi /etc/adduser.conf
#   # DSHELL=/bin/bash
#   DSHELL=/usr/bin/zsh

chsh -s /usr/bin/zsh root
#useradd -m develop
#deluser develop --remove-home
#chsh -s /usr/bin/zsh develop
## useradd bugs for ignore /etc/default/useradd
```

- [useradd vs adduser](https://askubuntu.com/questions/345974/what-is-the-difference-between-adduser-and-useradd)