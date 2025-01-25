import subprocess
import random
import string
import argparse
import yaml

def create_lightsail_instance(instance_name, availability_zone, bundle_id, user_data=None):
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
    try:
        result = subprocess.run(["aws", "lightsail", "get-instances"], capture_output=True, text=True, check=True)
        instances = result.stdout

        print(instances)
        
        instances_yaml = yaml.safe_load(instances)
        
        if 'instances' in instances_yaml:
            instance_list = instances_yaml['instances']
            if not instance_list:
                print("No Lightsail instances found to delete.")
                return
            
            for instance in instance_list:
                instance_name = instance['name']
                print(f"Deleting instance: {instance_name}")
                subprocess.run(["aws", "lightsail", "delete-instance", "--instance-name", instance_name], check=True)
            print("All Lightsail instances deleted successfully.")
        else:
            print("No instances found in the response.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting Lightsail instances: {e}")
    except yaml.YAMLError as e:
        print(f"Error decoding YAML response: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create or delete Lightsail instances.")
    parser.add_argument("--type", type=str, choices=["create", "delete"], required=True, help="Action type: create or delete")
    args = parser.parse_args()

    subprocess.run(["aws", "configure", "set", "region", "ap-northeast-1"], check=True)

    if args.type == "create":
        random_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
        instance_name = f"{random_chars}"
        availability_zone = "ap-northeast-1a"
        bundle_id = "nano_2_0"
        
        user_data = """#!/bin/bash
        sudo apt update
        """
        
        create_lightsail_instance(instance_name, availability_zone, bundle_id, user_data)
    elif args.type == "delete":
        delete_all_lightsail_instances()
