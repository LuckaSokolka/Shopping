        item = Product()  # product
        # item.load_from_user()
        item.url = "https://www.zalando-lounge.cz/campaigns/ZZO24UH/categories/28977875/articles/PU141I03S-J11"
        item.size = "S"
        item.order = 2
        item.write_info_in_to_file()
        print()

from playsound import playsound


class Notice:
    """
    play sound
    """

    def play(self):
        playsound('configuration/music_notice/zalando.wav')

from playsound import playsound


class Notice:
    """
    play sound
    """

    def play(self):
        playsound('music_notice/zalan2.wav')