from flask import Flask, render_template, send_file
import os


app = Flask(__name__, static_folder='public', static_url_path='')


# Handle the index (home) page
@app.route('/')
def index():
    return render_template('index.html')
   

# Handle any files that begin "/course" by loading from the course directory
@app.route('/course/<path:path>')
def base_static(path):
    return send_file(os.path.join(app.root_path, '.', 'course', path))


# Handle any unhandled filename by loading its template
@app.route('/<name>')
def generic(name):
    return render_template(name + '.html')


if __name__ == "__main__":
    app.run()
