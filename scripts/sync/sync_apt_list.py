import os
import shutil

src_dir = "/etc/apt/sources.list.d/"
dst_dir = "scripts/apt-sources"

os.makedirs(dst_dir, exist_ok=True)

for filename in os.listdir(src_dir):
    src_file = os.path.join(src_dir, filename)
    dst_file = os.path.join(dst_dir, filename)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dst_file)
