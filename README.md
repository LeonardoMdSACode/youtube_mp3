# Youtube music

Ever wonder how you can listen to your favorite music even when your internet is down or you're getting your router under DDoS and still want to enjoy a song? Think no more, pytube is a library that brings you the solution.

This is a quick Python script that enables you to download a youtube video as a mp3 file.

Open your powershell in the same directory as the Python file and run 
```powershell
py youtube_mp3.py "INSERT YOUTUBE LINK HERE" "INSERT VIDEO TITLE HERE"
It will initially download your file as webm, change it to .mp3 and send it to your desired location folder.

### To select your desired location folder

In the code ```python
shutil.move(mp3_file_path, r"C:\Users\user\Music") 
change the C:\Users\user\Music to your directory of choice.