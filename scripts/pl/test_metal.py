import torch
import argparse
import time

parser = argparse.ArgumentParser(description="Test torch with MPS, CUDA, or CPU.")
parser.add_argument(
    "--device",
    type=str,
    default="mps",
    choices=["mps", "cuda", "cpu"],
    help="Device to use (mps, cuda, or cpu)",
)
args = parser.parse_args()

if args.device == "mps":
    if torch.backends.mps.is_available():
        print("Metal is available")
        device = torch.device("mps")
    else:
        print("Metal is not available, using CPU instead")
        device = torch.device("cpu")
elif args.device == "cuda":
    if torch.cuda.is_available():
        print("CUDA is available")
        device = torch.device("cuda")
    else:
        raise Exception("CUDA is not available")
elif args.device == "cpu":
    device = torch.device("cpu")
    print("Using CPU")
else:
    print("Invalid device specified, using CPU instead")
    device = torch.device("cpu")


# Create a tensor and move it to the specified device
x = torch.randn(5000, 5000, device=device)
y = torch.randn(5000, 5000, device=device)

# Perform a more complex computation
start_time = time.time()
result = torch.matmul(x, y)
for _ in range(10):
    result = torch.matmul(result, y)
end_time = time.time()

# Print the result
print(result)
print(f"Time taken: {end_time - start_time:.4f} seconds")
