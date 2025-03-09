---
audio: true
generated: false
lang: hi
layout: post
title: विस्तृत आउटपुट
translated: true
---

- Homebrew में verbose output को enable करने के liye, `export HOMEBREW_CURL_VERBOSE=1` ko `brew upgrade --verbose` ke saath use karein.

- SSH mein verbosity badhane ke liye, `ssh -vvv user@host` use karein.

- `git` ke saath zyada verbose output ke liye, `git -v` ya `git --verbose` use karein.

- `rsync` se zyada output paane ke liye, `rsync -vv source destination` use karein.

- SSH config mein verbose config likhein, jaise ki `.ssh/config` mein `LogLevel VERBOSE` rakhein.

- `npm` ke saath verbose output enable karne ke liye, `npm install --verbose` ya `npm run <script> --verbose` use karein.

- Node.js mein verbose logging ke liye, `NODE_DEBUG` environment variable ka use karein: `NODE_DEBUG=http,net node your_script.js`.

- `curl` se verbose output paane ke liye, `curl -v <url>` use karein.

- `pip` ke saath verbose output enable karne ke liye, `pip install -v <package>` ya `pip install --verbose <package>` use karein.

- `wget` ke saath verbose output ke liye, `wget --verbose <url>` use karein.

- `yum` se verbose output paane ke liye, `yum -v install <package>` use karein.

- `apt-get` ke saath verbose output enable karne ke liye, `apt-get -o Debug::pkgProblemResolver=yes install <package>` use karein.

- `adb` ke saath verbose logging ke liye, `adb logcat -v verbose` use karein.

- Python ko verbose mode mein run karne ke liye, `python -v your_script.py` use karein.

- Java code ko verbose output ke saath compile karne ke liye, `javac -verbose YourClass.java` use karein.

- VSCode ko verbose mode mein start karne ke liye: `code --verbose`. Logging ke liye, `settings.json` mein `"trace": true` set karein aur logs ko "Developer: Open View..." -> "Log (Window)" ya "Log (Extension Host)" ke through dekhein.

- IntelliJ IDEA ke liye verbose logging: "Help" -> "Diagnostic Tools" -> "Debug Log Settings..." ya `idea.vmoptions` mein `-Didea.logging.level=DEBUG` add karein. Logs IntelliJ IDEA configuration directory ke "log" directory mein hain.

- Eclipse mein verbose output enable karne ke liye, `eclipse.ini` ko `-debug` ya `-consoleLog` ke saath modify karein. Detailed logging ke liye, Log4j ya java.util.logging configure karein. Log location logging configuration par depend karta hai.

- Maven se verbose output paane ke liye, `mvn -X <command>` use karein. Jaise ki, `mvn -X clean install`.

- WebSphere Liberty Server mein verbose logging enable karne ke liye, `server.xml` file ko configure karein taaki `<logging traceSpecification="*=info:com.ibm.ws.*=all:"/>` include ho sake. Aap `console.log` aur `messages.log` files ka bhi use kar sakte hain detailed logs ke liye.

- AWS CLI ke saath verbose output ke liye, `--debug` flag ka use karein: `aws <command> --debug`.

- `gcloud` se verbose output paane ke liye, `--verbosity` flag ka use karein: `gcloud <command> --verbosity=debug`.

- Gradle mein verbose output enable karne ke liye, `-v` ya `--verbose` flag ka use karein: `gradle <task> -v`. Zyada detailed logging ke liye, `--debug` ka use karein: `gradle <task> --debug`.

- Docker ke saath verbose output ke liye, `--verbose` flag ka use karein (agar specific command ke liye available hai) ya Docker daemon logs check karein. Aap Docker daemon logging level ko `daemon.json` file mein configure kar sakte hain.

- Terraform se verbose output paane ke liye, `TF_LOG` environment variable ko `DEBUG` ya `TRACE` set karein: `export TF_LOG=DEBUG` ya `export TF_LOG=TRACE`.

- Ansible ke saath verbose output enable karne ke liye, `-v`, `-vv`, `-vvv`, ya `-vvvv` flags ka use karein increasing verbosity ke liye: `ansible-playbook playbook.yml -vvv`.

- Kubernetes `kubectl` ke saath verbose output ke liye, `--v` flag ka use karein jo ki verbosity level ko indicate karta hai (jaise ki `--v=6` ya `--v=9`): `kubectl get pods --v=6`.

- Systemd se verbose output paane ke liye, `journalctl -b -x` use karein logs ke saath explanations ke saath dekhe ya `systemctl --full --all status <service>` use karein.