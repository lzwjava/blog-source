import speedtest
import webbrowser
import time
from datetime import datetime


def run_speed_test():
    print("Running internet speed test...")
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")
    return download_speed, upload_speed, ping


def test_tiktok_loading_time():
    print("\nTesting TikTok loading time...")
    start_time = time.time()
    webbrowser.open("https://www.tiktok.com")
    end_time = time.time()

    loading_time = end_time - start_time
    print(f"TikTok loading time: {loading_time:.2f} seconds")
    return loading_time


def main():
    print("Starting TikTok Speed Test")
    print("Timestamp:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 40)

    # Run internet speed test
    download_speed, upload_speed, ping = run_speed_test()

    # Test TikTok loading time
    loading_time = test_tiktok_loading_time()

    # Summarize results to use the variables
    print("\nSummary of Results:")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")
    print(f"TikTok Loading Time: {loading_time:.2f} seconds")

    print("\nTest Complete!")
    print("-" * 40)


if __name__ == "__main__":
    main()
