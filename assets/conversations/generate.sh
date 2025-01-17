file="computer-organization"

ffmpeg -i "${file}.jpg" -vf "crop=854:480" "${file}_480p_cropped.jpg"


