---
audio: true
generated: true
lang: ar
layout: post
title: OpenWrt Invasion on Xiaomi Mi Router 4C
translated: true
---

هذا هو محاولتي الثالثة لتثبيت OpenWrt. المرة الأولى كانت في عام 2019، عندما استخدمت منفذ UART للاتصال. المرة الثانية كانت في عام 2023، عندما استخدمت طريقة بعيدة مشابهة لتلك الوصفها هنا.

يمكن العثور على كود الاستغلال في [https://github.com/acecilia/OpenWRTInvasion](https://github.com/acecilia/OpenWRTInvasion).

أولاً، قم بتثبيت المتطلبات:

```bash
pip install -r requirements.txt --break-system-packages
```

بعد تشغيل الاستغلال، يمكنك الوصول إلى واجهة الويب للمروحة في عنوان URL مشابه لهذا (سيعتمد قيمة `stok`):

`http://192.168.1.28/cgi-bin/luci/;stok=fe9b14c5c4dee48709fbdf00e048d5ec/web/home`

```bash
lzwjava@anonymous OpenWRTInvasion % python remote_command_execution_vulnerability.py
Router IP address [press enter for using the default 'miwifi.com']: 192.168.1.28
Enter router admin password: ...
هناك خياران لتوفير الملفات اللازمة للغزو:
   1. استخدام خادم ملفات TCP المحلي يعمل على منفذ عشوائي لتوفير الملفات في الدليل المحلي `script_tools`.
   2. تحميل الملفات المطلوبة من مستودع GitHub البعيد. (اختر هذا الخيار فقط إذا كان GitHub متاحًا داخل جهاز المروحة.)
أي خيار تفضل؟ (الاختيار الافتراضي: 1)1
****************
router_ip_address: 192.168.1.28
stok: 08f4f22fed20b94580cb8e70703c941c
file provider: local file server
****************
start uploading config file...
start exec command...
local file server is runing on 0.0.0.0:63067. root='script_tools'
local file server is getting 'busybox-mipsel' for 192.168.1.28.
local file server is getting 'dropbearStaticMipsel.tar.bz2' for 192.168.1.28.
done! Now you can connect to the router using several options: (user: root, password: root)
* telnet 192.168.1.28
* ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa -c 3des-cbc -o UserKnownHostsFile=/dev/null root@192.168.1.28
* ftp: using a program like cyberduck

root@XiaoQiang:/tmp# wget "https://downloads.openwrt.org/releases/24.10.0/targets/ramips/mt76x8/openwrt-24.10.0-ramips-mt76x8-xiaomi_mi-router-4c-squashfs-sysupgr
ade.bin"
wget: not an http or ftp url: https://downloads.openwrt.org/releases/24.10.0/targets/ramips/mt76x8/openwrt-24.10.0-ramips-mt76x8-xiaomi_mi-router-4c-squashfs-sysupgrade.bin

scp -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa -c 3des-cbc  openwrt-24.10.0-ramips-mt76x8-xiaomi_mi-router-4c-squashfs-sysupgrade.bin root@192.168.1.28:/tmp/
ash: /usr/libexec/sftp-server: not found
scp: Connection closed

cat openwrt-24.10.0-ramips-mt76x8-xiaomi_mi-router-4c-squashfs-sysupgrade.bin | ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa root@192.168.1.28 "cat > /tmp/openwrt-24.10.0-ramips-mt76x8-xiaomi_mi-router-4c-squashfs-sysupgrade.bin"

root@XiaoQiang:/tmp# ls
2541.bootcheck.log                                                         oui
TZ                                                                         rc.done
appStoreRule.json                                                          rc.timing
arrays                                                                     resolv.conf
authenfailed-cache                                                         resolv.conf.auto
busybox                                                                    root
daemon                                                                     rr
datalist                                                                   run
dropbear                                                                   script.sh
dropbear.tar.bz2                                                           speedtest_urls.xml
etc                                                                        spool
ftpd                                                                       startscene_crontab.lua.PID
lock                                                                       stat_points_privacy.log
log                                                                        stat_points_rom.log
logexec                                                                    state
luci-indexcache                                                            sysapihttpd
luci-nonce                                                                 sysapihttpdconf
luci-sessions                                                              sysinfo
messages                                                                   syslog-ng.ctl
miqos.lock                                                                 syslog-ng.pid
mnt                                                                        taskmonitor
mt76xx2.sh.log                                                             uci2dat_mt7628.log
network.env                                                                uploadfiles
nginx_check.log                                                            upnp.leases
ntp.status                                                                 web_config_list
openwrt-24.10.0-ramips-mt76x8-xiaomi_mi-router-4c-squashfs-sysupgrade.bin  wifi_analysis.log

root@XiaoQiang:/tmp# mtd -r write openwrt-24.10.0-ramips-mt76x8-xiaomi_mi-router-4c-squashfs-sysupgrade.bin OS1
Unlocking OS1 ...

Writing from openwrt-24.10.0-ramips-mt76x8-xiaomi_mi-router-4c-squashfs-sysupgrade.bin to OS1 ...  [w]

اتصل بالمروحة عبر اتصال سلكي. يمكنك بعد ذلك الوصول إلى واجهة الويب في 192.168.1.1 أو استخدام SSH من خلال تشغيل `ssh root@192.168.1.1`.