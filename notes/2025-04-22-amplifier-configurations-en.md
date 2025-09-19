---
title: Amplifier Configurations
lang: en
layout: post
audio: false
translated: false
generated: true
---

Here’s a comprehensive explanation of the **three basic amplifier configurations**—**Common Emitter (CE)**, **Common Collector (CC)** (also known as **Emitter Follower**), and **Common Base (CB)**—focusing on their structure, signal characteristics, advantages, disadvantages, and typical applications.

---

## 🔷 1. Common Emitter (CE) Amplifier

### 🔧 Configuration
- **Input**: Applied between base and emitter.
- **Output**: Taken from collector and emitter.
- **Common terminal**: Emitter is common to both input and output.

### 🔍 Key Characteristics
| Property                | Description                       |
|-------------------------|------------------------------------|
| **Voltage Gain**        | High                               |
| **Current Gain**        | Moderate to high                   |
| **Power Gain**          | High                               |
| **Phase Shift**         | 180° (inverted output)             |
| **Input Impedance**     | Moderate                           |
| **Output Impedance**    | Moderate                           |

### ✅ Advantages
- Good for voltage and power amplification.
- Most widely used configuration.

### ❌ Disadvantages
- Inverts the signal (180° phase shift).
- Less suitable for impedance matching.

### 🧰 Applications
- General-purpose signal amplification.
- Audio amplifiers.
- Intermediate stages in amplifiers.

---

## 🔷 2. Common Collector (CC) Amplifier — *Emitter Follower*

### 🔧 Configuration
- **Input**: Applied between base and collector.
- **Output**: Taken from emitter and collector.
- **Common terminal**: Collector is common.

### 🔍 Key Characteristics
| Property                | Description                           |
|-------------------------|----------------------------------------|
| **Voltage Gain**        | Approximately 1 (unity gain)           |
| **Current Gain**        | High                                   |
| **Power Gain**          | Moderate                               |
| **Phase Shift**         | 0° (no inversion)                      |
| **Input Impedance**     | High                                   |
| **Output Impedance**    | Low                                    |

### ✅ Advantages
- Excellent buffer stage.
- Good for impedance matching (high input, low output impedance).
- No signal inversion.

### ❌ Disadvantages
- No voltage gain.
- Not suitable as a stand-alone amplifier where voltage amplification is needed.

### 🧰 Applications
- Buffer between stages.
- Driving low-impedance loads.
- Voltage followers.

---

## 🔷 3. Common Base (CB) Amplifier

### 🔧 Configuration
- **Input**: Applied between emitter and base.
- **Output**: Taken from collector and base.
- **Common terminal**: Base is common.

### 🔍 Key Characteristics
| Property                | Description                             |
|-------------------------|------------------------------------------|
| **Voltage Gain**        | High                                     |
| **Current Gain**        | Less than 1                              |
| **Power Gain**          | Moderate                                 |
| **Phase Shift**         | 0° (no inversion)                        |
| **Input Impedance**     | Very low                                 |
| **Output Impedance**    | High                                     |
| **Frequency Response**  | Very wide (good for high-frequency use) |

### ✅ Advantages
- Excellent high-frequency response.
- Stable operation.

### ❌ Disadvantages
- Low input impedance—requires careful design of the driving stage.
- Limited current gain.

### 🧰 Applications
- RF (radio frequency) amplifiers.
- High-frequency signal amplification.
- Impedance matching (for low-impedance sources to high-impedance loads).

---

## 🧠 Summary Table

| Configuration   | Voltage Gain | Current Gain | Phase Shift | Input Z | Output Z | Application                    |
|-----------------|--------------|--------------|-------------|---------|----------|-------------------------------|
| **Common Emitter (CE)**   | High         | High         | 180°       | Medium  | Medium   | General amplification         |
| **Common Collector (CC)** | ≈1 (unity)   | High         | 0°         | High    | Low      | Buffering, impedance matching |
| **Common Base (CB)**       | High         | <1           | 0°         | Low     | High     | High-frequency use            |

---

Would you like visual diagrams of these configurations or an example circuit analysis for one of them?