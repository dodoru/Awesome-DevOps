
# 防火墙 
## ufw
- 基于iptable之上的防火墙工具ufw, 操作更简单，规则更明朗 (uncomplicated firewall)
- 安装： `apt-get install ufw`
- 常用命令：

```bash
ufw allow 22
ufw allow 80
ufw allow 8000
ufw allow 443
ufw allow https
ufw allow http
ufw allow 32220/tcp 

ufw default deny incoming
ufw default allow outgoing
ufw status verbose
ufw enable
ufw disable

ufw allow 15000:16999/tcp
ufw allow 15000:16999/udp
ufw allow from 172.18.223.180 to any port 6379
ufw allow from 172.18.34.33 to any port 3306
ufw allow proto udp 192.168.0.1 port 53 to 192.168.0.2 port 53
ufw status

# 禁止外部访问smtp服务
ufw deny smtp 
# 删除规则
ufw delete deny smtp

# 显示相关网络服务
ufw app list  
# cat ~/.zsh_history | grep ufw
```

## 其它防火墙： netfilter/iptables
- netfilter :  内核内部
- iptables :  让用户定义规则集的表结构
- 可以对流入、流出的信息进行细化控制，它可以 实现防火墙、NAT（网络地址翻译）和数据包的分割等功能 