---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 偵錯 nmcli 語法陷阱
translated: true
type: note
---

是的，你說得完全正確——編程（特別是在處理 shell 命令、子進程或像 `nmcli` 這類工具時）確實充滿了這類吹毛求疵的語法陷阱。它們並非系統損壞或無法修復錯誤意義上的「錯誤」，而只是版本特定的怪癖或命令行界面中未文檔化的偏好設定，每個人在某個階段都曾被這些問題絆倒。工具不斷演進，文檔更新滯後，一個字母的差異（例如 `iface` 與 `ifname`）就足以讓一切停擺。這種情況雖然令人沮喪卻極為常見，而且一旦發現問題，解決方法通常都很直接明瞭。

從你分享的輸出內容來看，腳本在多個網絡上都遇到了這個確切問題：`nmcli` 拒絕接受 `iface` 作為有效參數（這很合理，因為在連接命令中指定接口名稱的官方標誌始終是 `ifname`）。你應用的更新——在第113行替換為 `ifname {interface}`——應該能乾淨俐落地解決問題。這個差異修正精確且影響範圍最小，因此不會有引入新副作用的風險。

### 快速測試建議
為了驗證修正效果而無需重新掃描全部35個網絡，你可以在 `test_wifi_connection` 函數中的 `subprocess.run` 調用後（約第114行處）暫時添加除錯輸出：

```python
result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
print(f"Debug: 已執行 '{cmd}' -> 返回碼: {result.returncode}, 標準輸出: '{result.stdout}', 標準錯誤: '{result.stderr}'")  # 添加此行
```

只需對一兩個SSID進行測試（例如臨時截取列表片段），此時應該顯示連接嘗試成功，或是揭示更具體的錯誤信息（例如認證失敗），而非參數錯誤的提示。

如果修正後仍遇到阻礙（例如在特定網絡如「HONG GOR 1」或顯示 `--` 的未命名網絡上），請將新輸出內容貼至此處——可能是密碼編碼問題、SSID中隱藏字符，甚至是硬件驅動程序的兼容性問題。我們可以據此繼續迭代調整。接下來執行結果如何？