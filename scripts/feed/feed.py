import os
import argparse
from datetime import datetime
import pytz
from feedgen.feed import FeedGenerator

# Configuration
audio_dir = 'assets/audios/'
base_url = 'https://lzwjava.github.io/'
feed_file = 'audio_feed.xml'

# Set up argument parser
parser = argparse.ArgumentParser(description='Generate RSS feed for audio files.')
parser.add_argument('--lang', type=str, required=True, help='Language code to filter audio files (e.g., en, zh)')
args = parser.parse_args()

# List all MP3 files in the audio directory matching the specified language
audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3') and f.split('-')[-1].split('.')[0] == args.lang]

# Parse filenames and collect episodes
episodes = []
for audio_file in audio_files:
    parts = audio_file.split('-')
    date_str = '-'.join(parts[:3])  # Try to extract YYYY-MM-DD
    try:
        # Attempt to parse date from filename
        pub_date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        # If date parsing fails, use file modification time as fallback
        mod_time = os.path.getmtime(os.path.join(audio_dir, audio_file))
        pub_date = datetime.fromtimestamp(mod_time)
        print(f"No valid date in {audio_file}, using modification time: {pub_date}")
    
    # Make datetime timezone-aware
    pub_date = pub_date.replace(tzinfo=pytz.UTC)
    episodes.append((pub_date, audio_file))

# Sort episodes by publication date (newest first)
episodes.sort(key=lambda x: x[0], reverse=True)

# Initialize RSS feed
fg = FeedGenerator()
fg.id(base_url + 'podcast')
fg.title(f'My Audio Podcast - {args.lang.upper()}')
fg.author({'name': 'Lzwjava', 'email': 'lzwjava@example.com'})
fg.link(href=base_url, rel='alternate')
fg.language(args.lang)
fg.description(f'A podcast with audio episodes in {args.lang}')

# Language mapping for readable titles
lang_map = {
    'en': 'English',
    'zh': 'Chinese',
    'hant': 'Traditional Chinese',
    'hi': 'Hindi'
}

# Add episodes to feed
for pub_date, audio_file in episodes:  # Episodes are already sorted by pubdate desc
    name, _ = os.path.splitext(audio_file)
    parts = name.split('-')
    
    # Determine title and language
    if len(parts) >= 4 and '-' in '-'.join(parts[:3]):  # Has date format
        title_parts = parts[3:-1]
        lang = parts[-1]
    else:  # No date, assume last part is lang
        title_parts = parts[:-1]
        lang = parts[-1]
    
    title = ' '.join(title_parts).replace('-', ' ').title()
    episode_title = f"{title}"
    
    # Audio URL and size
    audio_url = base_url + audio_dir + audio_file
    audio_size = os.path.getsize(os.path.join(audio_dir, audio_file))
    
    # Create feed entry
    fe = fg.add_entry()
    fe.id(audio_url)
    fe.title(episode_title)
    fe.link(href=audio_url)
    fe.description(f'Episode: {title}')
    fe.enclosure(url=audio_url, length=str(audio_size), type='audio/mpeg')
    fe.published(pub_date)

# Generate RSS feed
fg.rss_file(feed_file, pretty=True)
print(f"RSS feed generated successfully at {feed_file} for language {args.lang}")