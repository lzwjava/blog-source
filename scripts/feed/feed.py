import os
from datetime import datetime
from feedgen.feed import FeedGenerator

# Configuration
audio_dir = 'assets/audios/'  # Directory containing audio files
base_url = 'https://lzwjava.github.io/'  # Base URL of the Jekyll blog
feed_file = 'feed.xml'  # Output RSS feed file

# List all MP3 files in the audio directory
audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]

# Parse filenames to extract publication dates and sort episodes
episodes = []
for audio_file in audio_files:
    parts = audio_file.split('-')
    date_str = '-'.join(parts[:3])  # Extract YYYY-MM-DD
    try:
        pub_date = datetime.strptime(date_str, '%Y-%m-%d')
        episodes.append((pub_date, audio_file))
    except ValueError:
        print(f"Invalid date in filename: {audio_file}")
        continue

# Sort episodes by publication date in descending order (newest first)
episodes.sort(reverse=True, key=lambda x: x[0])

# Initialize the RSS feed
fg = FeedGenerator()
fg.id(base_url + 'podcast')  # Unique identifier for the podcast
fg.title('My Audio Podcast')  # Podcast title
fg.author({'name': 'Lzwjava', 'email': 'lzwjava@example.com'})  # Author info
fg.link(href=base_url, rel='alternate')  # Link to the blog
fg.language('en')  # Primary language of the podcast
fg.description('A podcast with various audio episodes')  # Podcast description

# Language code to full name mapping
lang_map = {
    'en': 'English',
    'zh': 'Chinese',
    'hant': 'Traditional Chinese',
    'hi': 'Hindi'
    # Add more language codes as needed
}

# Add each audio file as an episode to the feed
for pub_date, audio_file in episodes:
    # Parse filename components
    name, _ = os.path.splitext(audio_file)
    parts = name.split('-')
    title_parts = parts[3:-1]  # Title is between date and language
    title = ' '.join(title_parts).replace('-', ' ').title()  # Format title
    lang = parts[-1]  # Language code
    episode_title = f"{title} ({lang_map.get(lang, lang)})"  # e.g., "Bifocals (English)"
    
    # Construct audio URL and get file size
    audio_url = base_url + audio_dir + audio_file
    audio_size = os.path.getsize(os.path.join(audio_dir, audio_file))
    
    # Create feed entry
    fe = fg.add_entry()
    fe.id(audio_url)  # Unique ID (using audio URL)
    fe.title(episode_title)  # Episode title with language
    fe.link(href=audio_url)  # Link to the audio file
    fe.description('Description of the episode')  # Placeholder description
    fe.enclosure(url=audio_url, length=str(audio_size), type='audio/mpeg')  # Audio enclosure
    fe.pubdate(pub_date)  # Publication date

# Generate and save the RSS feed
fg.rss_file(feed_file, pretty=True)
print(f"RSS feed generated successfully at {feed_file}")