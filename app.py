from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('indexpage.html')

@app.route('/echopage', methods = ["POST"])
def echoinput():
    val_input = request.form.get('user_input', " ")
    return render_template('outpage.html', val_input = val_input)

if __name__ == "__main__":
    app.run()