from extract import extract_audio_streams
from fetch import fetch_youtube_page


video_url = "https://www.youtube.com/watch?v=JBSUgDxICg8&t=78s&ab_channel=PedroTech"

html = fetch_youtube_page(video_url)

audio_streams = extract_audio_streams(html)

