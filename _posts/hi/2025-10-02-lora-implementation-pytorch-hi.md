---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: पायटॉर्च के साथ लोरा कार्यान्वयन उदाहरण
translated: true
type: note
---

नीचे एक Python कोड उदाहरण है जो एक साधारण न्यूरल नेटवर्क को फाइन-ट्यून करने के लिए PyTorch का उपयोग करके LoRA (लो-रैंक एडाप्टेशन) को लागू करने का तरीका दर्शाता है। यह उदाहरण LoRA के साथ एक प्री-ट्रेंड लीनियर लेयर को एडाप्ट करने पर केंद्रित है, जहाँ मूल वेट्स को फ्रीज़ रखा जाता है और लो-रैंक अपडेट मैट्रिक्स पेश किए जाते हैं। कोड में एक टॉय डेटासेट के साथ एक बेसिक सेटअप और इस अवधारणा को समझाने के लिए एक मिनिमल ट्रेनिंग लूप शामिल है।

<xaiArtifact artifact_id="1327e99b-24b5-4b0d-9ffd-5b4c2d1472af" artifact_version_id="4053525d-2225-4913-a3b9-b7d66b48daea" title="lora_demo.py" contentType="text/python">
import torch
import torch.nn as nn
import torch.optim as optim

# LoRA लेयर को परिभाषित करें
class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # मूल फ्रोजन वेट्स
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # मूल वेट्स को फ्रीज़ करें
        # LoRA पैरामीटर्स: लो-रैंक मैट्रिक्स A और B
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # LoRA अपडेट्स के लिए स्केलिंग फैक्टर

    def forward(self, x):
        # मूल लीनियर ट्रांसफॉर्मेशन + LoRA एडजस्टमेंट
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment

# प्रदर्शन के लिए टॉय डेटासेट
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # रैंडम इनपुट फीचर्स
    y = torch.randn(n_samples, 10)  # रैंडम टार्गेट आउटपुट
    return X, y

# ट्रेनिंग फंक्शन
def train_model(model, X, y, epochs=10, lr=0.01):
    criterion = nn.MSELoss()
    optimizer = optim.Adam([param for param in model.parameters() if param.requires_grad], lr=lr)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

# मेन एक्जिक्यूशन
def main():
    # प्रजननीयता के लिए रैंडम सीड सेट करें
    torch.manual_seed(42)
    
    # टॉय डेटासेट बनाएं
    X, y = create_toy_dataset()
    
    # LoRA के साथ मॉडल को इनिशियलाइज़ करें
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # ट्रेन करने योग्य पैरामीटर्स की गिनती करें
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Trainable parameters: {trainable_params}")
    print(f"Total parameters: {total_params}")
    
    # मॉडल को ट्रेन करें
    train_model(model, X, y)

if __name__ == "__main__":
    main()
</xaiArtifact>

यह कोड एक `LoRALayer` को परिभाषित करता है जो लो-रैंक एडाप्टेशन मैट्रिक्स (`lora_A` और `lora_B`) के साथ एक स्टैंडर्ड लीनियर लेयर को रैप करता है। मूल वेट्स को फ्रीज़ कर दिया जाता है, और ट्रेनिंग के दौरान केवल LoRA पैरामीटर्स को अपडेट किया जाता है। टॉय डेटासेट और ट्रेनिंग लूप दर्शाते हैं कि कैसे LoRA ट्रेन करने योग्य पैरामीटर्स की संख्या को कम करते हुए भी फाइन-ट्यूनिंग की अनुमति देता है। आप ट्रेनिंग प्रक्रिया और पैरामीटर दक्षता को कार्यरत देखने के लिए PyTorch इंस्टॉल होने पर इस कोड को रन कर सकते हैं।

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)