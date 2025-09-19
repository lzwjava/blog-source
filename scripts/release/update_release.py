import subprocess
from ruamel.yaml import YAML
import os


def get_latest_commit_hash():
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=format:%H"], capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting latest commit hash: {e}")
        return None


def update_release_config(commit_hash):
    config_path = "_config.yml"
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)

    try:
        with open(config_path, "r") as file:
            config = yaml.load(file)

        if "release" in config:
            config["release"] = commit_hash
            with open(config_path, "w") as file:
                yaml.dump(config, file)
            print(f"Updated release to {commit_hash} in _config.yml")
        else:
            print("Could not find release in _config.yml")
    except Exception as e:
        print(f"Error updating _config.yml: {e}")


def main():
    commit_hash = get_latest_commit_hash()
    if commit_hash:
        update_release_config(commit_hash)


if __name__ == "__main__":
    main()
