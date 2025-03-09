---
audio: true
generated: false
lang: ar
layout: post
title: توضيح
translated: true
---

- لتفعيل الإخراج التفصيلي في Homebrew، استخدم `export HOMEBREW_CURL_VERBOSE=1` مع `brew upgrade --verbose`.

- لتزيد من التفصيل في SSH، استخدم `ssh -vvv user@host`.

- للحصول على إخراج أكثر تفصيلاً مع `git`، استخدم `git -v` أو `git --verbose`.

- للحصول على مزيد من الإخراج من `rsync`، استخدم `rsync -vv source destination`.

- كتابة ملف التكوين التفصيلي في SSH، مثل `LogLevel VERBOSE` في `.ssh/config`.

- لتفعيل الإخراج التفصيلي مع `npm`، استخدم `npm install --verbose` أو `npm run <script> --verbose`.

- للحصول على تسجيل تفصيلي في Node.js، استخدم المتغير البيئي `NODE_DEBUG`: `NODE_DEBUG=http,net node your_script.js`.

- للحصول على إخراج تفصيلي من `curl`، استخدم `curl -v <url>`.

- لتفعيل الإخراج التفصيلي مع `pip`، استخدم `pip install -v <package>` أو `pip install --verbose <package>`.

- للحصول على إخراج تفصيلي مع `wget`، استخدم `wget --verbose <url>`.

- للحصول على إخراج تفصيلي من `yum`، استخدم `yum -v install <package>`.

- لتفعيل الإخراج التفصيلي مع `apt-get`، استخدم `apt-get -o Debug::pkgProblemResolver=yes install <package>`.

- للحصول على تسجيل تفصيلي مع `adb`، استخدم `adb logcat -v verbose`.

- لتشغيل Python في وضع التفصيل، استخدم `python -v your_script.py`.

- لتجميع كود Java مع إخراج تفصيلي، استخدم `javac -verbose YourClass.java`.

- لتشغيل VSCode في وضع التفصيل: `code --verbose`. للحصول على تسجيل، قم بتحديد `"trace": true` في `settings.json` وعرض السجلات من خلال "Developer: Open View..." -> "Log (Window)" أو "Log (Extension Host)".

- للحصول على تسجيل تفصيلي في IntelliJ IDEA: "Help" -> "Diagnostic Tools" -> "Debug Log Settings..." أو أضف `-Didea.logging.level=DEBUG` إلى `idea.vmoptions`. السجلات في مجلد "log" تحت دليل التكوين لـ IntelliJ IDEA.

- لتفعيل الإخراج التفصيلي في Eclipse، قم بتعديل `eclipse.ini` مع `-debug` أو `-consoleLog`. للحصول على تسجيل تفصيلي، قم بتكوين Log4j أو java.util.logging. موقع السجلات يعتمد على تكوين السجلات.

- للحصول على إخراج تفصيلي من Maven، استخدم `mvn -X <command>`. على سبيل المثال، `mvn -X clean install`.

- لتفعيل تسجيل تفصيلي في WebSphere Liberty Server، قم بتكوين ملف `server.xml` ليشمل `<logging traceSpecification="*=info:com.ibm.ws.*=all:"/>`. يمكنك أيضًا استخدام ملفات `console.log` و `messages.log` للحصول على سجلات تفصيلي.

- للحصول على إخراج تفصيلي مع AWS CLI، استخدم علم `--debug`: `aws <command> --debug`.

- للحصول على إخراج تفصيلي من `gcloud`، استخدم علم `--verbosity`: `gcloud <command> --verbosity=debug`.

- لتفعيل الإخراج التفصيلي في Gradle، استخدم علم `-v` أو `--verbose`: `gradle <task> -v`. للحصول على تسجيل تفصيلي أكثر، استخدم `--debug`: `gradle <task> --debug`.

- للحصول على إخراج تفصيلي مع Docker، استخدم علم `--verbose` (إذا كان متاحاً للامر الخاص) أو تحقق من سجلات ديمون Docker. يمكنك تهيئة مستوى تسجيل ديمون Docker في ملف `daemon.json`.

- للحصول على إخراج تفصيلي من Terraform، قم بتحديد المتغير البيئي `TF_LOG` إلى `DEBUG` أو `TRACE`: `export TF_LOG=DEBUG` أو `export TF_LOG=TRACE`.

- لتفعيل الإخراج التفصيلي مع Ansible، استخدم أعلام `-v`, `-vv`, `-vvv`, أو `-vvvv` لتزيد من التفصيل: `ansible-playbook playbook.yml -vvv`.

- للحصول على إخراج تفصيلي مع Kubernetes `kubectl`، استخدم علم `--v` متبوعاً برقم يشير إلى مستوى التفصيل (على سبيل المثال، `--v=6` أو `--v=9`): `kubectl get pods --v=6`.

- للحصول على إخراج تفصيلي من systemd، استخدم `journalctl -b -x` لعرض السجلات مع شرح أو `systemctl --full --all status <service>`.