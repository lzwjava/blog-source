#!/usr/bin/env python3

import subprocess
import re

def find_process_on_port(port):
    """Find the process ID using the specified port on Unix systems (macOS/Linux)."""
    try:
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

def find_processes_by_pattern(pattern):
    """Find all process IDs matching the specified pattern on Unix systems (macOS/Linux)."""
    processes = []
    try:
        # Use ps aux and grep to find processes containing the pattern
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            for line in lines[1:]:  # Skip header
                if pattern.lower() in line.lower():
                    parts = line.split()
                    if len(parts) >= 11:  # ps aux format: USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
                        pid = parts[1]
                        command = ' '.join(parts[10:])
                        processes.append((pid, f"{command} ({pid})"))
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    return processes

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

def get_process_details(pid):
    """Get detailed information about a process on Unix systems (macOS/Linux)."""
    try:
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

def kill_process(pid):
    """Kill the process with the specified PID on Unix systems (macOS/Linux)."""
    try:
        result = subprocess.run(['kill', '-9', pid], capture_output=True, text=True, check=False)
        output = result.stdout + result.stderr
        return 'Killed' in output
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False