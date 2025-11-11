---
audio: false
generated: true
lang: hant
layout: post
title: 最有用的 100 個 Linux 指令
translated: true
type: note
---

根據你作為一名高度技術導向、自學成才的全端工程師背景，擁有豐富的Linux環境經驗、演算法問題解決能力，並熟悉雲端平台、容器和分散式系統，我為你精心挑選了**前100個實用Linux指令**，專為你在**Ubuntu**系統上使用而量身定制。這些指令的選擇契合你在全端開發、行動工程、機器學習和系統管理方面的專業能力，同時也支援你的自學研究與開源貢獻。它們涵蓋檔案管理、系統監控、網路連線、開發、自動化和進階腳本編寫，與你在TEKsystems的工作、過往職位及個人專案息息相關。

這些指令按類別分組以便清晰查閱，並附帶簡要說明，強調其實際應用與你的技能組合的契合度。我優先選擇能提升生產力、除錯效率和系統最佳化的指令，假設你已熟悉終端機工作流程，並可能在開發、部署或研究任務中使用這些指令。如果你需要，我可以提供特定指令的範例或腳本，或根據你的工作流程（例如開發與系統管理任務）生成指令使用頻率圖表。請隨時告訴我！

### **檔案與目錄管理（15個指令）**
1. **ls** - 列出目錄內容（`ls -la` 可顯示包含隱藏檔的詳細資訊）。
2. **cd** - 切換目錄（`cd ~/projects` 可導航至你的GitHub專案資料夾）。
3. **pwd** - 顯示目前工作目錄（適用於腳本編寫或路徑驗證）。
4. **mkdir** - 建立目錄（`mkdir -p src/main/java` 可建立嵌套專案結構）。
5. **rm** - 刪除檔案或目錄（`rm -rf temp/` 可遞迴刪除）。
6. **cp** - 複製檔案/目錄（`cp -r src/ backup/` 適用於專案備份）。
7. **mv** - 移動/重新命名檔案（`mv old.java new.java` 適用於重構）。
8. **touch** - 建立空白檔案（`touch script.sh` 用於新增腳本）。
9. **find** - 搜尋檔案（`find / -name "*.java"` 可定位原始碼檔案）。
10. **locate** - 快速依名稱尋找檔案（`locate config.yaml` 用於搜尋設定檔）。
11. **du** - 估算磁碟使用量（`du -sh /var/log` 可檢查日誌大小）。
12. **df** - 顯示磁碟空間（`df -h` 以易讀格式顯示）。
13. **ln** - 建立連結（`ln -s /path/to/project symlink` 用於建立捷徑）。
14. **chmod** - 變更檔案權限（`chmod 755 script.sh` 用於設定可執行腳本）。
15. **chown** - 變更檔案擁有者（`chown user:group file` 用於部署）。

### **文字處理與操作（15個指令）**
16. **cat** - 顯示檔案內容（`cat log.txt` 用於快速檢查日誌）。
17. **less** - 互動式檢視檔案（`less server.log` 用於大型日誌檔案）。
18. **more** - 分頁顯示檔案輸出（`more README.md` 用於閱讀文件）。
19. **head** - 顯示檔案開頭幾行（`head -n 10 data.csv` 用於資料預覽）。
20. **tail** - 顯示檔案末尾幾行（`tail -f app.log` 用於即時日誌監控）。
21. **grep** - 搜尋文字模式（`grep -r "error" /var/log` 用於除錯）。
22. **awk** - 處理文字欄位（`awk '{print $1}' access.log` 用於日誌解析）。
23. **sed** - 串流編輯器（`sed 's/old/new/g' file` 用於文字替換）。
24. **cut** - 從行中提取區段（`cut -d',' -f1 data.csv` 用於CSV檔案）。
25. **sort** - 排序行（`sort -n data.txt` 用於數值排序）。
26. **uniq** - 移除重複行（`sort file | uniq` 用於取得唯一項目）。
27. **wc** - 計算行數、字數或字元數（`wc -l code.java` 用於行數統計）。
28. **tr** - 轉換字元（`tr '[:lower:]' '[:upper:]' < file` 用於大小寫轉換）。
29. **tee** - 寫入檔案並輸出至標準輸出（`cat input | tee output.txt` 用於記錄）。
30. **diff** - 比較檔案（`diff old.java new.java` 用於程式碼變更比對）。

