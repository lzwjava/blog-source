from google.cloud import texttospeech


def text_to_speech(text, output_filename):
    # Initialize the Text-to-Speech client
    client = texttospeech.TextToSpeechClient()

    # Set up the synthesis input
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Choose the voice parameters, using 'en-US-Journey-D'
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # English (United States)
        name="en-US-Journey-F",  # Specific voice name (Journey voice model)
    )

    # Set audio configuration as per provided parameters, with MP3 encoding
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,  # Output format: MP3
        # Optimized for small Bluetooth speakers
        effects_profile_id=["small-bluetooth-speaker-class-device"],
        pitch=0.0,  # No pitch modification
        speaking_rate=0.0,  # Slow speech rate (adjust as needed)
        volume_gain_db=5.0,  # Louder volume (can be adjusted)
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Write the output audio to a file
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)

    print(f"Audio content written to {output_filename}")


# Example usage
article_text = """
Movies, oh my gosh, I just just absolutely love them. They're like time machines taking you to different worlds and landscapes, and um, and I just can't get enough of it.
"""
output_file = "output_audio.mp3"  # MP3 format

# Call the function
text_to_speech(article_text, output_file)
