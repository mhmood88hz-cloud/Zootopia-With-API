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
  output += f"Name: {animals_data[i]["name"]}\n"
  output += f"Diet: {animals_data[i]["characteristics"]['diet']}<br/>\n"
  output += f"Location: {", ".join(animals_data[i]["locations"])}<br/>\n"
  try:
    output += f"Type: {animals_data[i]["characteristics"]["type"]}<br/>\n"
  except KeyError:
    pass
  output += "</i>"
with open("animals_template.html", "r") as file:
  html_comment = file.read()
new_html = html_comment.replace("{{animals_data}}", output)
with open("animals.html", "w") as file:
  file.write(new_html)
