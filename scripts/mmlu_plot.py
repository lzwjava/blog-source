import matplotlib.pyplot as plt
import os

# Sample data (replace with your actual data)
models = ['mistral-7b-instruct-v0.2 (llama-server)', 'Mistral-7B-Instruct-v0.3 (ollama)', 'deepseek v3 (API)', 'gemini-1.5-flash (API)']
accuracy = [40.00, 40.00, 78.00, 72.00]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(models, accuracy, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
plt.xlabel('Model')
plt.ylabel('Accuracy (%)')
plt.title('MMLU Benchmark Accuracy')
plt.ylim(0, 100)  # Set y-axis limit to 0-100 for percentage
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.tight_layout()

# Add accuracy values on top of the bars
for i, val in enumerate(accuracy):
    plt.text(i, val + 1, f'{val:.2f}%', ha='center', va='bottom')

# Save the chart as a PNG file in the current directory
plt.savefig(os.path.join('.', 'mmlu_accuracy_chart.png'))
plt.show()
