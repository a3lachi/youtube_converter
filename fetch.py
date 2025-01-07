import http.client

def fetch_youtube_page(video_url):
    # Extract the hostname and path from the URL
    hostname = "www.youtube.com"
    path = video_url.replace("https://www.youtube.com", "")
    
    # Open a connection to YouTube
    conn = http.client.HTTPSConnection(hostname)
    conn.request("GET", path, headers={"User-Agent": "Mozilla/5.0"})
    
    # Get the response
    response = conn.getresponse()
    if response.status == 200:
        html = response.read().decode('utf-8')
        return html
    else:
        print(f"Failed to fetch page. Status: {response.status}")
        return None

