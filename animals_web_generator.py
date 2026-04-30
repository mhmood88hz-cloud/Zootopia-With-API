import json

from pydantic_core.core_schema import dataclass_args_schema
from pyparsing import html_comment


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data("animals_data.json")
output = ""
for i in range(len(animals_data)):
  output += '<li class="cards__item">'
  output += f'<div class="card__title">{animals_data[i]["name"]}</div>'
  output += f'<p class="card__text">'
  output += f"Diet: {animals_data[i]["characteristics"]['diet']}<br/>"
  output += f"Location: {", ".join(animals_data[i]["locations"])}<br/>"
  try:
    output += f"Type: {animals_data[i]["characteristics"]["type"]}<br/>"
  except KeyError:
    pass
  output += f"</p>"
  output += "</i>"
with open("animals_template.html", "r") as file:
  html_comment = file.read()
new_html = html_comment.replace("{{animals_data}}", output)
new_html = new_html.replace("â€™", "'")
with open("animals.html", "w") as file:
  file.write(new_html)
