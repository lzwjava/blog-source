---
audio: false
generated: true
lang: hi
layout: post
title: मैकओएस पर गो कमांड नॉट फाउंड को ठीक करना
translated: true
type: note
---

त्रुटि संदेश `/bin/sh: go: command not found` इंगित करता है कि Go प्रोग्रामिंग भाषा आपके macOS सिस्टम पर इंस्टॉल नहीं है, या यह आपके PATH में ठीक से कॉन्फ़िगर नहीं है। `make` कमांड एक Go बिल्ड प्रक्रिया चलाने का प्रयास कर रहा है, जिसके लिए Go कंपाइलर (`go`) की आवश्यकता होती है। macOS पर Go इंस्टॉल करने और इस समस्या को हल करने के चरण नीचे दिए गए हैं।

### macOS पर Go इंस्टॉल करने के चरण

macOS पर Go इंस्टॉल करने के दो प्राथमिक तरीके हैं: आधिकारिक Go इंस्टॉलर का उपयोग करना या Homebrew का उपयोग करना। मैं दोनों विधियों को कवर करूंगा, लेकिन macOS उपयोगकर्ताओं के लिए Homebrew अक्सर सरल होता है। अपनी पसंद के आधार पर एक विधि चुनें।

#### पूर्वापेक्षाएँ
- सुनिश्चित करें कि आपका macOS संस्करण 10.10 या बाद का है ताकि हाल के Go संस्करणों के साथ संगतता बनी रहे।[](https://tecadmin.net/install-go-on-macos/)
- Go और सिस्टम फ़ाइलों को संशोधित करने के लिए आपको व्यवस्थापक पहुंच की आवश्यकता है।
- एक टर्मिनल एप्लिकेशन (Applications > Utilities > Terminal में मिलता है)।

#### विधि 1: Homebrew का उपयोग करके Go इंस्टॉल करें (अनुशंसित)
Homebrew macOS के लिए एक लोकप्रिय पैकेज मैनेजर है जो सॉफ़्टवेयर इंस्टॉलेशन को सरल बनाता है।

1.  **Homebrew इंस्टॉल करें (यदि पहले से इंस्टॉल नहीं है)**:
    - टर्मिनल खोलें और चलाएँ:
      ```bash
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      ```
    - इंस्टॉलेशन पूरा करने के लिए स्क्रीन पर दिए गए निर्देशों का पालन करें।[](https://www.digitalocean.com/community/tutorials/how-to-install-go-and-set-up-a-local-programming-environment-on-macos)

2.  **Go इंस्टॉल करें**:
    - Go का नवीनतम संस्करण इंस्टॉल करने के लिए निम्नलिखित कमांड चलाएँ:
      ```bash
      brew install go
      ```
    - यह Go को `/usr/local/Cellar/go` (या इसी तरह के पथ पर) इंस्टॉल करता है और Go बाइनरी को `/usr/local/bin` में जोड़ता है।[](https://www.feliciano.tech/blog/how-to-install-go-on-linux-macos/)[](https://formulae.brew.sh/formula/go)

3.  **इंस्टॉलेशन सत्यापित करें**:
    - इंस्टॉल किए गए Go संस्करण की जांच करने के लिए चलाएँ:
      ```bash
      go version
      ```
    - आपको `go version go1.23.x darwin/amd64` जैसा आउटपुट दिखाई देना चाहिए, जो Go के इंस्टॉल होने की पुष्टि करता है।[](https://tecadmin.net/install-go-on-macos/)

4.  **एनवायरनमेंट वेरिएबल सेट अप करें (यदि आवश्यक हो)**:
    - Homebrew आमतौर पर Go को आपके PATH में स्वचालित रूप से जोड़ देता है, लेकिन यदि `go` कमांड काम नहीं करते हैं, तो अपने शेल प्रोफाइल में Go बाइनरी पथ जोड़ें:
      - उपयुक्त शेल कॉन्फ़िगरेशन फ़ाइल खोलें या बनाएँ (उदाहरण के लिए, Zsh के लिए `~/.zshrc` जो कैटालिना के बाद से macOS पर डिफ़ॉल्ट है, या Bash के लिए `~/.bash_profile`):
        ```bash
        nano ~/.zshrc
        ```
      - निम्नलिखित पंक्तियाँ जोड़ें:
        ```bash
        export PATH=$PATH:/usr/local/go/bin
        ```
      - फ़ाइल सहेजें (nano में Ctrl+X, फिर Y, फिर Enter दबाएं) और परिवर्तन लागू करें:
        ```bash
        source ~/.zshrc
        ```
      - यदि आप कस्टम वर्कस्पेस का उपयोग करना चाहते हैं, तो `GOPATH` सेट करें (वैकल्पिक, क्योंकि Go मॉड्यूल अक्सर इसकी आवश्यकता को समाप्त कर देते हैं):
        ```bash
        export GOPATH=$HOME/go
        export PATH=$PATH:$GOPATH/bin
        ```
      - फ़ाइल को फिर से सोर्स करें:
        ```bash
        source ~/.zshrc
        ```

5.  **Go इंस्टॉलेशन का परीक्षण करें**:
    - यह सुनिश्चित करने के लिए फिर से `go version` चलाएँ कि कमांड पहचाना जाता है।
    - वैकल्पिक रूप से, यह पुष्टि करने के लिए कि सब कुछ काम कर रहा है, एक साधारण Go प्रोग्राम बनाएँ:
      ```bash
      mkdir -p ~/go/src/hello
      nano ~/go/src/hello/main.go
      ```
      - निम्नलिखित कोड जोड़ें:
        ```go
        package main
        import "fmt"
        func main() {
            fmt.Println("Hello, World!")
        }
        ```
      - सेव करें और बाहर निकलें (Ctrl+X, Y, Enter), फिर कंपाइल और रन करें:
        ```bash
        cd ~/go/src/hello
        go run main.go
        ```
      - आपको आउटपुट के रूप में `Hello, World!` दिखाई देना चाहिए।[](https://www.digitalocean.com/community/tutorials/how-to-install-go-and-set-up-a-local-programming-environment-on-macos)

#### विधि 2: आधिकारिक इंस्टॉलर का उपयोग करके Go इंस्टॉल करें
यदि आप Homebrew का उपयोग नहीं करना चाहते हैं, तो आप आधिकारिक macOS पैकेज का उपयोग करके Go इंस्टॉल कर सकते हैं।

1.  **Go इंस्टॉलर डाउनलोड करें**:
    - आधिकारिक Go डाउनलोड पेज पर जाएँ: https://go.dev/dl/
    - अपने सिस्टम आर्किटेक्चर के लिए macOS पैकेज (`.pkg`) डाउनलोड करें (उदाहरण के लिए, इंटेल Mac के लिए `go1.23.x.darwin-amd64.pkg` या Apple Silicon के लिए `go1.23.x.darwin-arm64.pkg`)।[](https://medium.com/%40priyamjpatel/installing-go-on-a-mac-machine-bca6746fff0b)[](https://golangdocs.com/install-go-mac-os)

2.  **इंस्टॉलर चलाएँ**:
    - फाइंडर में डाउनलोड किए गए `.pkg` फ़ाइल पर डबल-क्लिक करें।
    - Go इंस्टॉल करने के लिए स्क्रीन पर दिए गए निर्देशों का पालन करें। यह डिफ़ॉल्ट रूप से `/usr/local/go` पर इंस्टॉल हो जाएगा।
    - आपको अपना व्यवस्थापक पासवर्ड दर्ज करने की आवश्यकता हो सकती है।[](https://www.scaler.com/topics/golang/install-golang/)[](https://golangdocs.com/install-go-mac-os)

3.  **एनवायरनमेंट वेरिएबल सेट अप करें**:
    - टर्मिनल खोलें और अपनी शेल कॉन्फ़िगरेशन फ़ाइल (जैसे `~/.zshrc` या `~/.bash_profile`) संपादित करें:
      ```bash
      nano ~/.zshrc
      ```
    - निम्नलिखित पंक्तियाँ जोड़ें:
      ```bash
      export GOROOT=/usr/local/go
      export GOPATH=$HOME/go
      export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
      ```
    - सेव करें और परिवर्तन लागू करें:
      ```bash
      source ~/.zshrc
      ```
    - नोट: `GOROOT` वैकल्पिक है जब तक कि आप Go का विकास नहीं कर रहे हैं या आपको गैर-मानक इंस्टॉलेशन पथ की आवश्यकता नहीं है। आधुनिक Go संस्करणों में अक्सर `GOROOT` सेट करने की आवश्यकता नहीं होती है।[](https://stackoverflow.com/questions/12843063/install-go-with-brew-and-running-the-gotour)[](https://tecadmin.net/install-go-on-macos/)

4.  **इंस्टॉलेशन सत्यापित करें**:
    - चलाएँ:
      ```bash
      go version
      ```
    - आपको इंस्टॉल किया गया Go संस्करण (जैसे `go version go1.23.x darwin/amd64`) दिखाई देना चाहिए।[](https://golangdocs.com/install-go-mac-os)

5.  **Go इंस्टॉलेशन का परीक्षण करें**:
    - "Hello, World!" प्रोग्राम बनाने और चलाने के लिए विधि 1, चरण 5 के समान चरणों का पालन करें।

#### मूल समस्या का समाधान
Go इंस्टॉल करने के बाद, अपने `clash-core` डायरेक्टरी में वापस नेविगेट करें और `make` कमांड फिर से आज़माएँ:
```bash
cd /path/to/clash-core
make
```

यदि आपको कोई समस्या आती है:
- **प्रॉक्सी सेटिंग्स**: आपका टर्मिनल आउटपुट दिखाता है कि `HTTP_PROXY` और `HTTPS_PROXY` `http://127.0.0.1:7890` पर सेट हैं। सुनिश्चित करें कि आपका प्रॉक्सी सक्रिय है और Go की नेटवर्क पहुंच (जैसे डिपेंडेंसी डाउनलोड करना) में हस्तक्षेप नहीं कर रहा है। आप परीक्षण करने के लिए प्रॉक्सी को अस्थायी रूप से अक्षम कर सकते हैं:
  ```bash
  unset HTTP_PROXY HTTPS_PROXY
  make
  ```
- **अनुमतियाँ**: यदि आपको अनुमति त्रुटियाँ मिलती हैं, तो सुनिश्चित करें कि आपके पास प्रोजेक्ट डायरेक्टरी और Go वर्कस्पेस (`$GOPATH` या `$HOME/go`) तक लिखने की पहुंच है।
- **Go मॉड्यूल**: `clash-core` प्रोजेक्ट संभवतः Go मॉड्यूल का उपयोग करता है। सुनिश्चित करें कि आप सही डायरेक्टरी में हैं जिसमें `go.mod` है, और `make` से पहले डिपेंडेंसी प्राप्त करने के लिए `go mod tidy` चलाएँ:
  ```bash
  go mod tidy
  make
  ```
- **आर्किटेक्चर मिसमैच**: `make` कमांड `linux-amd64` (`GOOS=linux GOARCH=amd64`) के लिए बिल्ड कर रहा है। यदि आप macOS पर बाइनरी चलाना चाहते हैं, तो आपको Makefile या बिल्ड कमांड को `darwin-amd64` (इंटेल Mac के लिए) या `darwin-arm64` (Apple Silicon के लिए) को लक्षित करने के लिए संशोधित करने की आवश्यकता हो सकती है। Makefile में `linux-amd64` टार्गेट की जांच करें और इसे समायोजित करें, या चलाएँ:
  ```bash
  GOARCH=amd64 GOOS=darwin CGO_ENABLED=0 go build -trimpath -ldflags '-X "github.com/Dreamacro/clash/constant.Version=1.18" -X "github.com/Dreamacro/clash/constant.BuildTime=Sat Jun 28 12:24:27 UTC 2025" -w -s -buildid=' -o bin/clash-darwin-amd64
  ```
  यदि आप Apple Silicon पर हैं तो `amd64` को `arm64` से बदलें।

#### अतिरिक्त नोट्स
- **पिछले Go संस्करणों को अनइंस्टॉल करना**: यदि Go पहले इंस्टॉल था, तो संघर्षों से बचने के लिए इसे हटा दें:
  ```bash
  sudo rm -rf /usr/local/go
  sudo rm -f /etc/paths.d/go
  ```
  फिर ऊपर दी गई किसी एक विधि का उपयोग करके पुनः इंस्टॉल करें।[](https://hostman.com/tutorials/how-to-install-go-on-macos/)[](https://go.dev/doc/install)
- **Go वर्कस्पेस**: यदि आपने `GOPATH` सेट किया है, तो डायरेक्टरी बनाएँ:
  ```bash
  mkdir -p $HOME/go/{bin,src,pkg}
  ```
  हालाँकि, Go मॉड्यूल (अधिकांश आधुनिक प्रोजेक्ट्स जैसे `clash-core` द्वारा उपयोग किए जाते हैं) के साथ, `GOPATH` कम महत्वपूर्ण है।[](https://www.geeksforgeeks.org/how-to-install-golang-on-macos/)
- **Xcode कमांड लाइन टूल्स**: कुछ Go प्रोजेक्ट्स को C डिपेंडेंसी (जैसे `CGO_ENABLED=1`) की आवश्यकता होती है। यदि आवश्यक हो तो Xcode कमांड लाइन टूल्स इंस्टॉल करें:
  ```bash
  xcode-select --install
  ```
  [](https://www.digitalocean.com/community/tutorials/how-to-install-go-and-set-up-a-local-programming-environment-on-macos)
- **एकाधिक Go संस्करण**: यदि आपको एकाधिक Go संस्करणों की आवश्यकता है, तो एक वर्जन मैनेजर जैसे `gvm` (Homebrew या स्क्रिप्ट के माध्यम से इंस्टॉल करें) का उपयोग करने पर विचार करें।[](https://jimkang.medium.com/install-go-on-mac-with-homebrew-5fa421fc55f5)

#### सत्यापन
एक बार Go इंस्टॉल हो जाने और `make` कमांड सफल हो जाने के बाद, `clash-core` बाइनरी `bin/` डायरेक्टरी (जैसे `bin/clash-linux-amd64` या `bin/clash-darwin-amd64`) में दिखाई देनी चाहिए। यह सत्यापित करें कि यह काम करती है:
```bash
./bin/clash-darwin-amd64 --version
```

यदि आपको और सहायता की आवश्यकता है या कोई विशिष्ट त्रुटि आती है, तो मुझे सटीक त्रुटि संदेश या संदर्भ बताएं, और मैं अधिक लक्षित सहायता प्रदान कर सकता हूं!