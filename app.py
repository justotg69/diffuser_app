from flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def home():
    sentence = ''
    if request.method == 'POST':
        sentence = request.form['sentence']  # Get the sentence from the form
    return render_template('index.html', sentence=sentence)
 
if __name__ == '__main__':
    app.run(debug=True)