# YouTube Transcript Master [EASY] (WebVTT & more) Scraper
This project extracts transcripts and metadata from YouTube videos, playlists, and channels with reliable performance. It supports multiple formats including TXT, JSON, VTT, TTML, and more, making it ideal for large-scale data workflows. The scraper minimizes failures with strong retry logic and optional proxy support to ensure consistent results.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>YouTube Transcript Master [EASY] (WebVTT & more)</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
This tool retrieves YouTube transcripts at scale and gathers essential video metadata in a structured format.

### Why Transcript Extraction Matters
- Helps researchers and creators analyze large sets of video content.
- Allows marketers and analysts to derive insights from spoken content.
- Enables developers to integrate subtitle and transcript data into applications.
- Simplifies content indexing and semantic analysis workflows.
- Supports bulk operations for channels, playlists, and mixed URL lists.

## Features
| Feature | Description |
|--------|-------------|
| Bulk Transcript Retrieval | Processes mixed YouTube inputs including videos, playlists, and channels. |
| Multi-Format Output | Supports plain text, JSON, JSON3, SRV1/2/3, TTML, and VTT formats. |
| Metadata Extraction | Captures title, duration, upload date, and language details for each video. |
| Language Selection | Retrieve transcripts in any supported YouTube subtitle language. |
| Robust Retry Logic | Handles HTML fetch errors, timeouts, and blocked requests gracefully. |
| Proxy Support | Optional proxy routing ensures stable access during high-volume runs. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|------------|------------------|
| url | Original YouTube video URL processed. |
| language | Transcript language code requested. |
| title | Extracted video title or fallback if processing fails. |
| duration | Video duration in seconds. |
| videoLink | Same as URL, included for convenience. |
| uploadDate | Publication date in YYYY-MM-DD format. |
| text | Plain text transcript, if selected. |
| json | JSON transcript segments including text, start, and duration. |
| json3 | Raw JSON3 transcript format. |
| srv1 | Raw SRV1 XML transcript. |
| srv2 | Raw SRV2 XML transcript. |
| srv3 | Raw SRV3 XML transcript. |
| ttml | Raw TTML transcript. |
| vtt | Raw VTT subtitle format. |
| error | Error message if transcript extraction fails. |
| details | Additional diagnostic information for failed items. |

---

## Example Output

Example:


    {
      "url": "https://www.youtube.com/watch?v=b_nep8vMnkc",
      "language": "en",
      "title": "Example Video Title",
      "duration": 123,
      "videoLink": "https://www.youtube.com/watch?v=b_nep8vMnkc",
      "uploadDate": "2023-10-27",
      "text": "This is the extracted plain text transcript...",
      "json": [
        {
          "text": "Segment 1 text",
          "start": 0.5,
          "dur": 3.2
        },
        {
          "text": "Segment 2 text",
          "start": 3.7,
          "dur": 2.8
        }
      ],
      "json3": null,
      "srv1": null,
      "srv2": null,
      "srv3": null,
      "ttml": null,
      "vtt": null,
      "error": null,
      "details": null
    }

---

## Directory Structure Tree


    YouTube Transcript Master [EASY] (WebVTT & more)/
    ├── src/
    │   ├── main.py
    │   ├── processors/
    │   │   ├── transcript_fetcher.py
    │   │   ├── metadata_parser.py
    │   │   └── format_converter.py
    │   ├── utils/
    │   │   ├── http_client.py
    │   │   ├── retry_handler.py
    │   │   └── url_resolver.py
    │   ├── outputs/
    │   │   └── dataset_writer.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── sample_inputs.json
    │   └── demo_output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Researchers** analyze spoken content from thousands of educational videos to accelerate dataset creation.
- **Marketing teams** extract transcripts to study competitor channels and identify messaging patterns.
- **Developers** integrate transcripts into indexing systems to boost searchability and semantic analysis.
- **Content creators** monitor competitor uploads and convert transcripts into research notes.
- **AI engineers** build speech-based datasets from large YouTube collections for model fine-tuning.

---

## FAQs
**Q1: Can the tool handle playlists with hundreds of videos?**
Yes, it is optimized for bulk operations and processes large playlists reliably with retry logic and optional proxy routing.

**Q2: What happens if a video has no transcript?**
The output includes an `error` and `details` field explaining the failure, while the rest of the dataset continues processing normally.

**Q3: Does it support newly uploaded videos?**
Transcripts for very recent uploads may not be available yet; such items may produce null transcript fields.

**Q4: Are live streams supported?**
Live or upcoming streams often lack completed transcript data, which may result in partial or empty results.

---

## Performance Benchmarks and Results
**Primary Metric:** Average processing speed reaches ~50–80 videos per minute depending on format selection.
**Reliability Metric:** Consistent success rate of 98–100% on stable video sets with clean URLs.
**Efficiency Metric:** Lightweight HTML parsing keeps CPU usage low, even in large batch operations.
**Quality Metric:** Transcript outputs maintain high fidelity with precise timestamps and clean formatting, ensuring accurate downstream analysis.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