### **系統監控與效能（15個指令）**
31. **top** - 互動式監控系統行程（即時CPU/記憶體使用情況）。
32. **htop** - 增強型行程檢視器（`htop` 提供更佳視覺化）。
33. **ps** - 列出行程（`ps aux | grep java` 用於查詢Java應用程式）。
34. **free** - 檢查記憶體使用量（`free -m` 以MB格式顯示）。
35. **vmstat** - 虛擬記憶體統計（`vmstat 1` 用於持續更新）。
36. **iostat** - 監控I/O效能（`iostat -x` 用於磁碟統計）。
37. **uptime** - 顯示系統運行時間與負載（`uptime` 用於快速檢查）。
38. **lscpu** - 顯示CPU資訊（`lscpu` 用於查看系統規格）。
39. **lsblk** - 列出區塊裝置（`lsblk` 用於磁碟/分割區詳細資訊）。
40. **iotop** - 依行程監控磁碟I/O（`iotop` 用於效能除錯）。
41. **netstat** - 網路統計（`netstat -tuln` 用於監聽埠檢查）。
42. **ss** - netstat的現代替代方案（`ss -tuln` 用於通訊端檢查）。
43. **dmesg** - 檢視核心訊息（`dmesg | grep error` 用於排查系統問題）。
44. **sar** - 收集系統活動（`sar -u 1` 用於CPU監控）。
45. **pmap** - 行程記憶體映射（`pmap -x <pid>` 用於記憶體除錯）。

### **網路與連線（15個指令）**
46. **ping** - 測試網路連線（`ping google.com` 用於檢查連通性）。
47. **curl** - 從URL獲取資料（`curl -X POST api` 用於API測試）。
48. **wget** - 下載檔案（`wget file.tar.gz` 用於取得專案相依套件）。
49. **netcat** - 網路工具（`nc -l 12345` 用於建立簡易伺服器）。
50. **ifconfig** - 網路介面資訊（`ifconfig eth0` 用於查看IP詳細資訊）。
51. **ip** - 現代網路設定（`ip addr` 用於查看介面詳細資訊）。
52. **nslookup** - 查詢DNS（`nslookup domain.com` 用於DNS除錯）。
53. **dig** - 詳細DNS查詢（`dig domain.com` 用於取得DNS記錄）。
54. **traceroute** - 追蹤網路路徑（`traceroute google.com` 用於路由追蹤）。
55. **telnet** - 測試埠連線（`telnet localhost 8080` 用於服務測試）。
56. **scp** - 安全複製檔案（`scp file user@server:/path` 用於檔案傳輸）。
57. **rsync** - 高效同步檔案（`rsync -avz src/ dest/` 用於備份）。
58. **ufw** - 管理防火牆（`ufw allow 80` 用於開放網頁伺服器存取）。
59. **iptables** - 設定防火牆規則（`iptables -L` 用於列出規則）。
60. **nmap** - 網路掃描（`nmap localhost` 用於檢查開放埠）。

### **開發與腳本編寫（15個指令）**
61. **gcc** - 編譯C程式（`gcc -o app code.c` 用於建置）。
62. **javac** - 編譯Java程式碼（`javac Main.java` 用於你的Java專案）。
63. **java** - 執行Java程式（`java -jar app.jar` 用於執行）。
64. **python3** - 執行Python腳本（`python3 script.py` 用於機器學習任務）。
65. **node** - 執行Node.js（`node app.js` 用於JavaScript專案）。
66. **npm** - 管理Node套件（`npm install` 用於前端相依套件）。
67. **git** - 版本控制（`git commit -m "update"` 用於你的GitHub儲存庫）。
68. **make** - 建置專案（`make -f Makefile` 用於自動化）。
69. **mvn** - Maven建置工具（`mvn package` 用於Java專案）。
70. **gradle** - Gradle建置工具（`gradle build` 用於Android專案）。
71. **docker** - 管理容器（`docker run -p 8080:8080 app` 用於部署）。
72. **kubectl** - 管理Kubernetes（`kubectl get pods` 用於叢集管理）。
73. **virtualenv** - Python虛擬環境（`virtualenv venv` 用於機器學習）。
74. **gdb** - 偵錯程式（`gdb ./app` 用於C/Java除錯）。
75. **strace** - 追蹤系統呼叫（`strace -p <pid>` 用於除錯）。

