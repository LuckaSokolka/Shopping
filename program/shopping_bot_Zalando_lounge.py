from program.zalando_lounge import Zalando_lounge
from configuration.screen.screen import Screen
from configuration.product.product import Product


class Shopping_bot_Zalando_lounge:
    """ """

    def start_shopping_bot_Zalando_lounge(self):
        """
        part for users:
            screen
            input info about the product
            program
        """

        screen = Screen("\tZalandoLounge shopping_bot")
        screen.print_header()  # screen
        screen.print_introduction()
        print()

        item = Product()  # product
        # item.load_from_user()
        item.url = "https://www.zalando-lounge.cz/campaigns/ZZO24UH/categories/28977875/articles/PU141I03S-J11"
        item.size = "S"
        item.order = 2
        item.write_info_in_to_file()
        print()

        zalando = Zalando_lounge()  # shopping_bot
        zalando.start()

        screen.print_end()
