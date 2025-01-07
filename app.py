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

video_url = "https://www.youtube.com/watch?v=JBSUgDxICg8&t=78s&ab_channel=PedroTech"

html = fetch_youtube_page(video_url)

if html:
    print("HTML fetched successfully!")

    # YouTube stores its stream URLs in a JSON-like format inside the page's HTML
    if "ytInitialPlayerResponse" in html :
        print("ytInitialPlayerResponse found")
    if "player_response" in html :
        print("player_response found")