import os
import frontmatter

posts_dir = "_posts"

for filename in os.listdir(posts_dir):
    if filename.endswith("-en.md") or filename.endswith("-zh.md"):
        filepath = os.path.join(posts_dir, filename)
        try:
            # Determine lang based on filename
            if filename.endswith("-en.md"):
                lang = "en"
            elif filename.endswith("-zh.md"):
                lang = "zh"
            # Read the file content as string
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            # Load the post from the content string
            post = frontmatter.loads(content)
            # Set lang in metadata
            post["lang"] = lang
            # Dump the post back to a string
            updated_content = frontmatter.dumps(post)
            # Write the updated content back to the file
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Updated {filepath}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
