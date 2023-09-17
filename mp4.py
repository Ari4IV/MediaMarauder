import sys
import yt_dlp

if len(sys.argv) == 1:
    url = input("請輸入影片網址：")
else:
    url = sys.argv[1]

ydl_opts = {
    'format': 'mp4',
    'outtmpl': f'mp4/%(title)s.%(ext)s',
    'addmetadata': True,
    'verbose': False # debug
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])