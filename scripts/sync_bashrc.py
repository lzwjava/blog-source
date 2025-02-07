import subprocess
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the command
command = "scp lzw@192.168.1.3:~/.bashrc {}".format(script_dir)

# Execute the command
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Check the result
if result.returncode == 0:
    print("Command executed successfully.")
    print("Output:", result.stdout)
else:
    print("Command failed with return code:", result.returncode)
    print("Error:", result.stderr)
