
## Linux 应用进程管理
 
### supervisor 

 - install : `pip install supervisor` / `apt-get install supervisor` / `npm install -g supervisor`

 - Supervisor 是一个 C/S 模型的程序，supervisord 是 server 端，supervisorctl 是 client 端
 
 - 常用命令 [Supervisor 管理后台守护进程](https://www.jianshu.com/p/b21f1abea5d2)
 
```bash
supervisord -c /srv/serivces/project1/supervisord.conf

#supervisorctl 操作
#查看正在守候的进程
supervisorctl status
#重新加载配置
supervisorctl reread
#更新新的配置到supervisord
supervisorctl update
#重新启动配置中的所有程序
supervisorctl reload
#启动某个进程(program_name=你配置中写的程序名称)
supervisorctl start program_name
#停止某一进程 (program_name=你配置中写的程序名称)
pervisorctl stop program_name
#重启某一进程 (program_name=你配置中写的程序名称)
supervisorctl restart program_name
#停止全部进程
supervisorctl stop all 
```

- supervisord 和 docker 是好搭档

- 配置模型 
 
```buildoutcfg
; -- supervisord.conf --
; usage: supervisord -c /etc/supervisord.conf
; Notes:
;  - Shell expansion ("~" or "$HOME") is not supported.  Environment
;    variables can be expanded using this syntax: "%(ENV_HOME)s".
;  - Comments must have a leading space: "a=b ;comment" not "a=b;comment".

[unix_http_server]
file=/tmp/supervisor.sock   ; (the path to the socket file)

[supervisord]
logfile=/tmp/supervisord.log ; (main log file;default $CWD/supervisord.log)
logfile_maxbytes=50MB        ; (max main logfile bytes b4 rotation;default 50MB)
logfile_backups=10           ; (num of main logfile rotation backups;default 10)
loglevel=info                ; (log level;default info; others: debug,warn,trace)
pidfile=/tmp/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
nodaemon=false               ; (start in foreground if true;default false)
minfds=1024                  ; (min. avail startup file descriptors;default 1024)
minprocs=200                 ; (min. avail process descriptors;default 200)

; the below section must remain in the config file for RPC
; (supervisorctl/web interface) to work, additional interfaces may be
; added by defining them in separate rpcinterface: sections
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket

[program:{{project_name}}]
command=gunicorn -k gevent -c gunicorn_conf.py wsgi:app
process_name=%(program_name)s_%(process_num)s
numprocs=1
directory=.
stdout_logfile=./log/{{project_name}}.log
stdout_logfile_maxbytes=8MB
stdout_logfile_backups=5
redirect_stderr=true
stopsignal=HUP

[program:celery_tasks]
command=celery worker -A celery_tasks -B -l info -E
process_name=%(program_name)s_%(process_num)s
numprocs=1
directory=./src
stdout_logfile=./log/celery_tasks.log
stdout_logfile_maxbytes=8MB
stdout_logfile_backups=5
autostart=true
autorestart=true
redirect_stderr=true
stopsignal=KILL
```

