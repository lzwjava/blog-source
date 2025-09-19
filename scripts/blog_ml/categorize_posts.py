import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import os
from collections import Counter


# Step 1: Load and preprocess data (simplified)
def load_posts(posts_dir="original"):
    texts = []
    labels = []  # Assume manual labels: 0=ML, 1=Notes, 2=Other
    for file in os.listdir(posts_dir):
        if file.endswith(".md"):
            with open(os.path.join(posts_dir, file), "r") as f:
                content = f.read().split("---")[2].strip()  # Skip frontmatter
                texts.append(content)
                # Placeholder: load label from a dict or CSV
                labels.append(0)  # Replace with actual labels
    return texts, labels


texts, labels = load_posts()
# Check if data is loaded correctly
if len(texts) == 0:
    raise ValueError("No posts loaded. Check the '_posts' directory.")
# Build vocab (top 1000 words)
all_words = " ".join(texts).lower().split()
vocab = {word: idx for idx, word in enumerate(Counter(all_words).most_common(1000))}
vocab_size = len(vocab)


# Convert text to vectors (bag-of-words)
def text_to_vec(text):
    vec = np.zeros(vocab_size)
    for word in text.lower().split():
        if word in vocab:
            vec[vocab[word]] += 1
    return vec


X = np.array([text_to_vec(t) for t in texts])
y = torch.tensor(labels, dtype=torch.long)
# Ensure input and target sizes match
if len(X) != len(y):
    raise ValueError(f"Size mismatch: input size {len(X)}, target size {len(y)}")


# Step 2: Define model
class Classifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)


model = Classifier(vocab_size, num_classes=3)  # Adjust num_classes

# Step 3: Train
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()
X_tensor = torch.tensor(X, dtype=torch.float32)

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_tensor)
    loss = loss_fn(outputs, y)
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")


# Step 4: Inference on new post
def classify_post(text):
    vec = torch.tensor(text_to_vec(text), dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        pred = model(vec).argmax(1).item()
    return pred  # Map back to category name


# Save model
torch.save(model.state_dict(), "test/classifier.pth")
