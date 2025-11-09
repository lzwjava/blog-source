---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ESP32 CAMコンパクト開発ボード概要
translated: true
type: note
---

### ESP32-CAMとは？

ESP32-CAMは、Espressif Systemsが提供するコンパクトで低コストの開発ボードで、高性能なESP32マイクロコントローラと統合カメラモジュールを組み合わせたものです。IoT（モノのインターネット）プロジェクト、特に画像キャプチャ、ビデオストリーミング、コンピュータビジョンに関連するプロジェクト向けに設計されています。「CAM」の部分は、2MP解像度（1600x1200ピクセル）をサポートする内蔵のOV2640カメラセンサーを指します。

#### 主な特徴：
- **プロセッサと接続性**：デュアルコアのESP32チップ（Xtensa LX6アーキテクチャ、最大240 MHz）を搭載し、520KBのSRAMと4MBのPSRAMを備えています。ワイヤレス通信のためにWi-Fi（802.11 b/g/n）とデュアルモードBluetooth（クラシックとBLE）を含みます。
- **カメラ**：焦点調整可能なレンズを備えたOV2640 CMOSイメージセンサーで、JPEG、BMP、グレースケールなどのフォーマットをサポートします。
- **電源とサイズ**：3.3V（またはレギュレータ経由で5V）で動作し、低電力消費（キャプチャ時200mA未満）で、サイズはわずか27x40.5x4.5mmです。これにより、組み込みプロジェクトに理想的です。
- **I/O**：10本のGPIOピン（一部はカメラと共有）、ストレージ用のmicroSDカードスロット、拡張によるセンサーのサポート。
- **プログラミング**：Arduino IDE、ESP-IDF、またはMicroPythonと互換性があります。esp32-camera（GitHub）のようなライブラリが画像処理とストリーミングを処理します。

#### 一般的な用途：
- **DIYセキュリティカメラ**：Wi-Fi経由でスマートフォンやブラウザにライブビデオをストリーミングし、モーション検出を備えます。
- **画像認識**：TensorFlow LiteなどのAIツールと統合して物体検出を行います。
- **監視とモニタリング**：リモート写真キャプチャ、タイムラプス、または野生生物カメラ。
- **プロトタイピング**：ロボティクス、スマートホームデバイス、または拡張現実実験。

その手頃な価格（多くの場合10ドル未満）と簡単なセットアップにより、メイカーの間で人気があります。ただし、初心者は初期プログラミング用にUSB-to-シリアルアダプタが必要な場合があります。より高品質のビデオには、ESP32-S3-CAMのような新しいバリアントが存在しますが、オリジナルのESP32-CAMはシンプルなプロジェクトの定番として残っています。

#### 参考文献：
- [ESP32-CAM Camera Module on Amazon](https://www.amazon.com/HiLetgo-ESP32-CAM-Development-Bluetooth-Raspberry/dp/B07RXPHYNM)
- [Espressif ESP32-Camera GitHub Repo](https://github.com/espressif/esp32-camera)
- [M5Stack ESP32-CAM Docs](https://docs.m5stack.com/en/unit/esp32cam)
- [Instructables: Super Cheap Security Camera with ESP32-CAM](https://www.instructables.com/Super-Cheap-Security-Camera-With-ESP32-cam/)
- [DFRobot ESP32-CAM Datasheet (PDF)](https://media.digikey.com/pdf/Data%2520Sheets/DFRobot%2520PDFs/DFR0602_Web.pdf)