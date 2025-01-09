---                            
layout: post
title: "Turbolist3r: सबडोमेन्स की गणना"
---

## Turbolist3r

[GitHub पर Turbolist3r](https://github.com/fleetcaptain/Turbolist3r)

[अहमद अबौल-एला - @aboul3la](https://github.com/aboul3la) द्वारा [Sublist3r](https://github.com/aboul3la/Sublist3r) पर आधारित  
कार्ल पियर्सन द्वारा फोर्क किया गया - [GitHub](https://github.com/fleetcaptain)

```bash
python turbolist3r.py -d google.com
```

(यह एक कमांड है जिसे टर्मिनल में चलाया जाता है। इसे हिंदी में अनुवाद करने की आवश्यकता नहीं है।)

## Sublist3r

कोशिश की। https://github.com/aboul3la/Sublist3r

```bash
% python  sublist3r.py -d google.com
🚀 **प्रॉक्सी सेटिंग्स का पता चला:**
   - HTTP_PROXY: http://127.0.0.1:7890
   - HTTPS_PROXY: http://127.0.0.1:7890
```

```
                 ____        _     _ _     _   _____
                / ___| _   _| |__ | (_)___| |_|___ / _ __
                \___ \| | | | '_ \| | / __| __| |_ \| '__|
                 ___) | |_| | |_) | | \__ \ |_ ___) | |
                |____/ \__,_|_.__/|_|_|___/\__|____/|_|
```

# कोडेड बाय अहमेद अबौल-एला - @aboul3la

[-] google.com के लिए अब सबडोमेन की गणना की जा रही है
[-] अब Baidu में खोज की जा रही है..
[-] अब Yahoo में खोज की जा रही है..
[-] अब Google में खोज की जा रही है..
[-] अब Bing में खोज की जा रही है..
[-] अब Ask में खोज की जा रही है..
[-] अब Netcraft में खोज की जा रही है..
[-] अब DNSdumpster में खोज की जा रही है..
[-] अब Virustotal में खोज की जा रही है..
[-] अब ThreatCrowd में खोज की जा रही है..
[-] अब SSL Certificates में खोज की जा रही है..
[-] अब PassiveDNS में खोज की जा रही है..
प्रक्रिया DNSdumpster-8:
ट्रेसबैक (सबसे हालिया कॉल अंतिम):
  फ़ाइल "/Users/lzwjava/anaconda3/lib/python3.10/multiprocessing/process.py", लाइन 314, में _bootstrap
    self.run()
  फ़ाइल "/Users/lzwjava/projects/Sublist3r/sublist3r.py", लाइन 268, में run
    domain_list = self.enumerate()
  फ़ाइल "/Users/lzwjava/projects/Sublist3r/sublist3r.py", लाइन 647, में enumerate
    token = self.get_csrftoken(resp)
  फ़ाइल "/Users/lzwjava/projects/Sublist3r/sublist3r.py", लाइन 641, में get_csrftoken
    token = csrf_regex.findall(resp)[0]
IndexError: सूची सीमा से बाहर
[!] त्रुटि: Virustotal संभवतः अब हमारे अनुरोधों को ब्लॉक कर रहा है
[-] कुल अद्वितीय सबडोमेन मिले: 97
www.google.com
accounts.google.com
freezone.accounts.google.com
adwords.google.com
qa.adz.google.com
answers.google.com
apps-secure-data-connector.google.com
audioads.google.com
checkout.google.com
mtv-da-1.ad.corp.google.com
ads-compare.eem.corp.google.com
da.ext.corp.google.com
m.guts.corp.google.com
m.gutsdev.corp.google.com
login.corp.google.com
mtv-da.corp.google.com
mygeist.corp.google.com
mygeist2010.corp.google.com
proxyconfig.corp.google.com
reseed.corp.google.com
twdsalesgsa.twd.corp.google.com
uberproxy.corp.google.com
uberproxy-nocert.corp.google.com
uberproxy-san.corp.google.com
ext.google.com
cag.ext.google.com
cod.ext.google.com
da.ext.google.com
eggroll.ext.google.com
fra-da.ext.google.com
glass.ext.google.com
glass-eur.ext.google.com
glass-mtv.ext.google.com
glass-twd.ext.google.com
hot-da.ext.google.com
hyd-da.ext.google.com
ice.ext.google.com
meeting.ext.google.com
mtv-da.ext.google.com
soaproxyprod01.ext.google.com
soaproxytest01.ext.google.com
spdy-proxy.ext.google.com
spdy-proxy-debug.ext.google.com
twd-da.ext.google.com
flexpack.google.com
www.flexpack.google.com
accounts.flexpack.google.com
gaiastaging.flexpack.google.com
mail.flexpack.google.com
plus.flexpack.google.com
search.flexpack.google.com
freezone.google.com
www.freezone.google.com
accounts.freezone.google.com
gaiastaging.freezone.google.com
mail.freezone.google.com
news.freezone.google.com
plus.freezone.google.com
search.freezone.google.com
gmail.google.com
hosted-id.google.com
jmt0.google.com
aspmx.l.google.com
alt1.aspmx.l.google.com
alt2.aspmx.l.google.com
alt3.aspmx.l.google.com
alt4.aspmx.l.google.com
gmail-smtp-in.l.google.com
alt1.gmail-smtp-in.l.google.com
alt2.gmail-smtp-in.l.google.com
alt3.gmail-smtp-in.l.google.com
alt4.gmail-smtp-in.l.google.com
gmr-smtp-in.l.google.com
alt1.gmr-smtp-in.l.google.com
alt2.gmr-smtp-in.l.google.com
alt3.gmr-smtp-in.l.google.com
alt4.gmr-smtp-in.l.google.com
vp.video.l.google.com
m.google.com
freezone.m.google.com
mail.google.com
freezone.mail.google.com
misc.google.com
misc-sni.google.com
mtalk.google.com
mx.google.com
ics.prod.google.com
sandbox.google.com
cert-test.sandbox.google.com
ecc-test.sandbox.google.com
services.google.com
talk.google.com
upload.google.com
dg.video.google.com
upload.video.google.com
wifi.google.com
onex.wifi.google.com
```

