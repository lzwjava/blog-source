---
audio: false
lang: zh
layout: post
title: 阿里云弹性IP管理
translated: true
---

该脚本提供了一个命令行界面来管理阿里云弹性公网IP (EIP)。它允许您使用阿里云Python SDK 创建、绑定、解绑和释放 EIP。该脚本接受要执行的任务和 EIP 的分配 ID 作为参数。

```bash
python aliyun_elastic_ip_manager.py unbind --allocation_id eip-j6c2olvsa7jk9l42iaaa
python aliyun_elastic_ip_manager.py bind --allocation_id eip-j6c7mhenamvy6zao3haaa
python aliyun_elastic_ip_manager.py release --allocation_id eip-j6c2olvsa7jk9l42aaa
```

```python
import logging
import os
import sys
from typing import List
import argparse

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
            logging.info(f"成功将 EIP {allocation_id} 绑定到实例 {instance_id}。结果：{result}")
            return True
        except Exception as error:
            logging.error(f"绑定 EIP {allocation_id} 到实例 {instance_id} 时出错：{error}")
            if hasattr(error, 'message'):
                logging.error(f"错误信息：{error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"建议：{error.data.get('Recommend')}")
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
            logging.info(f"成功将 EIP {allocation_id} 从实例 {instance_id} 解绑。结果：{result}")
            return True
        except Exception as error:
            logging.error(f"解绑 EIP {allocation_id} 从实例 {instance_id} 时出错：{error}")
            if hasattr(error, 'message'):
                logging.error(f"错误信息：{error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"建议：{error.data.get('Recommend')}")
            UtilClient.assert_as_string(str(error))
            return False

    @staticmethod
    def create_eip(
        region_id: str,
    ) -> str | None:
        client = Sample.create_client()
        allocate_eip_address_request = vpc_20160428_models.AllocateEipAddressRequest(
            region_id=region_id
        )
        runtime = util_models.RuntimeOptions(read_timeout=60000, connect_timeout=60000)
        try:
            result = client.allocate_eip_address_with_options(allocate_eip_address_request, runtime)
            print(result.body)
            allocation_id = result.body.allocation_id
            logging.info(f"成功创建 EIP。分配 ID：{allocation_id}")
            return allocation_id
        except Exception as error:
            logging.error(f"创建 EIP 时出错：{error}")
            if hasattr(error, 'message'):
                logging.error(f"错误信息：{error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"建议：{error.data.get('Recommend')}")
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
            logging.info(f"成功释放 EIP {allocation_id}。结果：{result}")
            return True
        except Exception as error:
            logging.error(f"释放 EIP {allocation_id} 时出错：{error}")
            if hasattr(error, 'message'):
                logging.error(f"错误信息：{error.message}")
            if hasattr(error, 'data') and error.data and error.data.get('Recommend'):
                logging.error(f"建议：{error.data.get('Recommend')}")
            UtilClient.assert_as_string(str(error))
            return False


    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        region_id = "cn-hongkong"
        instance_id = "i-j6c44l4zpphv7u7agdbk"

        parser = argparse.ArgumentParser(description='管理阿里云弹性公网IP。')
        parser.add_argument('job', choices=['create', 'bind', 'unbind', 'release'], help='要执行的操作：创建、绑定或解绑。')
        parser.add_argument('--allocation_id', type=str, help='EIP 的分配 ID。')
        parser.add_argument('--instance_id', type=str, default=instance_id, help='要绑定/解绑 EIP 的实例 ID。')

        parsed_args = parser.parse_args(args)

        if parsed_args.job == 'create':
            new_allocation_id = Sample.create_eip(region_id)
            if new_allocation_id:
                print(f"EIP 创建过程已成功启动。分配 ID：{new_allocation_id}")
            else:
                print("EIP 创建过程失败。")
        elif parsed_args.job == 'bind':
            if not parsed_args.allocation_id:
                print("错误：bind 操作需要 --allocation_id 参数。")
                return
            if Sample.bind_eip(region_id, parsed_args.allocation_id, parsed_args.instance_id):
                print(f"EIP 绑定过程已成功启动，EIP 为 {parsed_args.allocation_id}，实例为 {parsed_args.instance_id}。")
            else:
                print(f"EIP 绑定过程失败，EIP 为 {parsed_args.allocation_id}，实例为 {parsed_args.instance_id}。")
        elif parsed_args.job == 'unbind':
            if not parsed_args.allocation_id:
                print("错误：unbind 操作需要 --allocation_id 参数。")
                return
            if Sample.unbind_eip(region_id, parsed_args.allocation_id, parsed_args.instance_id):
                print(f"EIP 解绑过程已成功启动，EIP 为 {parsed_args.allocation_id}，实例为 {parsed_args.instance_id}。")
            else:
                print(f"EIP 解绑过程失败，EIP 为 {parsed_args.allocation_id}，实例为 {parsed_args.instance_id}。")
        elif parsed_args.job == 'release':
            if not parsed_args.allocation_id:
                print("错误：release 操作需要 --allocation_id 参数。")
                return
            if Sample.release_eip(parsed_args.allocation_id):
                 print(f"EIP 释放过程已成功启动，EIP 为 {parsed_args.allocation_id}。")
            else:
                print(f"EIP 释放过程失败，EIP 为 {parsed_args.allocation_id}。")


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
```
