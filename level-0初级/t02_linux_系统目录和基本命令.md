
## 1-2. linux 系统目录和基本命令

```
    /        根目录   

    /boot    启动目录: 核心文件（连接文件/镜像文件）
    /dev     设备文件命令: 访问 linux 外部设备


    /bin     命令保存目录: 常被 $PATH 引入, 
                eg: /bin/zsh, /bin/sh

    /sbin    系统管理程序：super user's bin (root)
                eg: /sbin/ifconfig, /sbin/route, /sbin/ip, /sbin/iptables, 
                    /sbin/e2fsck, /sbin/cfdisk, /sbin/chcpu, /sbin/fsck

    /usr     用户的应用程序和文件: (类似 Windows 的 C:/program files) 
                eg: ls /usr -> bin  etc sbin  share  src  games  include  lib  lib32  local
        
        /usr/bin    系统用户的应用程序, eg： /usr/bin/openssl, /usr/bin/zip
        /usr/sbin   超级用户使用的管理程序/系统守护程序(root), eg: /usr/sbin/logrotate, /usr/sbin/nginx,  /usr/sbin/iftop
        /usr/share  共享的应用程序目录(drwxr-xr-x), eg： /usr/share/javascript/  /usr/share/java/
     
                

    /etc     系统配置目录
                eg: /etc/nginx, /etc/mysql 

    /lib     系统动态连接共享库：常用基础软件， 
                eg: /lib/systemd, /lib/ufw, /lib/init

    /sys     系统服务的虚拟档案系统：记录核心模组/硬件设备的信息, 不占硬盘容量
             linux2.6 出现 sysfs，通过文件系统直观反映内核设备树: 针对进程信息的proc文件系统、针对设备的devfs文件系统以及针对伪终端的devpts文件系统。
                eg: 通常包括：block  bus  class  dev  devices  firmware  fs  hypervisor  kernel  module  power
                

    /proc    进程服务的虚拟目录：映射系统内存(root权限）, 不占硬盘容量
                eg: /proc/<int:$pid> , 通常包含文件：cwd, exe, mem, stat, task/, fd/, fdinfo/, map_files/, attr/ , ns/, net/ 
        
    /root    root用户主目录

    /home    普通用户主目录
                eg: /home/user


    /var     ; /var/log 
    /opt     个性化安装目录：默认为空，建议用户自行建立
    /srv     存放服务启动后需要提取数据的文件目录 
             建议使用 /srv/services 统一部署(自开发的)应用服务, chown dev:dev -R /srv/services
    /tmp     临时文件目录：通常可以设置垃圾回收策略，定时清理 
    /run     临时文件目录：存储系统启动以来的信息，系统重启后会自动删除或清理，通常` ln -s /run /var/run `


    /mnt     系统挂载目录: 扩展存储空间，挂载云盘，挂载光驱
    /lost+found  系统备份：系统意外崩溃/关机后产生文件碎片，系统开机时 fsck 会检查这里和尝试修复文件系统。
    
```

refer: 
- [IBM博客：使用 /sys 文件系统访问 Linux 内核](https://www.ibm.com/developerworks/cn/linux/l-cn-sysfs/)
- [菜鸟教程：Linux 命令大全](https://www.runoob.com/linux/linux-command-manual.html)
- [菜鸟教程：Linux 系统目录结构](https://www.runoob.com/linux/linux-system-contents.html)
- [cnblogs: Linux下/sys目录介绍](https://www.cnblogs.com/cuckoo-/p/10742367.html)
- [Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)


## 推荐使用工具网站:

- [Bash scripting cheatsheet](https://devhints.io/bash)
