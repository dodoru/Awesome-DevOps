"""
# 字符串整理

 通过 `cat /etc/services` , 我们可以列举 linux 常见的网络端口
 但是这个文件里的内容, 对于机器是易读, 但对于人而言却排版有点乱
 现在, 我们需要把该文件内容重新整理, 使其整整齐齐, 一目了然
 整理的需求如下:
    1. 对齐所有的行列
    2. 不使用 tab, 全使用空格
    3. 两列之间的空格至少为4个

eg: 整理前[L193,L199]
klogin		543/tcp				# Kerberized `rlogin' (v5)
kshell		544/tcp		krcmd		# Kerberized `rsh' (v5)
dhcpv6-client	546/tcp
klogin		543/tcp				# Kerberized `rlogin' (v5)
dhcpv6-client	546/udp
dhcpv6-server	547/tcp
dhcpv6-server	547/udp
afpovertcp	548/tcp				# AFP over TCP


==> 整理后
klogin           543/tcp             # Kerberized `rlogin' (v5)
kshell           544/tcp    krcmd    # Kerberized `rsh' (v5)
dhcpv6-client    546/tcp
dhcpv6-client    546/udp
dhcpv6-server    547/tcp
dhcpv6-server    547/udp
afpovertcp       548/tcp             # AFP over TCP

# refer: level-0初级/t12_linux_常用网络端口.md
# 请在下方实现你的代码, 并且提出pull-request
"""


