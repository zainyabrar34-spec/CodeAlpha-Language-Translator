from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        text = request.form.get("text")
        src = request.form.get("source_lang")
        dest = request.form.get("target_lang")
        if text:
            translated = translator.translate(text, src=src, dest=dest)
            translated_text = translated.text
    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
