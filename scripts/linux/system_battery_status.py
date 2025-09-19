import psutil
import os
import glob


def find_battery_path():
    """Find the battery directory in /sys/class/power_supply."""
    battery_paths = glob.glob("/sys/class/power_supply/BAT*")
    if not battery_paths:
        return None
    return battery_paths[0]  # Return the first battery found (e.g., BAT1)


def get_battery_info():
    try:
        # Get battery information using psutil
        battery = psutil.sensors_battery()

        if battery is None:
            print("No battery detected.")
            return

        # Battery percentage
        percent = battery.percent
        print(f"Battery Percentage: {percent:.2f}%")

        # Check if battery is charging
        is_charging = battery.power_plugged
        status = "Charging" if is_charging else "Discharging"
        print(f"Status: {status}")

        # Estimate remaining time (only when discharging)
        if not is_charging and battery.secsleft != psutil.POWER_TIME_UNLIMITED:
            remaining_secs = battery.secsleft
            hours = remaining_secs // 3600
            minutes = (remaining_secs % 3600) // 60
            print(f"Estimated Time Remaining: {hours} hours, {minutes} minutes")
        elif is_charging:
            # Try to estimate time to full charge using sysfs
            battery_path = find_battery_path()
            if not battery_path:
                print(
                    "Cannot estimate time to full charge (no battery found in sysfs)."
                )
                return

            try:
                # Use energy-based files
                energy_now_file = os.path.join(battery_path, "energy_now")
                energy_full_file = os.path.join(battery_path, "energy_full")
                power_now_file = os.path.join(battery_path, "power_now")

                # Verify required files exist
                if not (
                    os.path.exists(energy_now_file)
                    and os.path.exists(energy_full_file)
                    and os.path.exists(power_now_file)
                ):
                    print(
                        f"Cannot estimate time to full charge (required files not found in {battery_path})."
                    )
                    print(f"Available files: {', '.join(os.listdir(battery_path))}")
                    return

                # Read battery data
                with open(energy_now_file, "r") as f:
                    energy_now = int(f.read().strip())  # in µWh
                with open(energy_full_file, "r") as f:
                    energy_full = int(f.read().strip())  # in µWh
                with open(power_now_file, "r") as f:
                    power_now = int(f.read().strip())  # in µW

                if power_now > 0:
                    energy_remaining = energy_full - energy_now  # in µWh
                    seconds_to_full = (
                        energy_remaining / power_now
                    ) * 3600  # µWh / (µW) = hours, then * 3600 to seconds
                    hours = int(seconds_to_full // 3600)
                    minutes = int((seconds_to_full % 3600) // 60)
                    print(
                        f"Estimated Time to Full Charge: {hours} hours, {minutes} minutes"
                    )
                else:
                    print(
                        "Cannot estimate time to full charge (power_now is 0 or negative)."
                    )
            except PermissionError:
                print(
                    "Cannot estimate time to full charge (permission denied). Try running with sudo."
                )
            except FileNotFoundError:
                print(
                    f"Cannot estimate time to full charge (sysfs files not found in {battery_path})."
                )
                print(f"Available files: {', '.join(os.listdir(battery_path))}")
            except Exception as e:
                print(f"Error estimating time to full charge: {e}")
        else:
            print("No remaining time estimate available.")

    except Exception as e:
        print(f"Error retrieving battery information: {e}")


if __name__ == "__main__":
    get_battery_info()
