---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: पैरामिको एसएसएच और एसएफ़टीपी गाइड
translated: true
type: note
---

### इंस्टॉलेशन
Paramiko SSH और SFTP के लिए एक Python लाइब्रेरी है। इसे pip के माध्यम से इंस्टॉल करें:

```bash
pip install paramiko
```

### बेसिक उपयोग
Paramiko आपको SSH सर्वर से कनेक्ट करने, कमांड चलाने और फाइलें ट्रांसफर करने की अनुमति देता है। प्राइवेट कीज़ को हमेशा सुरक्षित रूप से हैंडल करें और मजबूत पासवर्ड का उपयोग करें—Paramiko की-आधारित और पासवर्ड ऑथेंटिकेशन दोनों का समर्थन करता है।

मुख्य अवधारणाएँ:
- **क्लाइंट**: कनेक्शन सेट अप करने के लिए `paramiko.SSHClient()` का उपयोग करें।
- **ट्रांसपोर्ट**: लोअर-लेवल कंट्रोल के लिए `paramiko.Transport()` का उपयोग करें।
- `client.connect()` के माध्यम से होस्टनाम, यूज़रनेम और या तो पासवर्ड या की (उदाहरण के लिए, `paramiko.RSAKey.from_private_key_file()` के माध्यम से) का उपयोग करके ऑथेंटिकेट करें।

### उदाहरण: कनेक्ट करना और एक कमांड चलाना
यहाँ एक SSH सर्वर से कनेक्ट करने, एक कमांड चलाने और आउटपुट प्रिंट करने के लिए एक संपूर्ण स्क्रिप्ट है। प्लेसहोल्डर्स को अपने विवरण से बदलें।

```python
import paramiko

# SSH क्लाइंट बनाएँ
client = paramiko.SSHClient()

# ऑटो-एड होस्ट की (प्रोडक्शन में सावधान रहें; इसके बजाय known_hosts लोड करें)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # कनेक्ट करें (पासवर्ड या की फाइल का उपयोग करें)
    client.connect(
        hostname='your.server.com',
        port=22,  # डिफॉल्ट SSH पोर्ट
        username='your_username',
        password='your_password',  # या key_filename='path/to/private_key.pem'
    )

    # एक कमांड चलाएँ
    stdin, stdout, stderr = client.exec_command('echo "Hello from SSH!"')

    # आउटपुट पढ़ें
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    print("Output:", output)
    print("Error:", error)

except paramiko.SSHException as e:
    print(f"SSH error: {e}")
finally:
    client.close()
```

### एडवांस्ड उदाहरण: की-आधारित ऑथेंटिकेशन और फाइल ट्रांसफर का उपयोग
की ऑथ के लिए, यदि आवश्यक हो तो एक की पेयर जनरेट करें (उदाहरण के लिए, `ssh-keygen`), सर्वर पर पब्लिक की को `~/.ssh/authorized_keys` में एड करें, फिर इसका उपयोग करें:

```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # की-आधारित कनेक्ट
    client.connect(
        hostname='your.server.com',
        username='your_username',
        key_filename='~/.ssh/id_rsa',  # प्राइवेट की का पथ
    )

    # कमांड चलाएँ
    stdin, stdout, stderr = client.exec_command('ls -la')
    print(stdout.read().decode('utf-8'))

    # SFTP उदाहरण: फाइल ट्रांसफर
    sftp = client.open_sftp()
    sftp.put('local_file.txt', 'remote_file.txt')  # अपलोड
    sftp.get('remote_file.txt', 'local_copy.txt')  # डाउनलोड
    sftp.close()

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
```

### टिप्स और बेस्ट प्रैक्टिसेज़
- **सुरक्षा**: पासवर्ड पर की-आधारित ऑथ को प्राथमिकता दें। प्रोडक्शन में `AutoAddPolicy` को डिसेबल करें और `client.load_host_keys()` के माध्यम से होस्ट कीज़ को वेरिफाई करें।
- **एरर हैंडलिंग**: हमेशा `paramiko.SSHException` को कैच करें और `exit_status = stdout.channel.recv_exit_status()` के साथ एक्ज़िट कोड चेक करें।
- **थ्रेड्स**: Paramiko डिफ़ॉल्ट रूप से थ्रेड-सेफ नहीं है; यदि आवश्यक हो तो लॉक्स का उपयोग करें।
- **डॉक्यूमेंटेशन**: अधिक जानकारी के लिए, [आधिकारिक Paramiko डॉक्स](https://docs.paramiko.org/) देखें। OpenSSH के `sshd` या लोकल VMs जैसे टूल्स के साथ टेस्ट करें।

यह आपको शुरुआत करने में मदद करेगा; अपनी आवश्यकताओं के अनुसार एडाप्ट करें!