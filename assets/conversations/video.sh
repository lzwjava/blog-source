file="$1"

ffmpeg -loop 1 -i "${file}.jpg" -i "${file}.mp3" -c:v libx264 -tune stillimage -c:a aac -b:a 192k -shortest "$HOME/Downloads/${file}.mp4"