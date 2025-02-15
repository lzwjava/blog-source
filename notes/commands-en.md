---
layout: post  
title: "macOS Shell Commands"
audio: true  
---

Here are 200 commonly used macOS shell commands, categorized for easier reference. These commands are useful for navigating the file system, managing files, system monitoring, and more.

### File System Navigation
1. `ls` - List directory contents.
2. `cd` - Change the current directory.
3. `pwd` - Print the current working directory.
4. `tree` - Display directories as trees (if installed).

### File Operations
5. `cp` - Copy files or directories.
6. `mv` - Move or rename files or directories.
7. `rm` - Remove files or directories.
8. `touch` - Create an empty file or update the timestamp.
9. `mkdir` - Create a new directory.
10. `rmdir` - Remove an empty directory.
11. `ln` - Create hard and symbolic links.
12. `chmod` - Change file permissions.
13. `chown` - Change file owner and group.
14. `cat` - Concatenate and display file content.
15. `less` - View file content page by page.
16. `more` - View file content page by page.
17. `head` - Display the first lines of a file.
18. `tail` - Display the last lines of a file.
19. `nano` - Edit text files.
20. `vi` - Edit text files.
21. `vim` - Edit text files (enhanced version of `vi`).
22. `find` - Search for files in a directory hierarchy.
23. `locate` - Find files by name quickly.
24. `grep` - Search text using patterns.
25. `diff` - Compare files line by line.
26. `file` - Determine file type.
27. `stat` - Display file or file system status.
28. `du` - Estimate file space usage.
29. `df` - Report file system disk space usage.
30. `dd` - Convert and copy a file.
31. `tar` - Store, list, or extract files in an archive.
32. `gzip` - Compress or decompress files.
33. `gunzip` - Decompress files compressed with gzip.
34. `zip` - Package and compress files.
35. `unzip` - Extract compressed files in a ZIP archive.
36. `rsync` - Remote file and directory synchronization.
37. `scp` - Secure copy files between hosts.
38. `curl` - Transfer data from or to a server.
39. `wget` - Download files from the web.

### System Information
40. `uname` - Print system information.
41. `top` - Display system processes.
42. `htop` - Interactive process viewer (if installed).
43. `ps` - Report a snapshot of current processes.
44. `kill` - Send a signal to a process.
45. `killall` - Kill processes by name.
46. `bg` - Run jobs in the background.
47. `fg` - Run jobs in the foreground.
48. `jobs` - List active jobs.
49. `nice` - Run a program with modified scheduling priority.
50. `renice` - Alter priority of running processes.
51. `time` - Time a command's execution.
52. `uptime` - Show how long the system has been running.
53. `who` - Show who is logged on.
54. `w` - Show who is logged on and what they are doing.
55. `whoami` - Print the current user name.
56. `id` - Print user and group information.
57. `groups` - Print the groups a user is in.
58. `passwd` - Change user password.
59. `sudo` - Execute a command as another user.
60. `su` - Switch user.
61. `chroot` - Run a command with a different root directory.
62. `hostname` - Show or set the system's host name.
63. `ifconfig` - Configure a network interface.
64. `ping` - Send ICMP ECHO_REQUEST to network hosts.
65. `traceroute` - Trace the route to a network host.
66. `netstat` - Network statistics.
67. `route` - Show or manipulate the IP routing table.
68. `dig` - DNS lookup utility.
69. `nslookup` - Query Internet name servers interactively.
70. `host` - DNS lookup utility.
71. `ftp` - Internet file transfer program.
72. `ssh` - OpenSSH SSH client.
73. `telnet` - User interface to the TELNET protocol.
74. `nc` - Netcat, arbitrary TCP and UDP connections and listens.
75. `iftop` - Display bandwidth usage on an interface (if installed).
76. `nmap` - Network exploration tool and security/port scanner (if installed).

### Disk Management
77. `mount` - Mount a filesystem.
78. `umount` - Unmount a filesystem.
79. `fdisk` - Partition table manipulator for Linux.
80. `mkfs` - Build a Linux filesystem.
81. `fsck` - Check and repair a Linux filesystem.
82. `df` - Report file system disk space usage.
83. `du` - Estimate file space usage.
84. `sync` - Synchronize cached writes to persistent storage.
85. `dd` - Convert and copy a file.
86. `hdparm` - Get/set hard disk parameters.
87. `smartctl` - Control and monitor SMART-enabled ATA/SCSI-3 drives (if installed).

### Package Management
88. `brew` - Homebrew package manager (if installed).
89. `port` - MacPorts package manager (if installed).
90. `gem` - RubyGems package manager.
91. `pip` - Python package installer.
92. `npm` - Node.js package manager.
93. `cpan` - Perl package manager.

### Text Processing
94. `awk` - Pattern scanning and processing language.
95. `sed` - Stream editor for filtering and transforming text.
96. `sort` - Sort lines of text files.
97. `uniq` - Report or omit repeated lines.
98. `cut` - Remove sections from each line of files.
99. `paste` - Merge lines of files.
100. `join` - Join lines of two files on a common field.
101. `tr` - Translate or delete characters.
102. `iconv` - Convert text from one encoding to another.
103. `strings` - Find printable strings in files.
104. `wc` - Print newline, word, and byte counts for each file.
105. `nl` - Number lines of files.
106. `od` - Dump files in various formats.
107. `xxd` - Make a hexdump or do the reverse.

