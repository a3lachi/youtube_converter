import os
import requests

def select_best_audio_stream(audio_streams):
    # Sort streams by bitrate (highest first)
    sorted_streams = sorted(audio_streams, key=lambda x: x.get('bitrate', 0), reverse=True)
    # Return the best stream (first in the sorted list)
    return sorted_streams[0] if sorted_streams else None


def decrypt_signature(cipher, player_script_url):
    # Placeholder: Implement this step if `signatureCipher` is present
    # We'll need to fetch the player script and reverse-engineer the signature decryption logic
    raise NotImplementedError("Decryption logic for ciphered signatures is not yet implemented.")



def get_audio_url(stream, player_script_url=None):
    if 'url' in stream:
        return stream['url']
    elif 'signatureCipher' in stream:
        cipher_data = dict(kv.split('=') for kv in stream['signatureCipher'].split('&'))
        url = requests.utils.unquote(cipher_data['url'])
        signature = requests.utils.unquote(cipher_data['s'])
        if player_script_url:
            decrypted_signature = decrypt_signature(signature, player_script_url)
            return f"{url}&sig={decrypted_signature}"
        else:
            raise ValueError("Player script URL is required for decryption.")
    else:
        raise ValueError("No valid URL found for this stream.")

def download_audio(audio_url, output_path):
    """Download the audio stream to a temporary file."""
    response = requests.get(audio_url, stream=True)
    temp_file = output_path + ".temp"
    with open(temp_file, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    return temp_file

