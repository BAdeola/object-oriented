import requests

class WebScrap:
    url : str

    def __init__(self, url):
        self.url = url

    def __str__(self):
        resposta = requests.get(self.url)
        txt = f"Resultado = {resposta}\n"
        self.html = f"Codigo HTML = \n{resposta.text}"
        return txt

    def title(self):
        inicio = self.html.find("<title>")
        fim = self.html.find("</title>")
        titulo = self.html[inicio + 7 :fim]
        return titulo


