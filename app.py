from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    response = ""

    if request.method == "POST":
        user_input = request.form["query"]
        language = request.form["language"]

        translated = translator.translate(user_input, dest=language)
        translated_text = translated.text

        response = "Thank you for contacting support. We will resolve your issue shortly."

    return render_template("index.html", translated=translated_text, reply=response)

if __name__ == "__main__":
    app.run(debug=True)