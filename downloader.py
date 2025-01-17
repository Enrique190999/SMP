import yt_dlp

def downlaod(url):
    ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }],
    'ffmpeg_location': './ffmpeg/bin'  # Ruta a la carpeta donde está ffmpeg
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download([url])
        return error_code
    return True

