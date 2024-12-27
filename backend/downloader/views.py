import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
import yt_dlp


@api_view(['POST'])
def download_video(request):
    url = request.data.get('url')
    if not url:
        return Response({'error': 'No URL provided'}, status=400)

    try:
        # Set up yt-dlp options
        ydl_opts = {
            'format': 'best',
            # Save in the 'downloads' folder
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }

        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', None)
            video_file = f"downloads/{video_title}.mp4"

        return Response({
            'download_url': f"/media/{video_file}"
        })

    except Exception as e:
        return Response({'error': str(e)}, status=500)
