---
audio: true
generated: false
image: false
lang: hant
layout: post
title: 管理阿里雲彈性IP
translated: true
type: post
---

本腳本提供一個命令列介面來管理阿里雲彈性公網 IP (EIP)。它允許您使用阿里雲 Python SDK 來建立、綁定、解綁和釋放 EIP。腳本接收要執行的作業和 EIP 的分配 ID 作為參數。

```bash
python aliyun_elastic_ip_manager.py unbind --allocation_id eip-j6c2olvsa7jk9l42iaaa
python aliyun_elastic_ip_manager.py bind --allocation_id eip-j6c7mhenamvy6zao3haaa
python aliyun_elastic_ip_manager.py release --allocation_id eip-j6c2olvsa7jk9l42aaa
python aliyun_elastic_ip_manager.py describe
```

```python
# -*- coding: utf-8 -*-
# 此檔案為自動生成，請勿編輯。謝謝。
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
            logging.info(f"成功綁定 EIP {allocation_id} 到實例 {instance_id}。結果：{result}")
            return True
        except Exception as error:
            logging.error(f"綁定 EIP {allocation_id} 到實例 {instance_id} 時發生錯誤：{error}")
            if hasattr(error, 'message'):
                logging.error(f"錯誤訊息：{error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"建議：{error.data.get('Recommend')}")
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
            logging.info(f"成功解除綁定 EIP {allocation_id} 與實例 {instance_id}。結果：{result}")
            return True
        except Exception as error:
            logging.error(f"解除綁定 EIP {allocation_id} 與實例 {instance_id} 時發生錯誤：{error}")
            if hasattr(error, 'message'):
                logging.error(f"錯誤訊息：{error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"建議：{error.data.get('Recommend')}")
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
            internet_charge_type='PayByBandwidth',
            bandwidth='200'
        )
        runtime = util_models.RuntimeOptions(read_timeout=60000, connect_timeout=60000)
        try:
            result = client.allocate_eip_address_with_options(allocate_eip_address_request, runtime)
            print(result.body)
            allocation_id = result.body.allocation_id
            logging.info(f"成功建立 EIP。分配 ID：{allocation_id}")
            return allocation_id
        except Exception as error:
            logging.error(f"建立 EIP 時發生錯誤：{error}")
            if hasattr(error, 'message'):
                logging.error(f"錯誤訊息：{error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"建議：{error.data.get('Recommend')}")
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
            logging.info(f"成功釋放 EIP {allocation_id}。結果：{result}")
            return True
        except Exception as error:
            logging.error(f"釋放 EIP {allocation_id} 時發生錯誤：{error}")
            if hasattr(error, 'message'):
                logging.error(f"錯誤訊息：{error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"建議：{error.data.get('Recommend')}")
            UtilClient.assert_as_string(str(error))
            return False

    @staticmethod
    def describe_eip(
        region_id: str,
    ) -> str | None:
        client = Sample.create_client()
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id=region_id
        )
        runtime = util_models.RuntimeOptions(read_timeout=60000, connect_timeout=60000)
        try:
            result = client.describe_eip_addresses_with_options(describe_eip_addresses_request, runtime)
            logging.info(f"成功描述 EIP。")
            print(json.dumps(result.body.to_map(), indent=4))
            if result.body.eip_addresses and hasattr(result.body.eip_addresses, 'eip_address') and result.body.eip_addresses.eip_address:
                if len(result.body.eip_addresses.eip_address) > 0:
                    first_allocation_id = result.body.eip_addresses.eip_address[0].allocation_id
                    return first_allocation_id
                else:
                    logging.info("沒有找到任何 EIP 位址。")
                    return None
            else:
                logging.info("沒有找到任何 EIP 位址。")
                return None
        except Exception as error:
            logging.error(f"描述 EIP 時發生錯誤：{error}")
            if hasattr(error, 'message'):
                logging.error(f"錯誤訊息：{error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"建議：{error.data.get('Recommend')}")
            UtilClient.assert_as_string(str(error))
            return None

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        region_id = "cn-hongkong"
        instance_id = "i-j6c44l4zpphv7u7agdbk"

        parser = argparse.ArgumentParser(description='管理阿里雲彈性公網 IP。')
        parser.add_argument('job', choices=['create', 'bind', 'unbind', 'release', 'describe', 'all'], help='要執行的作業：create、bind 或 unbind。')
        parser.add_argument('--allocation_id', type=str, help='EIP 的分配 ID。')
        parser.add_argument('--instance_id', type=str, default=instance_id, help='要綁定/解綁 EIP 的實例 ID。')

        parsed_args = parser.parse_args(args)

        if parsed_args.job == 'create':
            new_allocation_id = Sample.create_eip(region_id)
            if new_allocation_id:
                print(f"EIP 建立程序已成功啟動。分配 ID：{new_allocation_id}")
            else:
                print("EIP 建立程序失敗。")
        elif parsed_args.job == 'bind':
            if not parsed_args.allocation_id:
                print("錯誤：bind 作業需要 --allocation_id。")
                return
            if Sample.bind_eip(region_id, parsed_args.allocation_id, parsed_args.instance_id):
                print(f"EIP 綁定程序已成功啟動，EIP 為 {parsed_args.allocation_id}，實例為 {parsed_args.instance_id}。")
            else:
                print(f"EIP 綁定程序失敗，EIP 為 {parsed_args.allocation_id}，實例為 {parsed_args.instance_id}。")
        elif parsed_args.job == 'unbind':
            if not parsed_args.allocation_id:
                print("錯誤：unbind 作業需要 --allocation_id。")
                return
            if Sample.unbind_eip(region_id, parsed_args.allocation_id, parsed_args.instance_id):
                print(f"EIP 解綁程序已成功啟動，EIP 為 {parsed_args.allocation_id}，實例為 {parsed_args.instance_id}。")
            else:
                print(f"EIP 解綁程序失敗，EIP 為 {parsed_args.allocation_id}，實例為 {parsed_args.instance_id}。")
        elif parsed_args.job == 'release':
            if not parsed_args.allocation_id:
                print("錯誤：release 作業需要 --allocation_id。")
                return
            if Sample.release_eip(parsed_args.allocation_id):
                 print(f"EIP 釋放程序已成功啟動，EIP 為 {parsed_args.allocation_id}。")
            else:
                print(f"EIP 釋放程序失敗，EIP 為 {parsed_args.allocation_id}。")
        elif parsed_args.job == 'describe':
            Sample.describe_eip(region_id)
        elif parsed_args.job == 'all':
            # 查詢以取得目前的分配 ID
            current_allocation_id = Sample.describe_eip(region_id)
            if current_allocation_id:
                print(f"目前的分配 ID：{current_allocation_id}")
            else:
                print("沒有找到任何 EIP 可處理。")
                return
            
            # 解除綁定目前的 EIP
            if current_allocation_id:
                if Sample.unbind_eip(region_id, current_allocation_id, parsed_args.instance_id):
                    print(f"成功解除綁定 EIP {current_allocation_id} 與實例 {parsed_args.instance_id}。")
                else:
                    print(f"解除綁定 EIP {current_allocation_id} 與實例 {parsed_args.instance_id} 失敗。")
                    return
            
            # 建立新的 EIP
            new_allocation_id = Sample.create_eip(region_id)
            if new_allocation_id:
                print(f"EIP 建立程序已成功啟動。新的分配 ID：{new_allocation_id}")
            else:
                print("EIP 建立程序失敗。")
                return
            
            # 綁定新的 EIP
            if Sample.bind_eip(region_id, new_allocation_id, parsed_args.instance_id):
                print(f"成功綁定新的 EIP {new_allocation_id} 到實例 {parsed_args.instance_id}。")
            else:
                print(f"綁定新的 EIP {new_allocation_id} 到實例 {parsed_args.instance_id} 失敗。")
                return
            
            # 釋放舊的 EIP
            if current_allocation_id:
                if Sample.release_eip(current_allocation_id):
                    print(f"成功釋放舊的 EIP {current_allocation_id}。")
                else:
                    print(f"釋放舊的 EIP {current_allocation_id} 失敗。")
            
            # 再次查詢以顯示最終狀態
            final_allocation_id = Sample.describe_eip(region_id)
            if final_allocation_id:
                print(f"最終分配 ID：{final_allocation_id}")
            else:
                print("處理後沒有找到任何 EIP。")


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
```
