import subprocess

def create_lightsail_instance(instance_name, availability_zone, bundle_id, key_pair_name, user_data=None):
    """
    Creates an Amazon Lightsail instance using the AWS CLI.

    Args:
        instance_name (str): The name of the Lightsail instance.
        availability_zone (str): The AWS availability zone (e.g., ap-northeast-1a).
        bundle_id (str): The bundle ID for the instance (e.g., micro_2_0).
        key_pair_name (str): The name of the SSH key pair.
        user_data (str, optional): User data to pass to the instance. Defaults to None.
    """
    command = [
        "aws", "lightsail", "create-instances",
        "--instance-names", instance_name,
        "--availability-zone", availability_zone,
        "--bundle-id", bundle_id,
        "--key-pair-name", key_pair_name,
        "--tags", "key=created_by,value=lightsail_script",
        "--blueprint-id", "ubuntu_24_04" # Added blueprint-id
    ]
    
    if user_data:
        command.extend(["--user-data", user_data])

    try:
        subprocess.run(command, check=True)
        print(f"Lightsail instance '{instance_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating Lightsail instance: {e}")

if __name__ == "__main__":
    instance_name = "my-lightsail-instance"
    availability_zone = "ap-northeast-1a"  # Tokyo, Zone A
    bundle_id = "nano_2_0" # 512 MB RAM, 2 vCPUs, 20 GB SSD
    key_pair_name = "my-lightsail-key" # Replace with your key pair name
    
    # Example of passing user data to install docker
    user_data = """#!/bin/bash
    sudo apt update
    sudo apt install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    """
    
    create_lightsail_instance(instance_name, availability_zone, bundle_id, key_pair_name, user_data)
