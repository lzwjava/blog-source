import argparse
import subprocess
import os


def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube videos at specified resolution."
    )
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "resolution",
        choices=["1080p", "720p", "480p"],
        default="720p",
        help="Video resolution to download (default: 720p)",
    )
    args = parser.parse_args()

    output_dir = "test"
    os.makedirs(output_dir, exist_ok=True)

    # Updated format strings to ensure best audio quality
    if args.resolution == "1080p":
        format_str = "bestvideo[height<=1080]+bestaudio"
    elif args.resolution == "720p":
        format_str = "bestvideo[height<=720]+bestaudio"
    else:  # 480p
        format_str = "bestvideo[height<=480]+bestaudio"

    command = [
        "yt-dlp",
        "--cookies-from-browser",
        "firefox",
        "-f",
        format_str,
        "-P",
        output_dir,
        args.url,
    ]

    subprocess.run(command)


if __name__ == "__main__":
    main()
