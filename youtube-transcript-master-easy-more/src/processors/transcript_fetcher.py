thonimport requests
import json
import logging

def fetch_transcripts(url):
    logging.info(f"Fetching transcript for {url}...")
    
    # Simulate transcript fetching
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}")

    transcript = {
        "text": "This is the extracted transcript text.",
        "json": [{"text": "Segment 1 text", "start": 0, "dur": 2}],
        "vtt": "WEBVTT\n00:00:00.000 --> 00:00:02.000\nSegment 1 text"
    }
    
    return transcript