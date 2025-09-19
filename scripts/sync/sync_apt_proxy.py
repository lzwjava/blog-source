import shutil
import os

src = "/etc/apt/apt.conf.d/proxy.conf"
dst_dir = "scripts/config"
os.makedirs(dst_dir, exist_ok=True)
dst = os.path.join(dst_dir, "proxy.conf")

shutil.copy2(src, dst)
print(f"Copied {src} to {dst}")
