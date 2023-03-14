import time


class Screen:
    def __init__(self, name):
        self.name = name

    def print_header(self):
        """
        program screen introduction
        """
        print("\n------------------------------------------")
        print(self.name)
        print("------------------------------------------")
        time.sleep(2)

    def print_introduction(self):
        """
        presentation of the program
        """
        print(
            "This program will wait for the item in the ZalandoLounge online store in the reservation instead of you."
        )
        print("You need url adress of the product")
        print(
            "And calculate the order of your size in the chart. Count for all rows together."
        )
        time.sleep(3)

    def print_end(self):
        """
        end of the program
        """
        print("\n• The program is over\n")
        print("Thank you for using our app\n")
