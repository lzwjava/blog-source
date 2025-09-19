import os


def count_notes():
    try:
        file_count = len(
            [f for f in os.listdir("notes") if os.path.isfile(os.path.join("notes", f))]
        )
        return file_count
    except FileNotFoundError:
        return 0


if __name__ == "__main__":
    print(count_notes())
