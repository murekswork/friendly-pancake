import YouTubeTranscript

from bs4 import BeautifulSoup

def get_subtitle(url):

    result = YouTubeTranscript.get_transcript(url)
    print(result)

get_subtitle('https://www.youtube.com/watch?v=WpAuNSU--cQ&ab_channel=MarshmelloVEVO')

