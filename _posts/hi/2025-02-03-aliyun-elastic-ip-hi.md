---
audio: true
generated: false
image: false
lang: hi
layout: post
title: Aliyun इलास्टिक IPs का प्रबंधन
translated: true
type: post
---

यह स्क्रिप्ट Aliyun Elastic IPs (EIPs) को प्रबंधित करने के लिए एक कमांड-लाइन इंटरफ़ेस प्रदान करता है। यह आपको Python के लिए Aliyun SDK का उपयोग करके EIPs को बनाना, बाइंड करना, अनबाइंड करना और रिलीज़ करना की अनुमति देता है। स्क्रिप्ट कार्य करने और EIP के आवंटन ID के लिए तर्क लेता है।

```bash
python aliyun_elastic_ip_manager.py unbind --allocation_id eip-j6c2olvsa7jk9l42iaaa
python aliyun_elastic_ip_manager.py bind --allocation_id eip-j6c7mhenamvy6zao3haaa
python aliyun_elastic_ip_manager.py release --allocation_id eip-j6c2olvsa7jk9l42aaa
python aliyun_elastic_ip_manager.py describe
```

```python
# -*- coding: utf-8 -*-
# यह फ़ाइल स्वतः-उत्पन्न है, इसे संपादित न करें। धन्यवाद।
import logging
import os
import sys
from typing import List
import argparse
import json

from alibabacloud_vpc20160428.client import Client as Vpc20160428Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_vpc20160428 import models as vpc_20160428_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Vpc20160428Client:
        config = open_api_models.Config(
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_ID_API_KEY'],
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_API_KEY']
        )
        config.endpoint = f'vpc.cn-hongkong.aliyuncs.com'
        return Vpc20160428Client(config)

    @staticmethod
    def bind_eip(
        region_id: str,
        allocation_id: str,
        instance_id: str,
    ) -> bool:
        client = Sample.create_client()
        associate_eip_address_request = vpc_20160428_models.AssociateEipAddressRequest(
            region_id=region_id,
            allocation_id=allocation_id,
            instance_id=instance_id
        )
        runtime = util_models.RuntimeOptions(read_timeout=60000, connect_timeout=60000)
        try:
            result = client.associate_eip_address_with_options(associate_eip_address_request, runtime)
            logging.info(f"सफलतापूर्वक EIP {allocation_id} को इंस्टेंस {instance_id} से बाँध दिया गया। परिणाम: {result}")
            return True
        except Exception as error:
            logging.error(f"EIP {allocation_id} को इंस्टेंस {instance_id} से बाँधने में त्रुटि: {error}")
            if hasattr(error, 'message'):
                logging.error(f"त्रुटि संदेश: {error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"सुझाव: {error.data.get('Recommend')}")
            UtilClient.assert_as_string(str(error))
            return False
    
    @staticmethod
    def unbind_eip(
        region_id: str,
        allocation_id: str,
        instance_id: str,
    ) -> bool:
        client = Sample.create_client()
        unassociate_eip_address_request = vpc_20160428_models.UnassociateEipAddressRequest(
            region_id=region_id,
            allocation_id=allocation_id,
            instance_id=instance_id
        )
        runtime = util_models.RuntimeOptions(read_timeout=60000, connect_timeout=60000)
        try:
            result = client.unassociate_eip_address_with_options(unassociate_eip_address_request, runtime)
            logging.info(f"सफलतापूर्वक EIP {allocation_id} को इंस्टेंस {instance_id} से अनबाउंड कर दिया गया। परिणाम: {result}")
            return True
        except Exception as error:
            logging.error(f"EIP {allocation_id} को इंस्टेंस {instance_id} से अनबाउंड करने में त्रुटि: {error}")
            if hasattr(error, 'message'):
                logging.error(f"त्रुटि संदेश: {error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"सुझाव: {error.data.get('Recommend')}")
            UtilClient.assert_as_string(str(error))
            return False

    @staticmethod
    def create_eip(
        region_id: str,
    ) -> str | None:
        client = Sample.create_client()
        allocate_eip_address_request = vpc_20160428_models.AllocateEipAddressRequest(
            region_id= region_id,
            instance_charge_type='PostPaid',
            internet_charge_type='PayByTraffic',
            bandwidth='200'
        )
        runtime = util_models.RuntimeOptions(read_timeout=60000, connect_timeout=60000)
        try:
            result = client.allocate_eip_address_with_options(allocate_eip_address_request, runtime)
            print(result.body)
            allocation_id = result.body.allocation_id
            logging.info(f"सफलतापूर्वक EIP बनाया गया। आवंटन ID: {allocation_id}")
            return allocation_id
        except Exception as error:
            logging.error(f"EIP बनाने में त्रुटि: {error}")
            if hasattr(error, 'message'):
                logging.error(f"त्रुटि संदेश: {error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"सुझाव: {error.data.get('Recommend')}")
            UtilClient.assert_as_string(str(error))
            return None
    
    @staticmethod
    def release_eip(
        allocation_id: str,
    ) -> bool:
        client = Sample.create_client()
        release_eip_address_request = vpc_20160428_models.ReleaseEipAddressRequest(
            allocation_id=allocation_id
        )
        runtime = util_models.RuntimeOptions(read_timeout=60000, connect_timeout=60000)
        try:
            result = client.release_eip_address_with_options(release_eip_address_request, runtime)
            logging.info(f"सफलतापूर्वक EIP {allocation_id} को रिलीज़ कर दिया गया। परिणाम: {result}")
            return True
        except Exception as error:
            logging.error(f"EIP {allocation_id} को रिलीज़ करने में त्रुटि: {error}")
            if hasattr(error, 'message'):
                logging.error(f"त्रुटि संदेश: {error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"सुझाव: {error.data.get('Recommend')}")
            UtilClient.assert_as_string(str(error))
            return False

    @staticmethod
    def describe_eip(
        region_id: str,
        instance_id: str,
    ) -> str | None:
        client = Sample.create_client()
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id=region_id
        )
        runtime = util_models.RuntimeOptions(read_timeout=60000, connect_timeout=60000)
        try:
            result = client.describe_eip_addresses_with_options(describe_eip_addresses_request, runtime)
            logging.info(f"सफलतापूर्वक EIP का वर्णन किया गया।")
            print(json.dumps(result.body.to_map(), indent=4))
            if result.body.eip_addresses and hasattr(result.body.eip_addresses, 'eip_address') and result.body.eip_addresses.eip_address:
                for eip in result.body.eip_addresses.eip_address:
                    if eip.instance_id == instance_id:
                        return eip.allocation_id
                logging.info(f"इंस्टेंस {instance_id} के लिए कोई EIP पता नहीं मिला")
                return None
            else:
                logging.info("कोई EIP पता नहीं मिला।")
                return None
        except Exception as error:
            logging.error(f"EIP का वर्णन करने में त्रुटि: {error}")
            if hasattr(error, 'message'):
                logging.error(f"त्रुटि संदेश: {error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"सुझाव: {error.data.get('Recommend')}")
            UtilClient.assert_as_string(str(error))
            return None

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        region_id = "cn-hongkong"
        instance_id = "i-j6c44l4zpphv7u7agdbk"

        parser = argparse.ArgumentParser(description='Aliyun Elastic IPs को प्रबंधित करें।')
        parser.add_argument('job', choices=['create', 'bind', 'unbind', 'release', 'describe', 'all'], help='किया जाने वाला कार्य: बनाएँ, बाँधें, या अनबाँधें।')
        parser.add_argument('--allocation_id', type=str, help='EIP का आवंटन ID।')
        parser.add_argument('--instance_id', type=str, default=instance_id, help='EIP को बाँधने/अनबाँधने के लिए इंस्टेंस ID।')

        parsed_args = parser.parse_args(args)

        if parsed_args.job == 'create':
            new_allocation_id = Sample.create_eip(region_id)
            if new_allocation_id:
                print(f"EIP निर्माण प्रक्रिया सफलतापूर्वक शुरू की गई। आवंटन ID: {new_allocation_id}")
            else:
                print("EIP निर्माण प्रक्रिया विफल रही।")
        elif parsed_args.job == 'bind':
            if not parsed_args.allocation_id:
                print("त्रुटि: बाँधने के कार्य के लिए --allocation_id आवश्यक है।")
                return
            if Sample.bind_eip(region_id, parsed_args.allocation_id, parsed_args.instance_id):
                print(f"EIP बाँधने की प्रक्रिया EIP {parsed_args.allocation_id} और इंस्टेंस {parsed_args.instance_id} के लिए सफलतापूर्वक शुरू की गई।")
            else:
                print(f"EIP बाँधने की प्रक्रिया EIP {parsed_args.allocation_id} और इंस्टेंस {parsed_args.instance_id} के लिए विफल रही।")
        elif parsed_args.job == 'unbind':
            if not parsed_args.allocation_id:
                print("त्रुटि: अनबाँधने के कार्य के लिए --allocation_id आवश्यक है।")
                return
            if Sample.unbind_eip(region_id, parsed_args.allocation_id, parsed_args.instance_id):
                print(f"EIP अनबाँधने की प्रक्रिया EIP {parsed_args.allocation_id} और इंस्टेंस {parsed_args.instance_id} के लिए सफलतापूर्वक शुरू की गई।")
            else:
                print(f"EIP अनबाँधने की प्रक्रिया EIP {parsed_args.allocation_id} और इंस्टेंस {parsed_args.instance_id} के लिए विफल रही।")
        elif parsed_args.job == 'release':
            if not parsed_args.allocation_id:
                print("त्रुटि: रिलीज़ करने के कार्य के लिए --allocation_id आवश्यक है।")
                return
            if Sample.release_eip(parsed_args.allocation_id):
                 print(f"EIP रिलीज़ करने की प्रक्रिया EIP {parsed_args.allocation_id} के लिए सफलतापूर्वक शुरू की गई।")
            else:
                print(f"EIP रिलीज़ करने की प्रक्रिया EIP {parsed_args.allocation_id} के लिए विफल रही।")
        elif parsed_args.job == 'describe':
            if not parsed_args.instance_id:
                print("त्रुटि: वर्णन करने के कार्य के लिए --instance_id आवश्यक है।")
                return
            allocation_id = Sample.describe_eip(region_id, parsed_args.instance_id)
            if allocation_id:
                print(f"आवंटन ID: {allocation_id}")
            else:
                print("कोई EIP नहीं मिला।")
        elif parsed_args.job == 'all':
            # वर्तमान आवंटन ID प्राप्त करने के लिए वर्णन करें
            current_allocation_id = Sample.describe_eip(region_id, parsed_args.instance_id)
            if current_allocation_id:
                print(f"वर्तमान आवंटन ID: {current_allocation_id}")
            else:
                print("संसाधित करने के लिए कोई EIP नहीं मिला।")
                return
            
            # वर्तमान EIP अनबाँधें
            if current_allocation_id:
                if Sample.unbind_eip(region_id, current_allocation_id, parsed_args.instance_id):
                    print(f"सफलतापूर्वक EIP {current_allocation_id} को इंस्टेंस {parsed_args.instance_id} से अनबाँध दिया गया।")
                else:
                    print(f"EIP {current_allocation_id} को इंस्टेंस {parsed_args.instance_id} से अनबाँधने में विफल।")
                    return
            
            # नया EIP बनाएँ
            new_allocation_id = Sample.create_eip(region_id)
            if new_allocation_id:
                print(f"EIP निर्माण प्रक्रिया सफलतापूर्वक शुरू की गई। नया आवंटन ID: {new_allocation_id}")
            else:
                print("EIP निर्माण प्रक्रिया विफल रही।")
                return
            
            # नया EIP बाँधें
            if Sample.bind_eip(region_id, new_allocation_id, parsed_args.instance_id):
                print(f"सफलतापूर्वक नया EIP {new_allocation_id} इंस्टेंस {parsed_args.instance_id} से बाँध दिया गया।")
            else:
                print(f"नया EIP {new_allocation_id} को इंस्टेंस {parsed_args.instance_id} से बाँधने में विफल।")
                return
            
            # पुराने EIP को रिलीज़ करें
            if current_allocation_id:
                if Sample.release_eip(current_allocation_id):
                    print(f"सफलतापूर्वक पुराना EIP {current_allocation_id} रिलीज़ कर दिया गया।")
                else:
                    print(f"पुराना EIP {current_allocation_id} रिलीज़ करने में विफल।")
            
            # अंतिम स्थिति दिखाने के लिए फिर से वर्णन करें
            final_allocation_id = Sample.describe_eip(region_id, parsed_args.instance_id)
            if final_allocation_id:
                print(f"अंतिम आवंटन ID: {final_allocation_id}")
            else:
                print("संसाधित करने के बाद कोई EIP नहीं मिला।")


    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        associate_eip_address_request = vpc_20160428_models.AssociateEipAddressRequest(
            region_id='cn-hongkong'
        )
        runtime = util_models.RuntimeOptions()
        try:
            await client.associate_eip_address_with_options_async(associate_eip_address_request, runtime)
        except Exception as error:
            print(error)
            if hasattr(error, 'message'):
                print(error.message)
            if hasattr(error, 'data') and error.data.get("Recommend"):
                print(error.data.get("Recommend"))
            UtilClient.assert_as_string(str(error))


if __name__ == '__main__':
    Sample.main(sys.argv[1:])

# python scripts/auto-ss-config/aliyun_elastic_ip_manager.py create
# python scripts/auto-ss-config/aliyun_elastic_ip_manager.py unbind --allocation_id eip-j6c2olvsa7jk9l42i1aaa
# python scripts/auto-ss-config/aliyun_elastic_ip_manager.py bind --allocation_id eip-j6c7mhenamvy6zao3haaa
# python scripts/auto-ss-config/aliyun_elastic_ip_manager.py release --allocation_id "eip-j6c2olvsa7jk9l42i"
# python scripts/auto-ss-config/aliyun_elastic_ip_manager.py describe
# python scripts/auto-ss-config/aliyun_elastic_ip_manager.py all
```
