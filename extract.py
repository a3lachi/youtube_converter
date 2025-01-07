import re , json




# YouTube stores its stream URLs in a JSON-like format inside the page's HTML
def extract_audio_streams(html):
    if "ytInitialPlayerResponse" in html :
        match = re.search(r'ytInitialPlayerResponse\s*=\s*({.*?});', html)
        player_response = json.loads(match.group(1))
        try:
            streaming_data = player_response['streamingData']
            adaptive_formats = streaming_data.get('adaptiveFormats', [])
            
            # Extract audio-only streams
            audio_streams = [
                stream for stream in adaptive_formats
                if 'audio' in stream.get('mimeType', '')
            ]
            return audio_streams
        except KeyError as e:
            print(f"Error extracting audio streams: {e}")
            return None
    else :
        return None

