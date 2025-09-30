#!/usr/bin/env python3

import argparse
import sys
import subprocess
import platform

def find_process_on_port(port):
    """Find the process ID using the specified port."""
    os_type = platform.system().lower()

    try:
        if os_type == "windows":
            # For Windows, use netstat and tasklist
            result = subprocess.run(['netstat', '-ano'], capture_output=True, text=True, check=True)
            for line in result.stdout.split('\n'):
                if f':{port}' in line and ('LISTENING' in line or 'ESTABLISHED' in line):
                    parts = line.strip().split()
                    if len(parts) >= 5:
                        pid = parts[-1]
                        # Get process name
                        task_result = subprocess.run(['tasklist', '/FI', f'PID eq {pid}'], capture_output=True, text=True)
                        for task_line in task_result.stdout.split('\n'):
                            if pid in task_line and '.exe' in task_line:
                                parts_task = task_line.split()
                                if len(parts_task) >= 2:
                                    return pid, parts_task[0]
        else:
            # For macOS and Linux, use lsof
            result = subprocess.run(['lsof', '-i', f':{port}'], capture_output=True, text=True, check=False)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                if len(lines) > 1:  # Skip header
                    parts = lines[1].split()
                    if len(parts) >= 2:
                        return parts[1], f"{parts[0]} ({parts[1]})"  # PID and command
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    return None, None

def kill_process(pid):
    """Kill the process with the specified PID."""
    os_type = platform.system().lower()

    try:
        if os_type == "windows":
            subprocess.run(['taskkill', '/F', '/PID', pid], check=True)
        else:
            subprocess.run(['kill', pid], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    parser = argparse.ArgumentParser(description='Kill process running on a specific port')
    parser.add_argument('--port', '-p', type=int, default=8080,
                       help='Port number to kill process on (default: 8080)')
    args = parser.parse_args()

    port = args.port
    pid, process_info = find_process_on_port(port)

    if not pid:
        print(f"No process found running on port {port}")
        return

    print(f"Found process {process_info} running on port {port}")
    print("Do you want to kill this process? (Press Enter to kill, or 'no' to exit)")

    try:
        response = input().strip().lower()
        if response == 'no' or response == 'n':
            print("Process not killed. Exiting.")
            return
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return

    if kill_process(pid):
        print(f"Successfully killed process {pid}")
    else:
        print(f"Failed to kill process {pid}")
        print("You may need administrator privileges or the process may have already terminated.")

if __name__ == "__main__":
    main()