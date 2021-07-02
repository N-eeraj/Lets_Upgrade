from pytube import YouTube

while True:
    url = input("Enter URL: ")
    video = YouTube(url).streams.get_highest_resolution()
    print(video.title)

    if input("Enter y to download: ").lower() == 'y':
        break

video.download()

print("Video Downloaded")
