---
audio: false
generated: true
lang: ja
layout: post
title: キルヒホッフの法則とArduino
translated: true
type: note
---

Arduinoを使用してキルヒホッフの法則―具体的にはキルヒホッフの電流法則（KCL）とキルヒホッフの電圧法則（KVL）―を検証するのは、電子工学の理論と実践的な実験を結びつける優れた方法です。KCLは接合点に流入する電流の総和が流出する電流の総和に等しいことを述べ、KVLは閉回路における電圧降下の和が供給電圧に等しいことを述べています。ここでは、シンプルな回路を設計し、Arduinoを使用して電流と電圧を測定し、これらの法則を確認する方法を紹介します。

Arduinoは電流を直接測定できないため、抵抗両端の電圧を測定することで（オームの法則: \\( I = V/R \\) を使用）電流を推定します。また、アナログピン（0〜5V範囲）を使用して電圧を測定できます。以下に、KCL用とKVL用の2つの実験を、ステップバイステップの手順、配線、コードとともに概説します。

---

### **実験 1: キルヒホッフの電流法則 (KCL) の検証**

#### **目的**
接合点に流入する電流と流出する電流が等しいことを実証する。

#### **回路設定**
- **使用部品:**
  - Arduino (例: Uno)
  - 抵抗 3本 (例: R1 = 330Ω, R2 = 470Ω, R3 = 680Ω)
  - ブレッドボードとジャンパワイヤ
  - 5V電源 (Arduinoの5Vピン)
- **配線:**
  - Arduinoの5VをノードAに接続する。
  - ノードAから、R1をGNDに接続する（分岐1）。
  - ノードAから、R2をGNDに接続する（分岐2、R1と並列）。
  - ノードAから、R3をGNDに接続する（分岐3、R1、R2と並列）。
  - Arduinoのアナログピンを使用して各抵抗両端の電圧を測定する:
    - A0をR1両端（片方をノードA、もう片方をGNDに接続）。
    - A1をR2両端。
    - A2をR3両端。
- **注意:** GNDは共通の基準点です。

#### **理論**
- 5VからノードAへの総電流 (\\( I_{in} \\)) は、R1, R2, R3を流れる \\( I_1 \\), \\( I_2 \\), \\( I_3 \\) に分流する。
- KCL: \\( I_{in} = I_1 + I_2 + I_3 \\)。
- 各抵抗両端の電圧を測定し、電流を計算: \\( I = V/R \\)。

#### **Arduino コード**
```cpp
void setup() {
  Serial.begin(9600); // シリアル通信を開始
}

void loop() {
  // 電圧を読み取る (0-1023 は 0-5V にマッピング)
  int sensorValue1 = analogRead(A0); // R1両端の電圧
  int sensorValue2 = analogRead(A1); // R2両端の電圧
  int sensorValue3 = analogRead(A2); // R3両端の電圧

  // 電圧に変換 (基準電圧5V, 10ビットADC)
  float V1 = sensorValue1 * (5.0 / 1023.0);
  float V2 = sensorValue2 * (5.0 / 1023.0);
  float V3 = sensorValue3 * (5.0 / 1023.0);

  // 抵抗値 (オーム)
  float R1 = 330.0;
  float R2 = 470.0;
  float R3 = 680.0;

  // 電流を計算 (I = V/R)
  float I1 = V1 / R1;
  float I2 = V2 / R2;
  float I3 = V3 / R3;

  // ノードに流入する総電流 (供給電圧 = 5V と仮定)
  float totalResistance = 1.0 / ((1.0/R1) + (1.0/R2) + (1.0/R3)); // 並列合成抵抗
  float Iin = 5.0 / totalResistance;

  // 結果を出力
  Serial.print("I1 (mA): "); Serial.println(I1 * 1000);
  Serial.print("I2 (mA): "); Serial.println(I2 * 1000);
  Serial.print("I3 (mA): "); Serial.println(I3 * 1000);
  Serial.print("Iin (mA): "); Serial.println(Iin * 1000);
  Serial.print("I1+I2+I3の和 (mA): "); Serial.println((I1 + I2 + I3) * 1000);
  Serial.println("---");

  delay(2000); // 2秒待機
}
```

