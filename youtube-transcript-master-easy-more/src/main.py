thonimport os
import json
from processors.transcript_fetcher import fetch_transcripts
from processors.metadata_parser import parse_metadata
from processors.format_converter import convert_format
from utils.http_client import get_http_client
from utils.retry_handler import retry_request
from utils.url_resolver import resolve_url
from outputs.dataset_writer import write_to_output
import logging

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Starting YouTube Transcript Master...")

    # Load settings
    settings_file = os.path.join(os.path.dirname(__file__), 'config/settings.example.json')
    with open(settings_file) as f:
        settings = json.load(f)

    # Example video URLs
    video_urls = settings.get("video_urls", [])

    # Fetch transcripts and metadata
    for url in video_urls:
        try:
            resolved_url = resolve_url(url)
            transcript_data = fetch_transcripts(resolved_url)
            metadata = parse_metadata(resolved_url)

            # Convert formats
            formatted_data = convert_format(transcript_data, settings["output_format"])

            # Write to output
            write_to_output(formatted_data, settings["output_directory"])

        except Exception as e:
            logging.error(f"Error processing {url}: {str(e)}")

if __name__ == "__main__":
    main()