import requests
from django.conf import settings

def send_msg(text):
    token = settings.TOKEN_BOT
    chat_id = "358170417"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
