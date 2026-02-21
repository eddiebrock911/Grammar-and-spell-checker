from flask import Flask, render_template, request
from matplotlib import text
from Model import SpellCheckerModel

app = Flask(__name__)
spell_checker_module = SpellCheckerModel()

#route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell', methods=['POST', 'GET'])
def spell_check():
    if request.method == 'POST':
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)
        return render_template('index.html', corrected_text=corrected_text)

@app.route('/grammar', methods=['POST', 'GET'])
def grammar_check():
    if request.method == 'POST':
        file = request.files['file']  # request.files use karo
        readable_file = file.read().decode('utf-8', errors='ignore')
        corrected_file = spell_checker_module.correct_spell(readable_file)
        return render_template('index.html', corrected_file=corrected_file)

     


if __name__ == '__main__':
    app.run(debug=True)



