---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 自動化Clash代理管理
translated: true
type: post
---

本貼文詳細介紹了一個Python腳本`clash.py`，旨在**自動化管理您的Clash代理配置**。它涵蓋了從**定期下載更新的代理配置**和**重啟Clash服務**，到**智能選擇並切換至指定組內最快的可用代理**等所有功能。配合`clash.py`使用的`speed.py`模組，則負責**對各個Clash代理進行並行延遲測試**，確保您的連接始終通過最佳服務器路由。

## clash.py

```python
import os
import subprocess
import time
import shutil
import argparse
import logging
import requests
import json
import urllib.parse

# 假設speed.py位於同一目錄或可透過PYTHONPATH訪問
from speed import get_top_proxies 

# --- 配置 ---
CLASH_CONTROLLER_HOST = "127.0.0.1"
CLASH_CONTROLLER_PORT = 9090
CLASH_API_BASE_URL = f"http://{CLASH_CONTROLLER_HOST}:{CLASH_CONTROLLER_PORT}"
# 目標代理組名稱，最佳單一代理將被分配至此。
# 請確保此組存在於您的Clash配置中。
TARGET_PROXY_GROUP = "🚧Proxy" 

def setup_logging():
    """配置腳本的基本日誌記錄。"""
    logging.basicConfig(
        filename='clash.log', 
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def start_system_proxy(global_proxy_address):
    """設置系統範圍的代理環境變量。"""
    os.environ["GLOBAL_PROXY"] = global_proxy_address # 為一致性設置，如有需要可在其他地方使用
    os.environ["HTTP_PROXY"] = f"http://{global_proxy_address}"
    os.environ["HTTPS_PROXY"] = f"http://{global_proxy_address}"
    os.environ["http_proxy"] = f"http://{global_proxy_address}"
    os.environ["https_proxy"] = f"http://{global_proxy_address}"
    # 現代工具通常不需要明確設置為"false"，但保留以兼容原腳本意圖。
    os.environ["HTTP_PROXY_REQUEST_FULLURI"] = "false" 
    os.environ["HTTPS_PROXY_REQUEST_FULLURI"] = "false"
    os.environ["ALL_PROXY"] = os.environ["http_proxy"]
    logging.info(f"系統範圍代理設置為: {global_proxy_address}")

def stop_system_proxy():
    """清除系統範圍的代理環境變量。"""
    os.environ["http_proxy"] = ""
    os.environ["HTTP_PROXY"] = ""
    os.environ["https_proxy"] = ""
    os.environ["HTTPS_PROXY"] = ""
    os.environ["HTTP_PROXY_REQUEST_FULLURI"] = "true" # 恢復默認值
    os.environ["HTTPS_PROXY_REQUEST_FULLURI"] = "true"
    os.environ["ALL_PROXY"] = ""
    logging.info("系統範圍代理已停止（環境變量已清除）。")

def switch_clash_proxy_group(group_name, proxy_name):
    """
    將指定Clash代理組中的活動代理切換為新代理。
    """
    encoded_group_name = urllib.parse.quote(group_name)
    url = f"{CLASH_API_BASE_URL}/proxies/{encoded_group_name}"
    headers = {"Content-Type": "application/json"}
    payload = {"name": proxy_name}
    
    try:
        response = requests.put(url, headers=headers, data=json.dumps(payload), timeout=5)
        response.raise_for_status()
        logging.info(f"成功將'{group_name}'切換至'{proxy_name}'。")
        return True
    except requests.exceptions.ConnectionError:
        logging.error(f"錯誤：無法連接至Clash API於{CLASH_API_BASE_URL}以切換代理。")
        logging.error("請確保Clash正在運行且其external-controller已配置。")
        return False
    except requests.exceptions.Timeout:
        logging.error(f"錯誤：切換'{group_name}'代理時，連接Clash API超時。")
        return False
    except requests.exceptions.RequestException as e:
        logging.error(f"切換'{group_name}'代理時發生意外錯誤: {e}")
        return False

def main():
    """管理Clash配置、重啟及選擇最佳代理的主函數。"""
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Clash配置及管理腳本。")
    parser.add_argument("--minutes", type=int, default=10, help="更新間隔分鐘數（默認: 10）")
    parser.add_argument("--iterations", type=int, default=1000, help="迭代次數（默認: 1000）")
    parser.add_argument(
        "--config-url", 
        type=str, 
        default=os.getenv("CLASH_DOWNLOAD_URL"),
        help="下載Clash配置的URL。若設置了CLASH_DOWNLOAD_URL環境變量則使用該值，否則使用硬編碼URL。"
    )
    args = parser.parse_args()

    ITERATIONS = args.iterations
    SLEEP_SECONDS = args.minutes * 60
    config_download_url = args.config_url

    if not config_download_url:
        logging.critical("錯誤：未提供配置下載URL。請設置CLASH_DOWNLOAD_URL環境變量或使用--config-url參數。")
        return # 無可用URL時退出

    clash_executable_path = "/home/lzw/clash-linux-386-v1.17.0/clash-linux-386"
    clash_config_dir = os.path.expanduser("~/.config/clash")
    clash_config_path = os.path.join(clash_config_dir, "config.yaml")

    for i in range(1, ITERATIONS + 1):
        logging.info(f"--- 開始第{i}次迭代，共{ITERATIONS}次 ---")

        # 步驟1：停止任何現有的系統代理設置
        stop_system_proxy()
        
        # 步驟2：下載並更新Clash配置
        try:
            logging.info(f"從以下位置下載新配置: {config_download_url}")
            subprocess.run(["wget", config_download_url, "-O", "zhs4.yaml"], check=True, capture_output=True)
            os.makedirs(clash_config_dir, exist_ok=True)
            shutil.move("zhs4.yaml", clash_config_path)
            logging.info("Clash配置更新成功！")
        except subprocess.CalledProcessError as e:
            logging.error(f"下載或移動配置文件失敗: {e.stderr.decode().strip()}")
            logging.error("跳過至下一次迭代。")
            time.sleep(10) # 重試前稍等
            continue
        except Exception as e:
            logging.error(f"配置更新期間發生意外錯誤: {e}")
            logging.error("跳過至下一次迭代。")
            time.sleep(10)
            continue

        # 步驟3：在後台啟動Clash
        clash_process = None
        try:
            # 確保Clash啟動時啟用了external-controller並可訪問
            # 這通常在config.yaml本身中配置。
            clash_process = subprocess.Popen([clash_executable_path], 
                                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logging.info(f"Clash已啟動，PID為{clash_process.pid}")
            # 給Clash一點時間完全初始化並打開其API端口
            time.sleep(5) 
        except FileNotFoundError:
            logging.critical(f"未找到Clash可執行文件於: {clash_executable_path}")
            logging.critical("請確保路徑正確且已安裝Clash。")
            return # 嚴重錯誤，退出腳本
        except Exception as e:
            logging.error(f"啟動Clash失敗: {e}")
            logging.error("跳過至下一次迭代。")
            if clash_process: clash_process.terminate()
            time.sleep(10)
            continue

        # 步驟4：測試代理速度並選擇最佳代理
        best_proxy_name = None
        try:
            logging.info("測試代理速度以尋找最佳代理...")
            top_proxies = get_top_proxies(num_results=1) # 僅獲取單一最佳代理
            if top_proxies:
                best_proxy_name = top_proxies[0]['name']
                logging.info(f"識別到最佳代理: '{best_proxy_name}'，延遲{top_proxies[0]['latency']}ms")
            else:
                logging.warning("無成功代理測試。無法為此次迭代選擇最佳代理。")
        except Exception as e:
            logging.error(f"代理速度測試期間發生錯誤: {e}")

        # 步驟5：將Clash的代理組切換至最佳代理（如找到）
        if best_proxy_name:
            # 在設置系統代理前，確保Clash正確設置。
            # 將系統範圍代理設置為指向Clash的本地HTTP代理。
            # Clash通常在其HTTP代理上運行於端口7890（或類似，請檢查您的配置）。
            clash_local_proxy_address = f"{CLASH_CONTROLLER_HOST}:7890" # 如果您的Clash HTTP端口不同，請調整
            start_system_proxy(clash_local_proxy_address)
            
            if not switch_clash_proxy_group(TARGET_PROXY_GROUP, best_proxy_name):
                logging.error(f"無法將Clash組'{TARGET_PROXY_GROUP}'切換至'{best_proxy_name}'。")
        else:
            logging.warning("未找到最佳代理，此次迭代跳過代理組切換及系統代理設置。")
            
        # 步驟6：等待指定時長
        logging.info(f"等待{SLEEP_SECONDS / 60}分鐘後進行下一次迭代...")
        time.sleep(SLEEP_SECONDS)

        # 步驟7：停止Clash進程
        if clash_process:
            logging.info("終止Clash進程...")
            clash_process.terminate()
            try:
                clash_process.wait(timeout=10) # 給Clash更多時間優雅關閉
                logging.info("Clash已成功停止。")
            except subprocess.TimeoutExpired:
                logging.warning("Clash未優雅終止，殺死進程。")
                clash_process.kill()
                clash_process.wait() # 確保進程完全終止
            except Exception as e:
                logging.error(f"等待Clash停止時發生錯誤: {e}")
        
        logging.info(f"--- 第{i}次迭代完成 ---")

    logging.info(f"已完成{ITERATIONS}次迭代。腳本結束。")

if __name__ == "__main__":
    main()
```