#### **検証**
- シリアルモニタを開く (Arduino IDEで Ctrl+Shift+M, ボーレート 9600 に設定)。
- \\( I_{in} \\) (総抵抗から計算) と \\( I_1 + I_2 + I_3 \\) を比較する。これらはほぼ等しく、KCLが検証される。
- 抵抗器の許容誤差やArduinoのADC精度により、小さな不一致が生じる可能性がある。

---

### **実験 2: キルヒホッフの電圧法則 (KVL) の検証**

#### **目的**
閉回路における電圧降下の和が供給電圧に等しいことを示す。

#### **回路設定**
- **使用部品:**
  - Arduino
  - 抵抗 2本 (例: R1 = 330Ω, R2 = 470Ω)
  - ブレッドボードとジャンパワイヤ
  - 5V電源 (Arduinoの5Vピン)
- **配線:**
  - 5VをR1に接続する。
  - R1をR2に接続する。
  - R2をGNDに接続する。
  - 電圧を測定する:
    - A0を回路全体（5VからGND）にかけて供給電圧を確認。
    - A1をR1両端（5VからR1とR2の接合点まで）。
    - A2をR2両端（接合点からGNDまで）。
- **注意:** 電圧分割回路の設定を使用する。電圧が5V(Arduinoの限界)を超えないようにする。

#### **理論**
- KVL: \\( V_{source} = V_{R1} + V_{R2} \\)。
- 各電圧降下を測定し、それらの和が供給電圧(5V)と等しいか確認する。

#### **Arduino コード**
```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  // 電圧を読み取る
  int sensorValueSource = analogRead(A0); // 5VからGND間
  int sensorValueR1 = analogRead(A1);     // R1両端
  int sensorValueR2 = analogRead(A2);     // R2両端

  // 電圧に変換
  float Vsource = sensorValueSource * (5.0 / 1023.0);
  float VR1 = sensorValueR1 * (5.0 / 1023.0);
  float VR2 = sensorValueR2 * (5.0 / 1023.0);

  // 結果を出力
  Serial.print("供給電圧 Vsource (V): "); Serial.println(Vsource);
  Serial.print("VR1 (V): "); Serial.println(VR1);
  Serial.print("VR2 (V): "); Serial.println(VR2);
  Serial.print("VR1 + VR2 (V): "); Serial.println(VR1 + VR2);
  Serial.println("---");

  delay(2000);
}
```

#### **検証**
- シリアルモニタで、\\( V_{source} \approx V_{R1} + V_{R2} \\) であることを確認する。
- R1 = 330Ω と R2 = 470Ω が直列の場合、\\( V_{R1} \approx 2.1V \\)、\\( V_{R2} \approx 2.9V \\) と予想される（電圧分割則: \\( V_{R1} = 5 \cdot \frac{R1}{R1+R2} \\) に基づく）。合計は約5Vになる。

---

### **ヒントと注意点**
- **精度:** Arduinoの10ビットADC (0–1023) の分解能は約4.9mVであるため、微小な誤差が生じる。必要に応じてマルチメータでクロスチェックする。
- **安全性:** Arduinoを損傷しないように、電圧は5V未満、電流は低く保つ。
- **拡張:** より複雑な回路では、抵抗を追加するか、外部センサ（例: INA219による直接電流測定）を使用する。
- **デバッグ:** 結果が一致しない場合は、抵抗値、接続、GNDの一貫性を確認する。

これらの実験は実際の条件を単純化していますが、キルヒホッフの法則を効果的に実証します。これらの設定を調整したり、配線やコードなどの特定の部分で助けが必要ですか？お知らせください！