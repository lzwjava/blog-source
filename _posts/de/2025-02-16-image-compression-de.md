---
audio: false
generated: true
image: false
lang: de
layout: post
title: Bildkomprimierung mit linearer Algebra
translated: true
type: note
---

Bildkompression ist eine grundlegende Aufgabe in der digitalen Bildverarbeitung, die darauf abzielt, die Speichergröße von Bildern zu reduzieren und gleichzeitig ihre visuelle Qualität zu erhalten. Eine leistungsstarke Methode, um dies zu erreichen, ist die Verwendung von linearer Algebra, insbesondere der Singulärwertzerlegung (SVD). Diese Technik ermöglicht es uns, eine Bildmatrix in einer kompakteren Form darzustellen, wodurch weniger wichtige Informationen effektiv verworfen werden, während die wesentlichen Merkmale erhalten bleiben.

Der folgende Python-Code demonstriert, wie ein Bild mit SVD komprimiert wird. Der Prozess umfasst die Zerlegung des Bildes in seine Bestandteile, die Komprimierung dieser Komponenten durch Beibehaltung nur einer Teilmenge der signifikantesten Merkmale und die anschließende Rekonstruktion des komprimierten Bildes. Dieser Ansatz kann sowohl auf Graustufen- als auch auf Farbbilder angewendet werden und bietet eine flexible und mathematisch fundierte Methode zur Reduzierung der Bildgröße.

```python
import numpy as np
from PIL import Image
import argparse
import os

def compress_image(image_path, compression_factor=0.1):
    # Öffne das Bild und konvertiere es in ein numpy-Array
    img = Image.open(image_path)
    img_array = np.array(img, dtype=float)

    # Prüfe, ob das Bild Graustufen oder Farbe ist
    if len(img_array.shape) == 2:  # Graustufenbild
        # Führe SVD auf dem Bild-Array durch
        U, S, Vt = np.linalg.svd(img_array, full_matrices=False)

        # Komprimiere das Bild, indem nur die obersten Singulärwerte behalten werden
        k = int(compression_factor * min(img_array.shape))
        S_compressed = np.diag(S[:k])
        U_compressed = U[:, :k]
        Vt_compressed = Vt[:k, :]

        # Rekonstruiere das komprimierte Bild
        img_compressed = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))
    else:  # Farbbild
        # Führe SVD für jeden Kanal separat durch
        img_compressed = np.zeros_like(img_array)
        for i in range(img_array.shape[2]):  # Iteriere über jeden Kanal
            channel = img_array[:, :, i]
            U, S, Vt = np.linalg.svd(channel, full_matrices=False)

            # Komprimiere den Kanal, indem nur die obersten Singulärwerte behalten werden
            k = int(compression_factor * min(channel.shape))
            S_compressed = np.diag(S[:k])
            U_compressed = U[:, :k]
            Vt_compressed = Vt[:k, :]

            # Rekonstruiere den komprimierten Kanal
            img_compressed[:, :, i] = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))

    # Begrenze die Werte auf den Bereich zwischen 0 und 255 und konvertiere zurück zu uint8
    img_compressed = np.clip(img_compressed, 0, 255).astype(np.uint8)

    # Generiere den Ausgabepfad durch Hinzufügen von '_compressed' zum ursprünglichen Dateinamen
    file_name, file_extension = os.path.splitext(image_path)
    output_path = f"{file_name}_compressed{file_extension}"

    # Speichere das komprimierte Bild
    compressed_img = Image.fromarray(img_compressed)
    compressed_img.save(output_path)

    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compress an image using SVD.")
    parser.add_argument("input_file", help="Path to the input image file")
    parser.add_argument("--compression_factor", type=float, default=0.1, help="Compression factor (default: 0.1)")
    args = parser.parse_args()

    output_file = compress_image(args.input_file, args.compression_factor)
    print(f"Compressed image saved as: {output_file}")

```