from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "99999"





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
