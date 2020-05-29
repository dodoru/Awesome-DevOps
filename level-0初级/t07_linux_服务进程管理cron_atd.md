
# Linux 进程管理

## 自动化任务 cron / atd

- [使用 cron 和 atd运行计划任务] https://debian-handbook.info/browse/zh-CN/stable/sect.task-scheduling-cron-atd.html
- `at` : 指定未来特定时间运行某个命令
- `crontab` :周期执行任务
 - 使用
  
```text
usage:	crontab [-u user] file
	crontab [ -u user ] [ -i ] { -e | -l | -r }
		(default operation is replace, per 1003.2)
	-e	(edit user's crontab)
	-l	(list user's crontab)
	-r	(delete user's crontab)
	-i	(prompt before deleting user's crontab)
```
 
 - 配置 /etc/crontab
 
```bash
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
# 每日监控数据迁移azure
#5 0 * * * root cd /srv/s3 && sh tools/daily_monitor_stat.sh

# 定时抓取netdig 日志
#0 * * * * root cd /srv/s5 &&  node jobs/download_netdig_job.js >> /mnt/disk2/netdig/info.log 2>&1

# 迁移backup 监控数据
#0 2 * * * root cd /srv/s3 && node jobs/procinfo_backup_job.js >> data/logs/procinfo_backup.log 2>&1
#0 6 * * * root cd /srv/s3 && node jobs/uptime_backup_job.js >> data/logs/uptime_backup.log 2>&1


## 迁移备份s7 的图像和视频(image/video)
# 30 2 * * * cd /mnt/disk4/s7/scripts && screen -dmS "s7oss" /bin/bash daily_job.sh
```

 - `crontab -e` 和 `vi /etc/crontab` 的区别: 前者 /tmp/crontab.$rand/crontab

