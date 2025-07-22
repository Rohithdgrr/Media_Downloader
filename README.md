# Media_Downloader
Most simple and user-friendly media downloader of platforms (YouTube , Instagram , Twitter X , Reddit , Facebook) and more .


Project Structure
youtube_downloader/
├── src/
│   └── downloader.py     # Main script with download functionality
├── docs/
│   └── usage.md          # Detailed usage instructions
├── requirements.txt       # Project dependencies
└── README.md             # Project overview

Prerequisites
Python 3.8+
FFmpeg installed and added to system PATH

Installation
Clone the repository:git clone https://github.com/yourusername/youtube_downloader.git
cd youtube_downloader

Install dependencies:pip install -r requirements.txt
Ensure FFmpeg is installed:
Windows: Download from FFmpeg website and add to PATH
macOS: brew install ffmpeg
Linux: sudo apt-get install ffmpeg (Ubuntu/Debian) or equivalent



Usage
Run the script and follow the prompts:
python src/downloader.py

Options
List available formats for the video
Download video in 8K (4320p)
Download video in 4K (2160p)
Download video in 1080p
Download video in 720p
Download video in 480p
Download audio as MP3

Dependencies
yt-dlp: Python library for downloading YouTube content
FFmpeg: Required for merging video/audio and MP3 conversion

Contributing
Fork the repository
Create a feature branch (git checkout -b feature/new-feature)
Commit changes (git commit -m 'Add new feature')
Push to the branch (git push origin feature/new-feature)
Create a Pull Request

