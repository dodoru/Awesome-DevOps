


## 运维基础测试题

请先查阅 [web服务初级运维](https://github.com/dodoru/Awesome-DevOps/tree/master/level-0%E5%88%9D%E7%BA%A7)


### 1. Linux系统中，通常以下哪个目录提供了管理程序相关的命令或工具？（多选）
    A. /bin    B. /sbin     C. /usr/bin   D. /usr/sbin

    答案：BD
   
    
### 2. 关于 Linux 系统的文件权限，以下哪种说法是错误的？（单选）
    A. 可以使用 chmod 修改文件的权限
    B. 可以使用 chown 修改文件的所属用户和组
    C. 可以通过 usermod 把指定用户添加到组
    D. 用户的 home 目录一旦设置后，不可再更改

    答案：D
    

### 3. 关于防火墙ufw， 以下哪种说法是错误的 ？（单选）
    A. ufw 是基于 iptables 之上的防火墙工具，全称为 uncomplicated firewall
    B. 禁止外部访问 smtp 服务，可配置： ufw deny smtp
    C. 启动 ufw 的设置的命令是： ufw enable
    D. ufw 具有 iptables 的所有功能，完全可以取代 iptables

    答案：D
    
    
### 4. 关于远程登录ssh，以下哪种说法是错误的 ？(单选)
    A. 默认用户dev的ssh目录为 /home/dev/.ssh, 且权限必须为 700
    B. 如果要修改 ssh 的默认端口，通常修改配置文件为 /etc/ssh/ssh_config
    C. 如果要禁止 ssh 的密码登录，通常修改配置文件为 /etc/ssh/sshd_config
    D. 修改 /etc/ssh/sshd_config 后，需要执行 service ssh restart 才能起效
    
    答案：C
    
    
### 5. 关于日志文件管理 logrotate, 以下哪种说法是错误的 ？（单选）
    A. 默认自定义的日志文件管理配置目录为: /etc/logrotate.d/
    B. 配置日志路径时，设置 /var/log/nginx/*.log 可包含 /var/log/nginx 的子目录下的日志文件，eg: /var/log/nginx/s5/s5.log
    C. 配置日志管理时，可以通过 prerotate 来执行预处理脚本
    D. 默认条件下，需要使用 root 权限对 logrotate 进行配置
    
    答案：C
    
    
### 6. 关于自动化任务管理 cron / atd, 以下哪种说法是错误的 ？（单选）     
    A. crontab 通常用于周期执行脚本任务，一般配置文件为 /etc/crontab 
    B. Linux可以通过命令 at 来指定未来特定时间来运行某个任务
    C. crontab 的配置最小单位为秒，配置后无需手动重启 crontab 服务，配置会立即生效
    D. Linux 默认支持任意用户执行 crontab 命令
    
    答案：C
      (最小单位是分钟, 想要完成"秒"级别任务，需要额外借助于其他机制，
    例如可以定义每分钟定时计划任务，再利用脚本实现在每分钟之内，循环执行多次)
    
### 7. (附加题) t06_linux_logrotate 中简要介绍了 logrotate 并出示了配置模板, 其中有提到

```L103,L106
# !-- 注意不要同时使用以下选项
# dateformat %Y-%m-%d.
# extension log
# 请自行测试理解发生了什么事情 @2020年12月15日--!
``` 

请对此做出你的理解和描述.


 
    


