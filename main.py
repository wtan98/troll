import webbrowser
import threading

urls = [
    "https://www.youtube.com/",
    "https://www.youtube.com/",
    "https://www.youtube.com/",
]

def open_url(url):
    webbrowser.open_new(url)

while True:
    threads = []
    for url in urls:
        thread = threading.Thread(target=open_url, args=(url,))
        threads.append(thread)
        thread.start()
