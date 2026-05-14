import json

from pydantic_core.core_schema import dataclass_args_schema
from pyparsing import html_comment


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)
#MM

animals_data = load_data("animals_data.json")
def serialize_animal():
  output = ""
  output += '<li class="cards__item">'
  output += f'<div class="card__title">{animals_obj["name"]}</div><br/>'

  output += f'<div class="card__text">'
  output += f'<ul>'
  output += f"<li><strong>Diet: {animals_obj["characteristics"]['diet']}</li></strong><br/>"
  output += f"<li><strong>Location: {", ".join(animals_obj["locations"])}</li></strong><br/>"
  try:
    output += f"<li><strong>Type: {animals_obj["characteristics"]["type"]}</li></strong><br/>"
  except KeyError:
    pass
  output += f"</ul>"
  output += f"</div>"
  output += "</li>"
  output += "</li>"
  return output

output = ""
for animals_obj in animals_data:
  output += serialize_animal()

with open("animals_template.html", "r") as file:
  html_comment = file.read()
new_html = html_comment.replace("{{animals_data}}", output)
new_html = new_html.replace("â€™", "'")
with open("animals.html", "w") as file:
  file.write(new_html)
