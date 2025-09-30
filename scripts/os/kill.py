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

def get_process_details(pid):
    """Get detailed information about a process."""
    os_type = platform.system().lower()

    try:
        if os_type == "windows":
            # For Windows, use tasklist and wmic for more details
            task_result = subprocess.run(['tasklist', '/FI', f'PID eq {pid}', '/FO', 'CSV'],
                                       capture_output=True, text=True)
            if task_result.returncode == 0:
                lines = task_result.stdout.strip().split('\n')
                if len(lines) > 1:
                    parts = lines[1].replace('"', '').split(',')
                    return {
                        'name': parts[0],
                        'pid': parts[1],
                        'started': None,  # Windows tasklist doesn't easily show start time
                        'command': f"{parts[0]} (PID: {parts[1]})"
                    }
        else:
            # For macOS and Linux, use ps
            ps_result = subprocess.run(['ps', '-p', pid, '-o', 'pid,ppid,lstart,etime,command'],
                                     capture_output=True, text=True)
            if ps_result.returncode == 0:
                lines = ps_result.stdout.strip().split('\n')
                if len(lines) > 1:
                    # Skip header and find data line
                    data_line = None
                    for line in lines[1:]:
                        line = line.strip()
                        if line.startswith(pid):
                            data_line = line
                            break

                    if data_line:
                        # Parse the ps output carefully
                        # Format: PID PPID STARTED ELAPSED COMMAND
                        # Where STARTED can have multiple spaces: "Mon Sep 29 23:40:03 2025"
                        import re
                        match = re.match(r'(\d+)\s+(\d+)\s+(.*?)\s+(\d+-\d+:\d+:\d+)\s+(.+)', data_line)
                        if match:
                            pid_val, ppid_val, lstart_val, etime_val, command_val = match.groups()
                            # Check if it's Java and try to extract jar/class name
                            app_info = extract_java_app_info(command_val)

                            return {
                                'name': 'java' if 'java' in command_val.lower() else command_val.split()[0],
                                'pid': pid_val,
                                'ppid': ppid_val,
                                'started': lstart_val,
                                'elapsed': etime_val,
                                'command': command_val,
                                'app_info': app_info
                            }
    except (subprocess.CalledProcessError, FileNotFoundError, IndexError):
        pass

    return None

def extract_java_app_info(command):
    """Extract application information from Java command line."""
    if not command or 'java' not in command.lower():
        return None

    parts = command.split()

    # Look for common Spring Boot patterns
    for i, part in enumerate(parts):
        if part.endswith('.jar'):
            return f"JAR: {part}"
        elif part == '-cp' and i + 1 < len(parts):
            return f"Classpath with main class: {parts[i+1] if i+2 < len(parts) else 'Unknown'}"
        elif not part.startswith('-') and '.class' in part:
            return f"Class: {part}"

    # Check for Spring Boot specific indicators
    if 'springframework' in command or 'spring-boot' in command:
        return "Spring Boot Application"

    # Generic Java app
    return "Java Application"

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

    # Get detailed process information
    details = get_process_details(pid)

    print(f"Found process running on port {port}:")
    print(f"  Name: {process_info}")

    if details:
        if details.get('app_info'):
            print(f"  Application: {details['app_info']}")
        if details.get('started'):
            print(f"  Started: {details['started']}")
        if details.get('elapsed'):
            print(f"  Running for: {details['elapsed']}")
        if details.get('ppid'):
            print(f"  Parent PID: {details['ppid']}")

        # Show full command for Java processes
        if details.get('name') == 'java' and details.get('command'):
            print(f"  Command: {details['command']}")
    else:
        print("  (Unable to retrieve detailed process information)")

    print("")
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