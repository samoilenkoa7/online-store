import requests


def send_msg(text):
    token = "5523682718:AAHxQP03VtHWgxNky_nb291m-yo0csO2KQk"
    chat_id = "358170417"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
