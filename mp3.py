import os
import yt_dlp


def yt2mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'mp3/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }, {
            'key': 'EmbedThumbnail'
        }, {
            'key': 'FFmpegMetadata'
        }],
        'addmetadata': True,
        'writethumbnail': True,
        'verbose': False # debug
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(info_dict).replace(info_dict['ext'], 'mp3')
        filepath = os.path.abspath(filename)
        title = info_dict['title']
        if not os.path.isfile(filepath):
            ydl.download([url])
        else:
            print(f"File '{title}.mp3' already exists. Skipping download.")
        print(filepath)
        print(title)


if __name__ == '__main__':
    url = input('URL: ')
    yt2mp3(url)
