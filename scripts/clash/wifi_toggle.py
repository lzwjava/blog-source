import subprocess


def turn_off_wifi():
    """Turns off Wi-Fi on macOS."""
    command = ["networksetup", "-setairportpower", "Wi-Fi", "off"]

    try:
        # run the command, capture output and check for errors
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Wi-Fi successfully turned off.")
        # print("STDOUT:", result.stdout) # Uncomment to see command output
        # print("STDERR:", result.stderr) # Uncomment to see error messages
    except subprocess.CalledProcessError as e:
        print(f"Error turning off Wi-Fi: {e}")
        print(f"Command: {' '.join(e.cmd)}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
    except FileNotFoundError:
        print("Error: 'networksetup' command not found. Make sure it's in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def turn_on_wifi():
    """Turns on Wi-Fi on macOS."""
    command = ["sudo", "networksetup", "-setairportpower", "Wi-Fi", "on"]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Wi-Fi successfully turned on.")
    except subprocess.CalledProcessError as e:
        print(f"Error turning on Wi-Fi: {e}")
        print(f"Command: {' '.join(e.cmd)}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
    except FileNotFoundError:
        print("Error: 'networksetup' command not found. Make sure it's in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("Attempting to turn off Wi-Fi...")
    turn_off_wifi()

    # You can add a delay here if you want to see the effect before turning it back on
    # import time
    # time.sleep(5)

    # print("\nAttempting to turn on Wi-Fi...")
    # turn_on_wifi()
