import os
import datetime

today = datetime.date.today()
date_str = today.strftime("%Y-%m-%d")

pages_dir = "pages"

for filename in os.listdir(pages_dir):
    if filename.endswith(".md"):
        old_path = os.path.join(pages_dir, filename)
        new_filename = f"{date_str}-{filename}"
        new_path = os.path.join(pages_dir, new_filename)
        os.rename(old_path, new_path)
