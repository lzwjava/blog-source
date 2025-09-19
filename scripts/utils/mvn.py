import os
import argparse


def get_base_path_from_java_tool_options():
    java_tool_options = os.environ.get("JAVA_TOOL_OPTIONS", "")
    for option in java_tool_options.split():
        if option.startswith("-Duser.home="):
            return option.split("=")[1]
    return None


def compile_maven_projects(
    base_directory, log_directory="mvn_logs", maven_options=None
):
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)

        if os.path.isdir(item_path) and os.path.exists(
            os.path.join(item_path, "pom.xml")
        ):
            print(f"Compiling Maven project in: {item_path}")
            log_file_path = os.path.join(log_directory, f"{item}.log")

            pom_file_path = os.path.join(item_path, "pom.xml")
            mvn_command = ["mvn", "compile", "-f", pom_file_path, "-X"]
            if maven_options:
                mvn_command.extend(maven_options.split())

            # Normalize paths to forward slashes
            mvn_command = [path.replace("\\", "/") for path in mvn_command]
            mvn_command_str = " ".join(mvn_command)

            # Print the command that would be executed along with output redirection
            print(f"{mvn_command_str} > {log_file_path}")


def main():
    parser = argparse.ArgumentParser(description="Compile Maven projects.")
    parser.add_argument(
        "--project_name",
        type=str,
        default="projectname",
        help="The name of the project directory under user home.",
    )
    parser.add_argument(
        "--log_subdirectory",
        type=str,
        default="mvn_compile_logs",
        help="The subdirectory under user home to store compilation logs.",
    )
    parser.add_argument(
        "--maven_options",
        type=str,
        default="-Dversion=1.1",
        help="Maven options to pass to the compile command.",
    )

    args = parser.parse_args()

    base_path = get_base_path_from_java_tool_options()
    if base_path is None:
        print("JAVA_TOOL_OPTIONS environment variable does not contain user home path.")
        return

    # Use os.path.join to create paths with correct separators
    base_directory = os.path.join(base_path, args.project_name)
    log_directory = os.path.join(base_path, args.log_subdirectory)
    maven_options = args.maven_options

    compile_maven_projects(base_directory, log_directory, maven_options)


if __name__ == "__main__":
    main()
