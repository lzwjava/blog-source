import os
import argparse
from PIL import Image


def images_to_gif(image_folder, output_gif, duration):
    # Load and sort image files
    images = []
    file_list = sorted(os.listdir(image_folder))

    for filename in file_list:
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            path = os.path.join(image_folder, filename)
            img = Image.open(path).convert("RGB")
            images.append(img)

    if not images:
        print("No images found in the folder.")
        return

    # Save the first image and append the rest
    images[0].save(
        output_gif, save_all=True, append_images=images[1:], duration=duration, loop=0
    )
    print(f"GIF saved as {output_gif}")


def main():
    parser = argparse.ArgumentParser(description="Convert images in a folder to a GIF.")
    parser.add_argument("image_folder", help="Path to the folder containing images")
    parser.add_argument("output_gif", help="Output GIF file path")
    parser.add_argument(
        "--duration", type=int, default=300, help="Frame duration in ms (default: 300)"
    )

    args = parser.parse_args()
    images_to_gif(args.image_folder, args.output_gif, args.duration)


if __name__ == "__main__":
    main()
