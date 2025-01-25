import subprocess
import random
import string
import argparse
import yaml
import os

KEY_PATH = os.path.expanduser("~/Downloads/LightsailDefaultKey-ap-northeast-1.pem")

def _get_lightsail_instances():
    print("Fetching Lightsail instances...")
    try:
        result = subprocess.run(["aws", "lightsail", "get-instances"], capture_output=True, text=True, check=True)
        print("Lightsail instances fetched successfully.")
        return yaml.safe_load(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error getting Lightsail instances: {e}")
        return None
    except yaml.YAMLError as e:
        print(f"Error decoding YAML response: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def create_lightsail_instance(instance_name, availability_zone, bundle_id, user_data=None):
    random_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
    instance_name = f"{random_chars}"
    availability_zone = "ap-northeast-1a"
    bundle_id = "nano_2_0"
    
    user_data = """#!/bin/bash
    sudo apt update
    """
    print(f"Creating Lightsail instance with name: {instance_name}, zone: {availability_zone}, bundle: {bundle_id}...")

    command = [
        "aws", "lightsail", "create-instances",
        "--instance-names", instance_name,
        "--availability-zone", availability_zone,
        "--bundle-id", bundle_id,
        "--blueprint-id", "ubuntu_24_04"
    ]
    
    if user_data:
        command.extend(["--user-data", user_data])

    try:
        subprocess.run(command, check=True)
        print(f"Lightsail instance '{instance_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating Lightsail instance: {e}")

def delete_all_lightsail_instances():
    instances_yaml = _get_lightsail_instances()
    if not instances_yaml or 'instances' not in instances_yaml:
        print("No Lightsail instances found to delete.")
        return

    instance_list = instances_yaml['instances']
    if not instance_list:
        print("No Lightsail instances found to delete.")
        return
    
    for instance in instance_list:
        instance_name = instance['name']
        print(f"Deleting instance: {instance_name}")
        print(f"Executing command: aws lightsail delete-instance --instance-name {instance_name}")
        subprocess.run(["aws", "lightsail", "delete-instance", "--instance-name", instance_name], check=True)
    print("All Lightsail instances deleted successfully.")


def install_outline_server():
    instances_yaml = _get_lightsail_instances()
    if not instances_yaml or 'instances' not in instances_yaml or not instances_yaml['instances']:
        print("No Lightsail instances found to install outline server on.")
        return
    
    instance = instances_yaml['instances'][0]
    instance_name = instance['name']
    public_ip = instance['publicIpAddress']
    print(f"Installing outline server on instance: {instance_name} with IP: {public_ip}")
    user_data = """#!/bin/bash
    sudo apt update
    sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"
    """
    
    
    os.chmod(KEY_PATH, 0o600)
    print(f"Executing command: chmod 600 {KEY_PATH}")

    ssh_command = [
        "ssh",
        "-i",
        KEY_PATH,
        f"ubuntu@{public_ip}",
        user_data
    ]
    print(f"Executing command: {' '.join(ssh_command)}")
    try:
        subprocess.run(ssh_command, check=True)
        print(f"Outline server installed on {instance_name} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing outline server: {e}")


def open_firewall_ports():
    instances_yaml = _get_lightsail_instances()
    if not instances_yaml or 'instances' not in instances_yaml or not instances_yaml['instances']:
        print("No Lightsail instances found to open firewall ports on.")
        return
    
    instance = instances_yaml['instances'][0]
    instance_name = instance['name']
    print(f"Opening firewall ports for instance: {instance_name}")
    for protocol in ["tcp", "udp"]:
        command = [
            "aws", "lightsail", "open-instance-public-ports",
            "--port-info", f"protocol={protocol},fromPort=1000,toPort=65535",
            "--instance-name", instance_name
        ]
        print(f"Executing command: {' '.join(command)}")
        subprocess.run(command, check=True)
    print(f"Firewall ports opened for instance '{instance_name}' successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create or delete Lightsail instances.")
    parser.add_argument("--job", type=str, choices=["create", "delete", "install", "firewall"], required=True, help="Action type: create or delete or install or firewall")
    args = parser.parse_args()

    print(f"Setting AWS region to ap-northeast-1")
    subprocess.run(["aws", "configure", "set", "region", "ap-northeast-1"], check=True)

    if args.job == "create":           
        create_lightsail_instance()
    elif args.job == "delete":
        delete_all_lightsail_instances()
    elif args.job == "install":
        install_outline_server()
    elif args.job == "firewall":
        open_firewall_ports()
