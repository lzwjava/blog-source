---
audio: false
generated: true
image: false
lang: ja
layout: post
title: macOSとLinuxにおけるネットワークサービス
translated: true
type: note
---

### macOSとLinuxにおけるネットワークサービスと関連用語

これらの用語は主にネットワークサービス名を指しており、多くの場合macOSとLinuxシステムの両方で`/etc/services`ファイルに定義されています。このファイルは、標準的なネットワークサービスのサービス名をポート番号とプロトコルにマッピングします。一部は公式のIANA登録サービスであり、他はシステム設定で一般的に使用されるエイリアスやプロトコル名です。以下は、macOS（BSDライクなベースを使用）とLinuxディストリビューションにおける標準的な使用法に基づく各用語の説明です。

- **service**: これはmacOS（launchd経由）とLinux（systemdまたはinitシステム経由）の両方におけるシステムデーモンまたはプロセスの総称です。`/etc/services`内の特定のネットワークサービスではなく、LinuxではレガシーなSysV initスクリプトを管理するための「service」コマンドを指す場合があります。または、広義にあらゆるバックグラウンドサービスを指します。

- **ircu**: IRCU（Internet Relay Chat Undernet）サービスを指し、IRCサーバーソフトウェアの一種です。ポート6667/tcp（場合によってはudpも）を使用します。Linuxでは、ircuやundernet-ircuパッケージなどのIRCデーモンに関連付けられている可能性があります。macOSや最新のLinuxに標準でインストールされることは稀ですが、チャットサーバー用にportsやパッケージ経由で利用可能です。

- **complex-link**: おそらく「commplex-link」の誤記またはバリエーションであり、ポート5001/tcpに登録されたネットワークサービスです。通信多重化リンク（例：一部のネットワークツールやプロトコル内）に使用されます。macOSでは、このポートはAirPort/Time Capsuleの設定やルーター管理ユーティリティ（NetgearやAppleデバイスなど）に関連付けられています。Linuxでは、同様の目的でファイアウォールルールやnetstatの出力に表示されることがあります。

- **dhcpc**: DHCPクライアントサービスのエイリアスで、ポート68/udp（bootpcとしても知られる）を使用します。これはIPアドレスを動的に取得するためのDHCPのクライアント側です。Linuxではdhclientやdhcpcdなどのプロセスによって処理され、macOSではconfigdやbootpd（クライアントモード）によって処理されます。

- **zeroconf**: ゼロコンフィギュレーションネットワーキング（Zeroconf）を指し、手動設定なしで自動サービスディスカバリを実現するプロトコルです。macOSではBonjour（ポート5353/udpでmDNSを使用）として実装されています。Linuxでは通常Avahi（同様にポート5353/udp）です。プリンター、共有、その他のローカルネットワークサービスを発見するために使用されます。

- **ntp**: ネットワーク上でシステムクロックを同期させるためのNetwork Time Protocolサービスです。ポート123/udp（場合によってはtcpも）を使用します。Linuxではntpdやchronydによって処理され、macOSではntpdまたは組み込みの時刻同期デーモンによって処理されます。

- **http**: ウェブ通信の基盤であるHyperText Transfer Protocolです。ポート80/tcp（場合によってはudpも）を使用します。macOSとLinuxの両方で、Apache（httpd）やNginxなどのウェブサーバーに関連付けられています。

- **ssh**: 安全なリモートアクセスとファイル転送のためのSecure Shellプロトコルです。ポート22/tcp（およびudp/sctp）を使用します。LinuxとmacOSでは、デーモンはsshdであり、システム設定やsshd_configを介して有効化されます。

- **hgvirtgrp**: これは仮想化に関連するユーザーグループへの参照と思われ、Linuxの「libvirt group」（例：libvirtまたはlibvirt-qemuグループ）のバリエーションまたはタイポの可能性があります。Linuxでは、ユーザーをlibvirtグループに追加すると、libvirt経由（KVM/QEMU用）で仮想マシンを管理する権限が付与されます。macOSでは仮想化にHypervisorフレームワークを使用しますが、標準の「hgvirtgrp」グループは存在しません。QEMUやVirt-Managerなどのハイパーバイザー/仮想化ツール用のカスタムグループを指す可能性があります。特定のグループである場合は、システムの`/etc/group`を確認してください。

これらは、`netstat`、`lsof`、ファイアウォール設定（例：macOSのpf、Linuxのiptables/ufw）などのツールで一般的に見られます。正確な定義については、システムの`/etc/services`ファイルまたはIANAポートレジストリを参照してください。

**参考文献**  
[Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)  
[what is an open port with a commplex-link? - Apple Community](https://discussions.apple.com/thread/7747034)  
[Running virt-manager and libvirt on macOS](https://www.arthurkoziel.com/running-virt-manager-and-libvirt-on-macos/)