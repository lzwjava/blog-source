file="computer-organization"

ffmpeg -i "${file}.jpg" -vf "crop=854:480" "${file}_480p_cropped.jpg"

# ffmpeg -loop 1 -i "${file}.jpg" -i "${file}.mp3" -c:v libx264 -tune stillimage -c:a aac -b:a 192k -shortest "${file}.mp4"
