import subprocess
import argparse


def set_proxy(proxy_host, proxy_port):
    """Set HTTP and HTTPS proxy settings using gsettings."""
    try:
        # Set proxy mode to manual
        subprocess.run(
            ["gsettings", "set", "org.gnome.system.proxy", "mode", "manual"], check=True
        )
        # Set HTTP proxy
        subprocess.run(
            ["gsettings", "set", "org.gnome.system.proxy.http", "host", proxy_host],
            check=True,
        )
        subprocess.run(
            [
                "gsettings",
                "set",
                "org.gnome.system.proxy.http",
                "port",
                str(proxy_port),
            ],
            check=True,
        )
        # Set HTTPS proxy
        subprocess.run(
            ["gsettings", "set", "org.gnome.system.proxy.https", "host", proxy_host],
            check=True,
        )
        subprocess.run(
            [
                "gsettings",
                "set",
                "org.gnome.system.proxy.https",
                "port",
                str(proxy_port),
            ],
            check=True,
        )
        # Optionally, set no_proxy to bypass localhost
        subprocess.run(
            [
                "gsettings",
                "set",
                "org.gnome.system.proxy",
                "ignore-hosts",
                "['localhost', '127.0.0.1', '::1']",
            ],
            check=True,
        )
        print(f"Successfully set HTTP and HTTPS proxies to {proxy_host}:{proxy_port}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting proxy: {e}")


def unset_proxy():
    """Unset proxy settings by switching to 'none' mode."""
    try:
        subprocess.run(
            ["gsettings", "set", "org.gnome.system.proxy", "mode", "none"], check=True
        )
        print("Successfully unset HTTP and HTTPS proxies")
    except subprocess.CalledProcessError as e:
        print(f"Error unsetting proxy: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Manage HTTP and HTTPS proxy settings on Ubuntu"
    )
    parser.add_argument(
        "action", choices=["set", "unset"], help="Action to perform: set or unset proxy"
    )
    args = parser.parse_args()

    # Default proxy settings (modify as needed)
    proxy_host = "127.0.0.1"
    proxy_port = 7890

    if args.action == "set":
        set_proxy(proxy_host, proxy_port)
    else:
        unset_proxy()


if __name__ == "__main__":
    main()
