import requests

API_KEY = "plyPimnA2MNAWv7ULhuqD8BQVc4tjcM3sQAzEqYR"


def load_data(animal_name):
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"

    headers = {
        "X-Api-Key": API_KEY
    }

    response = requests.get(url, headers=headers)

    return response.json()


def serialize_animal(animals_obj):

    output = ""

    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animals_obj["name"]}</div><br/>'

    output += '<div class="card__text">'
    output += '<ul>'

    try:
        output += f'<li><strong>Diet:</strong> {animals_obj["characteristics"]["diet"]}</li><br/>'
    except KeyError:
        pass

    try:
        output += f'<li><strong>Location:</strong> {", ".join(animals_obj["locations"])}</li><br/>'
    except KeyError:
        pass

    try:
        output += f'<li><strong>Type:</strong> {animals_obj["characteristics"]["type"]}</li><br/>'
    except KeyError:
        pass

    output += "</ul>"
    output += "</div>"
    output += "</li>"

    return output


animals_input = input("Enter animal name: ").strip().lower()

animals_data = load_data(animals_input)
if not animals_data:
    output = f"<h2>The animal '{animals_input}' doesn't exist.</h2>"
else:
    output = ""


for animals_obj in animals_data:
    output += serialize_animal(animals_obj)

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

new_html = html_template.replace("{{animals_data}}", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(new_html)

print("Website generated successfully!")