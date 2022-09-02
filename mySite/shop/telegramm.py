import requests


def send_msg(text):
    token = "5685308789:AAG6K4R_shqX6QDStLMQhPc1vL_3rHPJK7k"
    chat_id = "358170417"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
