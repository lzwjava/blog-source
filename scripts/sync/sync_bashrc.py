import subprocess
import os
import argparse

# Get the directory of the current script
dir = os.path.dirname(os.path.abspath(__file__))

script_dir = os.path.join(dir, "config")

# Set up argument parser
parser = argparse.ArgumentParser(description="Sync .bashrc between local and remote")
parser.add_argument(
    "direction",
    choices=["back", "forth"],
    help="Direction of sync: back (remote to local) or forth (local to remote)",
)
args = parser.parse_args()

# Define commands based on direction
if args.direction == "back":
    command = "scp lzw@192.168.1.3:~/.bashrc {}".format(script_dir)
    action = "Copying .bashrc from remote to local"
else:
    command = "scp {}/.bashrc lzw@192.168.1.3:~".format(script_dir)
    action = "Copying .bashrc from local to remote"

print(action)
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Check the result
if result.returncode == 0:
    print("Command executed successfully.")
    print("Output:", result.stdout)
else:
    print("Command failed with return code:", result.returncode)
    print("Error:", result.stderr)
