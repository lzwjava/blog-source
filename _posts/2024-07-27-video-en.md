---
layout: post
title: "Automating Video Annotation with OCR and LLM"
---

*This blog post was written with the assistance of ChatGPT-4o.*

---

To create a system that uses a language model to generate annotations based on the text extracted from a video screen, you can follow these steps:

1. **Extract Frames from Video**: Use a library to capture frames from the video.
2. **Extract Text from Frames**: Use Optical Character Recognition (OCR) to extract text from each frame.
3. **Generate Annotations**: Use a language model to generate annotations based on the extracted text.
4. **Overlay Annotations on Video**: Add the generated annotations back onto the video frames.

Here is a simplified example in Python using OpenCV for video processing, Tesseract for OCR, and the OpenAI GPT-3 model for generating annotations:

### Prerequisites

1. **Install the required libraries**:
   ```sh
   pip install opencv-python pytesseract openai
   ```

2. **Tesseract Installation**: Ensure Tesseract OCR is installed on your system. You can download it from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

3. **OpenAI API Key**: You need an OpenAI API key to use the GPT-3 model. You can get it from [OpenAI](https://beta.openai.com/signup/).

### Step-by-Step Code

#### 1. Extract Frames from Video

```python
import cv2

def extract_frames(video_path, frame_rate):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    frames = []

    while success:
        if count % frame_rate == 0:
            frames.append(image)
        success, image = vidcap.read()
        count += 1

    vidcap.release()
    return frames

video_path = 'path/to/video.mp4'
frame_rate = 30  # Extract one frame every 30 frames
frames = extract_frames(video_path, frame_rate)
```

#### 2. Extract Text from Frames

```python
import pytesseract

def extract_text_from_frames(frames):
    text_data = []
    for frame in frames:
        text = pytesseract.image_to_string(frame)
        text_data.append(text)
    return text_data

text_data = extract_text_from_frames(frames)
```

#### 3. Generate Annotations

```python
import openai

openai.api_key = 'your_openai_api_key'

def generate_annotations(text_data):
    annotations = []
    for text in text_data:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate annotation for the following text extracted from a video frame:\n\n{text}\n\nAnnotation:",
            max_tokens=50
        )
        annotation = response.choices[0].text.strip()
        annotations.append(annotation)
    return annotations

annotations = generate_annotations(text_data)
```

#### 4. Overlay Annotations on Video

```python
def overlay_annotations_on_frames(frames, annotations):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_color = (0, 255, 0)
    line_type = 2

    annotated_frames = []
    for i, frame in enumerate(frames):
        annotation = annotations[i]
        annotated_frame = cv2.putText(frame.copy(), annotation, (10, 30), font, font_scale, font_color, line_type)
        annotated_frames.append(annotated_frame)
    
    return annotated_frames

annotated_frames = overlay_annotations_on_frames(frames, annotations)
```

#### 5. Save the Annotated Video

```python
def save_annotated_video(annotated_frames, output_path, original_video_path, frame_rate):
    vidcap = cv2.VideoCapture(original_video_path)
    frame_width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    vidcap.release()

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (frame_width, frame_height))

    for frame in annotated_frames:
        out.write(frame)
    
    out.release()

output_path = 'path/to/annotated_video.mp4'
save_annotated_video(annotated_frames, output_path, video_path, frame_rate)
```

### Explanation

1. **Extract Frames**: `extract_frames` function captures frames from the video at the specified frame rate.
2. **Extract Text**: `extract_text_from_frames` function uses Tesseract to perform OCR on each frame to extract text.
3. **Generate Annotations**: `generate_annotations` function uses OpenAI GPT-3 to generate annotations for each extracted text.
4. **Overlay Annotations**: `overlay_annotations_on_frames` function overlays the generated annotations onto the video frames.
5. **Save Annotated Video**: `save_annotated_video` function saves the annotated frames back into a video file.

This code is a basic example and might need adjustments based on the specific requirements and video characteristics. Also, consider optimizing the frame extraction and annotation generation process for large videos.