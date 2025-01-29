import logging
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.UnassociateEipAddressRequest import UnassociateEipAddressRequest

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def unbind_eip(region_id, access_key_id, access_key_secret, instance_id, allocation_id):
    """
    Unbinds an Elastic IP from an instance.

    Args:
        region_id (str): The ID of the region.
        access_key_id (str): The Access Key ID.
        access_key_secret (str): The Access Key Secret.
        instance_id (str): The ID of the instance.
        allocation_id (str): The ID of the Elastic IP.
    """
    try:
        client = AcsClient(access_key_id, access_key_secret, region_id)
        request = UnassociateEipAddressRequest()
        request.set_InstanceId(instance_id)
        request.set_AllocationId(allocation_id)
        result = client.do_action_with_exception(request)
        logging.info(f"Successfully unbound EIP {allocation_id} from instance {instance_id}. Result: {result}")
        return True
    except Exception as e:
        logging.error(f"Error unbinding EIP {allocation_id} from instance {instance_id}: {e}")
        return False

if __name__ == '__main__':
    # Example usage (replace with your actual values)
    region_id = "your_region_id"
    access_key_id = "your_access_key_id"
    access_key_secret = "your_access_key_secret"
    instance_id = "your_instance_id"
    allocation_id = "your_allocation_id"

    if unbind_eip(region_id, access_key_id, access_key_secret, instance_id, allocation_id):
        print("EIP unbinding process initiated successfully.")
    else:
        print("EIP unbinding process failed.")