## speed.py

```python
import requests
import json
import urllib.parse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging # 導入日誌模組

# --- 配置 ---
CLASH_CONTROLLER_HOST = "127.0.0.1"  # 使用127.0.0.1，因為控制器位於同一機器上
CLASH_CONTROLLER_PORT = 9090
CLASH_API_BASE_URL = f"http://{CLASH_CONTROLLER_HOST}:{CLASH_CONTROLLER_PORT}"
LATENCY_TEST_URL = "https://github.com" # 更新測試URL
LATENCY_TEST_TIMEOUT_MS = 5000  # 毫秒
CONCURRENT_CONNECTIONS = 10 # 並行測試數量

# 已知的代理組名稱列表，排除於速度測試之外
# 這些通常不是單一節點，而是策略組或特殊代理。
EXCLUDE_PROXY_GROUPS = [
    "DIRECT",
    "REJECT",
    "GLOBAL", # 默認已在API中排除
    "🇨🇳國內網站或資源",
    "🌵其它規則外",
    "🎬Netflix等國外流媒體",
    "📦ChatGPT",
    "📹Youtube",
    "📺愛奇藝等國內流媒體",
    "🚧Proxy",
    # 添加您想排除的其他組名
]

# --- speed.py的日誌設置 ---
# 為此特定腳本配置日誌
# 這確保當speed.py被導入且其函數被調用時，
# 其輸出會寫入speed.log，與clash_manager.log分開。
logging.basicConfig(
    filename='clash.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# 可選地，如果您還想在控制台看到輸出，添加StreamHandler:
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# console_handler.setFormatter(formatter)
# logging.getLogger().addHandler(console_handler)

# --- 腳本邏輯 ---

def get_all_proxy_names():
    """從Clash API獲取所有代理名稱，排除已知組。"""
    try:
        response = requests.get(f"{CLASH_API_BASE_URL}/proxies", timeout=5)
        response.raise_for_status()  # 對於HTTP錯誤（4xx或5xx）引發異常
        proxies_data = response.json()
        
        all_names = proxies_data.get("proxies", {}).keys()
        
        # 過濾組名
        filtered_names = [name for name in all_names if name not in EXCLUDE_PROXY_GROUPS]
        
        logging.info(f"成功獲取{len(filtered_names)}個可測試代理名稱。")
        return filtered_names
    except requests.exceptions.ConnectionError:
        logging.error(f"無法連接至Clash API於{CLASH_API_BASE_URL}。請確保Clash正在運行。")
        return []
    except requests.exceptions.Timeout:
        logging.error(f"連接Clash API超時，超過5秒。")
        return []
    except requests.exceptions.RequestException as e:
        logging.error(f"獲取代理名稱時發生意外錯誤: {e}")
        return []

def test_proxy_latency(proxy_name):
    """使用Clash API測試單一代理的延遲。
    返回元組(proxy_name, latency)或失敗時返回(proxy_name, None)。
    """
    encoded_proxy_name = urllib.parse.quote(proxy_name)
    url = f"{CLASH_API_BASE_URL}/proxies/{encoded_proxy_name}/delay"
    params = {
        "url": LATENCY_TEST_URL,
        "timeout": LATENCY_TEST_TIMEOUT_MS
    }
    try:
        # requests超時以秒為單位，轉換毫秒
        response = requests.get(url, params=params, timeout=(LATENCY_TEST_TIMEOUT_MS / 1000) + 1)
        response.raise_for_status()
        latency_data = response.json()
        latency = latency_data.get("delay")
        logging.info(f"代理: {proxy_name} - 延遲: {latency}ms")
        return proxy_name, latency
    except requests.exceptions.RequestException as e:
        logging.warning(f"測試'{proxy_name}'時錯誤: {e}")
        return proxy_name, None

def get_top_proxies(num_results=5):
    """
    並行測試Clash代理速度並返回前N個最快的單一代理。

    返回:
        list: 字典列表，每個包含'top'代理的'name'和'latency'。
              如果未找到可測試代理或發生錯誤，返回空列表。
    """
    logging.info("開始通過External Controller API進行Clash代理速度測試（並行）...")
    logging.info(f"使用測試URL: {LATENCY_TEST_URL}")
    logging.info(f"同時運行{CONCURRENT_CONNECTIONS}次測試。這可能需要一些時間...")

    proxy_names_to_test = get_all_proxy_names()
    if not proxy_names_to_test:
        logging.warning("未找到可測試代理或獲取代理名稱時發生錯誤。")
        return []

    logging.info(f"找到{len(proxy_names_to_test)}個單一代理進行測試。")

    proxy_latencies = {}
    
    with ThreadPoolExecutor(max_workers=CONCURRENT_CONNECTIONS) as executor:
        future_to_proxy = {executor.submit(test_proxy_latency, name): name for name in proxy_names_to_test}

        for future in as_completed(future_to_proxy):
            proxy_name = future_to_proxy[future]
            try:
                name, latency = future.result()
                if latency is not None:
                    proxy_latencies[name] = latency
                else:
                    logging.info(f"代理: {name} - 測試失敗或超時（詳見警告日誌）")
            except Exception as exc:
                logging.error(f"代理{proxy_name}在測試期間產生意外異常: {exc}")

    sorted_proxies = sorted([item for item in proxy_latencies.items() if item[1] is not None], 
                            key=lambda item: item[1])

    top_proxies_list = []
    if not sorted_proxies:
        logging.warning("未完成任何成功的單一代理測試。")
    else:
        logging.info(f"--- 前{num_results}個最快單一代理 ---")
        for i, (name, latency) in enumerate(sorted_proxies[:num_results]):
            top_proxies_list.append({"name": name, "latency": latency})
            logging.info(f"  {i+1}. {name}: {latency}ms")
        logging.info(f"速度測試完成。已識別前{num_results}個代理。")
            
    return top_proxies_list

if __name__ == "__main__":
    # 當speed.py直接運行時，仍會輸出至speed.log
    # 並打印至控制台（如console_handler未被註釋）。
    top_5_proxies = get_top_proxies(num_results=5)
    print("\n函數返回的前5個代理:", top_5_proxies)
```