### Shell Scripting
108. `echo` - Display a line of text.
109. `printf` - Format and print data.
110. `test` - Evaluate an expression.
111. `expr` - Evaluate expressions.
112. `read` - Read a line from standard input.
113. `export` - Set an environment variable.
114. `unset` - Unset values and attributes of shell variables and functions.
115. `alias` - Create an alias for a command.
116. `unalias` - Remove an alias.
117. `source` - Execute commands from a file in the current shell.
118. `exec` - Execute a command.
119. `trap` - Trap signals and other events.
120. `set` - Set or unset shell options and positional parameters.
121. `shift` - Shift positional parameters.
122. `getopts` - Parse positional parameters.
123. `type` - Describe a command.
124. `which` - Locate a command.
125. `whereis` - Locate the binary, source, and manual page files for a command.

### Development Tools
126. `gcc` - GNU project C and C++ compiler.
127. `make` - Directory-oriented makefile processor.
128. `cmake` - Cross-platform makefile generator.
129. `autoconf` - Generate configure scripts.
130. `automake` - Generate Makefile.in files.
131. `ld` - The GNU linker.
132. `ar` - Create, modify, and extract from archives.
133. `nm` - List symbols from object files.
134. `objdump` - Display information from object files.
135. `strip` - Discard symbols from object files.
136. `ranlib` - Generate index to archive.
137. `gdb` - The GNU debugger.
138. `lldb` - The LLVM debugger.
139. `valgrind` - Instrumentation framework for building dynamic analysis tools (if installed).
140. `strace` - Trace system calls and signals (if installed).
141. `ltrace` - Trace library calls (if installed).
142. `perf` - Performance analysis tools for Linux.
143. `time` - Time a command's execution.
144. `xargs` - Build and execute command lines from standard input.
145. `m4` - Macro processor.
146. `cpp` - The C Preprocessor.
147. `flex` - Fast Lexical Analyzer generator.
148. `bison` - Yacc-compatible parser generator.
149. `bc` - An arbitrary precision calculator language.
150. `dc` - An arbitrary precision calculator.

### Version Control
151. `git` - Distributed version control system.
152. `svn` - Subversion version control system.
153. `hg` - Mercurial distributed version control system.
154. `cvs` - Concurrent Versions System.

### Miscellaneous
155. `man` - Format and display the online manual pages.
156. `info` - Read Info documents.
157. `apropos` - Search the manual page names and descriptions.
158. `whatis` - Display one-line manual page descriptions.
159. `history` - Display or manipulate the history list.
160. `yes` - Output a string repeatedly until killed.
161. `cal` - Display a calendar.
162. `date` - Display or set the date and time.
163. `sleep` - Delay for a specified amount of time.
164. `watch` - Execute a program periodically, showing output fullscreen.
165. `xargs` - Build and execute command lines from standard input.
166. `seq` - Print a sequence of numbers.
167. `shuf` - Generate random permutations.
168. `tee` - Read from standard input and write to standard output and files.
169. `tput` - Initialize a terminal or query terminfo database.
170. `stty` - Change and print terminal line settings.
171. `clear` - Clear the terminal screen.
172. `reset` - Reset the terminal to a sane state.
173. `script` - Make typescript of terminal session.
174. `wall` - Write a message to all users.
175. `write` - Send a message to another user.
176. `mesg` - Control write access to your terminal.
177. `talk` - Talk to another user.
178. `ytalk` - Yet another talk program (if installed).
179. `crontab` - Maintain crontab files for individual users.
180. `at` - Schedule commands to be executed once at a later time.
181. `batch` - Schedule commands to be executed in a batch queue.
182. `nice` - Run a program with modified scheduling priority.
183. `renice` - Alter priority of running processes.
184. `time` - Time a command's execution.
185. `ulimit` - Set or report user resource limits.
186. `pr` - Convert text files for printing.
187. `lp` - Send files to a printer.
188. `lpr` - Print files.
189. `lpq` - Show printer queue status.
190. `lprm` - Remove jobs from the printer queue.
191. `enscript` - Convert text to PostScript, HTML, or RTF, with syntax highlighting (if installed).
192. `a2ps` - Any to PostScript filter.
193. `ps2pdf` - Convert PostScript to PDF.
194. `pdf2ps` - Convert PDF to PostScript.
195. `gs` - Ghostscript interpreter.
196. `convert` - Convert between image formats (if installed).
197. `mogrify` - Resize, rotate, and transform images (if installed).
198. `exiftool` - Read, write, and edit meta information in files (if installed).
199. `jpegoptim` - Optimize JPEG files (if installed).
200. `optipng` - Optimize PNG files (if installed).

These commands cover a wide range of functionalities and are essential for users who want to efficiently manage and interact with their macOS system through the terminal.