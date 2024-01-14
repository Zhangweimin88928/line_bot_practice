import requests
from bs4 import BeautifulSoup


def music_Leaderboard(input_country):
    country = {"西洋": "3",
               "日韓": "2",
               "華語": "1"}
    req = requests.get(
        'https://www.kiss.com.tw/music/billboard.php?a=%s' % (country[input_country]))
    soup = BeautifulSoup(req.text, 'html.parser')
    music_list = soup.find('tbody')
    music_info = music_list.find_all('td')
    music_name = []
    for music in music_info:
        music_name.append(music.get_text())
    show = ''
    for i in range(8, len(music_name)+8, 8):
        show += "名次:%s\n歌名:%s\n歌手:%s\n專輯名稱:%s\n發行公司:%s\n\n" % (
            music_name[i-8], music_name[i-7], music_name[i-6], music_name[i-5], music_name[i-4])
    return show
