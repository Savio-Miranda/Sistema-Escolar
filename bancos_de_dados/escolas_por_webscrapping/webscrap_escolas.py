import json


from requests import get
from bs4 import BeautifulSoup

link_total = "http://www.seduc.pa.gov.br/portal/escola/consulta_matricula/"
html_escolas_unidades = get(link_total + "RelatorioMatriculas.php?codigo_ure=19").text
soup = BeautifulSoup(html_escolas_unidades, 'html.parser')

links = soup.find_all("a")
links = [x["href"] for x in links if "disparar-consulta" in x["class"]]

unidade_escolhida = links[0]

html_escolas = get(link_total + unidade_escolhida).text
unidade = BeautifulSoup(html_escolas, 'html.parser')

escola = unidade.find_all("td")
escola = [x.find("a").text.replace("\n", "").replace("\t", "").strip() for x in escola if x.find("a") is not None]
escola = [x.split("-") for x in escola]
escola = [{"codigo": x[0].strip(), "escola": x[1].strip()} for x in escola]
print(escola)

with open('escolas.json', 'w') as banco:
    json.dump(escola, banco, indent=4)
