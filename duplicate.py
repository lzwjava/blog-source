import os

# Directory containing markdown files
posts_dir = "_posts"

# Extract article names and check for duplicates


def extract_article_names_with_threshold(directory, threshold=3):
    article_name_count = {}
    duplicates = []

    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            # Extract the article name
            article_name = filename.split("-")[3]
            if article_name in article_name_count:
                article_name_count[article_name] += 1
            else:
                article_name_count[article_name] = 1

    for article_name, count in article_name_count.items():
        if count > threshold:
            duplicates.append(article_name)

    return set(article_name_count.keys()), set(duplicates)


# Get article names and duplicates with a threshold of more than 4
article_names, duplicates = extract_article_names_with_threshold(posts_dir)

print("Unique Article Names:", article_names)
print("Duplicate Article Names:", duplicates)
