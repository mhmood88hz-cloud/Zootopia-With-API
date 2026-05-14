import data_fetcher


def serialize_animal(animal):

    output = ""

    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal["name"]}</div>'

    output += '<div class="card__text">'
    output += '<ul>'

    try:
        output += f'<li><strong>Diet:</strong> {animal["characteristics"]["diet"]}</li>'
    except KeyError:
        pass

    try:
        output += f'<li><strong>Location:</strong> {", ".join(animal["locations"])}</li>'
    except KeyError:
        pass

    try:
        output += f'<li><strong>Type:</strong> {animal["characteristics"]["type"]}</li>'
    except KeyError:
        pass

    output += "</ul>"
    output += "</div>"
    output += "</li>"

    return output


animals_input = input("Enter animal name: ").strip().lower()

animals_data = data_fetcher.fetch_data(animals_input)

if not animals_data:

    output = f"""
    <h2>
        The animal "{animals_input}" doesn't exist.
    </h2>
    """

else:

    output = ""

    for animal in animals_data:
        output += serialize_animal(animal)


with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()


new_html = html_template.replace("{{animals_data}}", output)


with open("animals.html", "w", encoding="utf-8") as file:
    file.write(new_html)


print("Website generated successfully!")