---
audio: false
generated: true
lang: hant
layout: post
title: 函數計算與 OSS 整合
translated: true
---

此程式碼示範如何整合阿里雲函數計算與 OSS (對象儲存服務)。它從指定的網址下載檔案，並將其上傳到 OSS 存儲桶。

## 程式碼

```python
# -*- coding: utf-8 -*-
import oss2
import requests
import logging
import os

def handler(event, context):
    # 設定
    # model_url = "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

    model_url = "https://storage.googleapis.com/lzwjava1/ss_urls.txt"
    oss_bucket_name = "lzw-download"  # 您的儲存桶名稱
    oss_endpoint = "oss-cn-hangzhou.aliyuncs.com"  # 公共端點
    
    try:
        # 使用提供的角色 ARN 建立身份驗證物件
        role_arn = "acs:ram::1768386076294612:role/fc"
        auth = oss2.Auth(
            os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        
        sts_auth = oss2.StsAuth(
            os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'],
            os.environ['ALIBABA_CLOUD_SECURITY_TOKEN']
        )

        # 2. 使用正確的端點初始化 OSS 客戶端
        bucket = oss2.Bucket(
            sts_auth,
            oss_endpoint,
            oss_bucket_name
        )

        # 3. 串流下載和上傳
        logging.info("開始下載...")
        with requests.get(model_url, stream=True) as response:
            response.raise_for_status()
            
            # 上傳到 OSS
            result = bucket.put_object(
                'models/mistral-7b-instruct-v0.2.Q4_K_M.gguf',
                response.iter_content(chunk_size=1024*1024)
            )
            
        if result.status == 200:
            logging.info("上傳成功!")
            return "成功"
        else:
            raise Exception(f"OSS 上傳失敗: {result.status}")

    except Exception as e:
        logging.error(f"錯誤: {str(e)}")
        raise e
```

## 錯誤

我們遇到與之前相同的錯誤。看來需要 VPN 才能完成此任務。

> 2025-01-24 17:43:342025-01-24 17:43:34 1-679360a6-154b432a-15cadcce0c27 [錯誤] {
>    "errorMessage": "HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f7d3c289f60>: Failed to establish a new connection: [Errno 101] Network is unreachable'))"


