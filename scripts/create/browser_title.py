#!/usr/bin/env python3
"""Cross-platform script to get the current browser tab title."""

import sys
import platform
import subprocess


def get_linux_firefox_title():
    """Get the current Firefox tab title on Linux."""
    try:
        # Use xdotool to get the active window title
        result = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'],
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            title = result.stdout.strip()
            # Firefox titles typically include the page title followed by " - Mozilla Firefox"
            if " - Mozilla Firefox" in title:
                return title.split(" - Mozilla Firefox")[0]
            return title
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def get_macos_safari_title():
    """Get the current Safari tab title on macOS."""
    try:
        # Use AppleScript to get the current Safari tab title
        script = '''
        tell application "Safari"
            set currentTab to current tab of window 1
            return name of currentTab
        end tell
        '''
        result = subprocess.run(['osascript', '-e', script],
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, subprocess.SubprocessError):
        pass
    return None


def get_windows_edge_title():
    """Get the current Edge tab title on Windows."""
    try:
        # Use PowerShell to get Microsoft Edge window title
        ps_script = '''
        $edge = Get-Process | Where-Object { $_.ProcessName -eq "msedge" } | Select-Object -First 1
        if ($edge) {
            Add-Type -AssemblyName Microsoft.VisualBasic
            [Microsoft.VisualBasic.Interaction]::AppActivate($edge.Id) | Out-Null
            $title = Get-Process -Id $edge.Id | Select-Object -ExpandProperty MainWindowTitle
            Write-Output $title
        }
        '''
        result = subprocess.run(['powershell.exe', '-Command', ps_script],
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0 and result.stdout.strip():
            title = result.stdout.strip()
            # Edge titles may include " - Microsoft Edge" suffix
            if " - Microsoft Edge" in title:
                return title.split(" - Microsoft Edge")[0]
            return title
    except (subprocess.TimeoutExpired, subprocess.SubprocessError):
        pass
    return None


def main():
    """Main function to get browser title based on platform."""
    system = platform.system().lower()

    title = None

    if system == "linux":
        title = get_linux_firefox_title()
    elif system == "darwin":  # macOS
        title = get_macos_safari_title()
    elif system == "windows":
        title = get_windows_edge_title()
    else:
        print(f"Unsupported platform: {system}", file=sys.stderr)
        sys.exit(1)

    if title:
        print(title)
    else:
        print("Could not retrieve browser title", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()