### **套件管理（10個指令）**
76. **apt** - 套件管理員（`apt install vim` 用於軟體安裝）。
77. **apt-get** - 進階套件工具（`apt-get upgrade` 用於系統更新）。
78. **dpkg** - 管理.deb套件（`dpkg -i package.deb` 用於手動安裝）。
79. **apt-cache** - 查詢套件資訊（`apt-cache search java` 用於搜尋套件）。
80. **snap** - 管理snap套件（`snap install code` 用於安裝VS Code）。
81. **update-alternatives** - 管理預設應用程式（`update-alternatives --config java`）。
82. **add-apt-repository** - 新增PPA（`add-apt-repository ppa:repo` 用於新增來源）。
83. **apt-file** - 尋找套件檔案（`apt-file search /bin/bash` 用於除錯）。
84. **dpkg-query** - 查詢已安裝套件（`dpkg-query -l` 用於列出套件）。
85. **apt-mark** - 標記套件（`apt-mark hold package` 用於防止升級）。

### **系統管理與安全性（15個指令）**
86. **sudo** - 以root權限執行指令（`sudo apt update` 用於管理任務）。
87. **su** - 切換使用者（`su - user` 用於切換帳戶）。
88. **passwd** - 變更密碼（`passwd user` 用於安全性維護）。
89. **useradd** - 新增使用者（`useradd -m dev` 用於建立新帳戶）。
90. **usermod** - 修改使用者（`usermod -aG sudo dev` 用於權限設定）。
91. **groupadd** - 建立群組（`groupadd developers` 用於存取控制）。
92. **chgrp** - 變更群組擁有權（`chgrp -R dev /project` 用於團隊協作）。
93. **crontab** - 排程任務（`crontab -e` 用於自動化腳本）。
94. **systemctl** - 管理服務（`systemctl start nginx` 用於網頁伺服器）。
95. **journalctl** - 檢視系統日誌（`journalctl -u docker` 用於服務日誌）。
96. **who** - 列出已登入使用者（`who` 用於伺服器監控）。
97. **last** - 顯示登入歷史（`last` 用於安全性稽核）。
98. **shutdown** - 關機（`shutdown -h now` 用於系統關閉）。
99. **reboot** - 重新啟動系統（`reboot` 用於更新後重啟）。
100. **env** - 顯示環境變數（`env | grep PATH` 用於除錯）。

### **與你背景相關的注意事項**
- **開發重點**：如 `git`、`mvn`、`docker` 和 `kubectl` 等指令與你的全端和容器化工作流程高度契合，特別適用於你的10個GitHub專案和雲端經驗（AWS、Azure、阿里雲）。
- **除錯與效能**：包含如 `strace`、`gdb`、`htop` 和 `dmesg` 等工具，以滿足你後端和系統除錯的需求，這與你8年的後端經驗相符。
- **網路連線**：如 `curl`、`netcat` 和 `nmap` 等指令支援你的API和網路專業知識，適用於測試微服務或雲端部署。
- **自動化**：`crontab` 和 `rsync` 對於自動化備份或部署非常實用，與你的自由工作和企業職位相關。
- **研究與學習**：文字處理工具（`grep`、`awk`、`sed`）對於解析日誌或資料集非常有用，可支援你在視覺恢復方面的自學研究。

如果你想深入瞭解任何類別（例如 `awk` 或 `sed` 的腳本範例、Docker工作流程或雲端特定指令），或者希望生成指令使用頻率圖表（例如按任務類型分類的使用頻率），請告訴我！你也可以查看你的GitHub作品集以尋找專案相關的特定指令，或分享更多關於你目前TEKsystems任務的詳細資訊，以獲得更加量身定制的建議。