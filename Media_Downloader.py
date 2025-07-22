import yt_dlp

def list_available_formats(video_url: str) -> None:
    """Display available video and audio formats for a given YouTube URL.
    """
    ydl_options = {}
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(video_url, download=False)
        print("\nAvailable formats:")
        for format_info in info['formats']:
            print(f"{format_info['format_id']}: {format_info['ext']} - "
                  f"{format_info.get('resolution', 'audio only')} - "
                  f"vcodec: {format_info.get('vcodec', 'N/A')} - "
                  f"acodec: {format_info.get('acodec', 'N/A')}")
        print(f"\nVideo title: {info.get('title', 'N/A')}")

def download_video(video_url: str, max_resolution: int = 4320) -> None:
    """Download a video with a specified maximum resolution (default 8K).
    """
    ydl_options = {
        'format': f'bestvideo[height<={max_resolution}]+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        print(f"\nDownloading video (up to {max_resolution}p)...")
        ydl.download([video_url])
        print("Video download complete!")

def download_audio(video_url: str) -> None:
    """Download audio from a video as MP3.
    """
    ydl_options = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',  # Best quality
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        print("\nDownloading audio as MP3...")
        ydl.download([video_url])
        print("Audio download complete!")

def main() -> None:
    """Main function to handle user input and execute download options."""
    video_url = input("Enter the YouTube video URL: ")
    print("\nOptions:")
    print("1. List available formats")
    print("2. Download video (8K)")
    print("3. Download video (4K)")
    print("4. Download video (1080p)")
    print("5. Download video (720p)")
    print("6. Download video (480p)")
    print("7. Download audio (MP3)")
    
    choice = input("Enter your choice (1-7): ")

    try:
        if choice == '1':
            list_available_formats(video_url)
        elif choice == '2':
            download_video(video_url, max_resolution=4320)
        elif choice == '3':
            download_video(video_url, max_resolution=2160)
        elif choice == '4':
            download_video(video_url, max_resolution=1080)
        elif choice == '5':
            download_video(video_url, max_resolution=720)
        elif choice == '6':
            download_video(video_url, max_resolution=480)
        elif choice == '7':
            download_audio(video_url)
        else:
            print("Invalid choice! Please select a number between 1 and 7.")
    except Exception as error:
        print(f"An error occurred: {error}")



if __name__ == "__main__":
    main()