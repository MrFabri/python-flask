from flask import Flask, render_template

app = Flask(__name__)

# Avoids caching 
# I only recommend using this while you are in development mode. 
# Comment this in production.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Runs the server only if this is the main file!
if __name__ == '__main__':
    app.run(debug = True)