
# 🎁 Shopping Bot
***

Shopping Bot is a tool for shopping on zalando-lounge.cz. If the item you want is reserved by another customer, Shopping Bot will keep an eye on whether the item has been sold out or returned for sale on your behalf.<br>

Using this tool, you can:
- Go to the zalando-lounge.cz website.<br>
- Log in with your Google account.<br>
- Select the item you want.<br>
- When the item is reserved, Shopping Bot will automatically refresh the page.<br>
- Once the item becomes available, Shopping Bot will add it to your cart and play a notification sound.<br>
- If the item is sold out, Shopping Bot will display a message and play a notification sound.<br>

## 📦 Prerequisites

- python 3.11.1
- selenium 4.8.2 - pip install selenium<br>
- google chrome 111.0.5563.65<br>
- chromedriver <br> 
- undetected-chromedriver 3.4.6 - pip install undetected-chromedriver<br>
- playsound 1.2.2 (playsound 1.3.0 doesn't work) - pip install playsound==1.2.2<br>
- google account

## 📦 Installation
1. [Click here to download the project as a ZIP file](https://github.com/LuckaSokolka/shopping_bot/archive/refs/heads/main.zip)
2. Create a file named **log.py** in the same folder
3. Insert your Google email and password for your Google account in the log.py file:<br>

    email = "xxxxx"  # only the part before @gmail.com<br>
    password_gmail = "xxxxx"<br>

4. run the file main.py

## 🚀 How to use
After starting up the program, it is necessary to input data about the item:<br>

![terminal](photos/terminal.png)

![zalando_screen](photos/zalando_screen.png)

## Example







