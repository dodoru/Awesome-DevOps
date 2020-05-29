
## 日志文件的管理 logrotate
- `/etc/logrotate.conf`

```text 
# see "man logrotate" for details
# rotate log files weekly
weekly

# keep 4 weeks worth of backlogs
rotate 4

# create new (empty) log files after rotating old ones
create

# uncomment this if you want your log files compressed
#compress

# packages drop log rotation information into this directory
include /etc/logrotate.d

# no packages own wtmp, or btmp -- we'll rotate them here
/var/log/wtmp {
    missingok
    monthly
    create 0664 root utmp
    rotate 1
}

/var/log/btmp {
    missingok
    monthly
    create 0660 root utmp
    rotate 1
}

# system-specific logs may be configured here
```

- 推荐配置：`/etc/logrotate.d/nginx`

```text
/var/log/nginx/*.log 
/var/log/nginx/*/*.log{
        daily
        missingok
        rotate 14
        compress
        delaycompress
        notifempty
        create 0640 www-data adm
        sharedscripts
        prerotate
                if [ -d /etc/logrotate.d/httpd-prerotate ]; then \
                        run-parts /etc/logrotate.d/httpd-prerotate; \
                fi \
        endscript
        postrotate
                invoke-rc.d nginx rotate >/dev/null 2>&1
        endscript
}
```

- 推荐配置：`/etc/logroate.d/pm2-log`

```text
/root/.pm2/pm2.log
/root/.pm2/logs/*.log
/home/*/.pm2/pm2.log
/home/*/.pm2/logs/*.log
{
        rotate 15
        daily
        missingok
        notifempty
        compress
        delaycompress
        copytruncate
        create 0640 developer developer
        dateext
                dateformat %Y-%m-%d.
        extension log
}
```