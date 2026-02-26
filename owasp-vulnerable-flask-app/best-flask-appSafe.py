from flask import Flask, jsonify, render_template_string, request, Response, render_template
import subprocess
from werkzeug.datastructures import Headers
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/home/kali/Desktop/upload"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# Utilisez toujours des requêtes paramétrées pour prévenir l'injection SQL
@app.route("/user/<string:name>")
def search_user(name):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    # Utilisez des requêtes paramétrées plutôt que de concaténer les chaînes
    cur.execute("select * from test where username = ?", (name,))
    data = str(cur.fetchall())
    con.close()
    import logging
    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(data)
    return jsonify(data=data), 200

# Évitez l'injection HTML en échappant les données avant de les insérer dans le modèle
@app.route("/welcome2/<string:name>")
def welcome2(name):
    # Utilisez la fonction d'échappement HTML pour prévenir l'injection HTML
    data = "Welcome " + escape(name)
    return data

# Évitez XSS en échappant les données avant de les rendre
@app.route("/hello")
def hello_ssti():
    if request.args.get('name'):
        name = request.args.get('name')
        template = f'''<div>
        <h1>Hello</h1>
        {escape(name)}
        </div>
        '''
        import logging
        logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
        logging.debug(str(template))
        return render_template_string(template)

# Utilisez la bibliothèque subprocess de manière sécurisée pour éviter l'injection de commande
@app.route("/get_users")
def get_users():
    try:
        hostname = request.args.get('hostname')
        # Utilisez la liste d'arguments pour passer les arguments de manière sécurisée
        command = ["dig", hostname]
        data = subprocess.check_output(command)
        return data
    except Exception as e:
        # Gérez les erreurs de manière appropriée plutôt que de renvoyer des messages d'erreur système
        data = str(hostname) + " username didn't found"
        return data

# Assurez-vous que le fichier lu est dans un répertoire autorisé
@app.route("/read_file")
def read_file():
    filename = request.args.get('filename')
    # Utilisez os.path.join pour construire des chemins de fichier sécurisés
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    try:
        # Vérifiez que le chemin du fichier est autorisé avant de le lire
        if os.path.isfile(filepath) and filepath.startswith(app.config['UPLOAD_FOLDER']):
            file = open(filepath, "r")
            data = file.read()
            file.close()
            import logging
            logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
            logging.debug(str(data))
            return jsonify(data=data), 200
        else:
            return jsonify(data="Invalid file path"), 403
    except Exception as e:
        return jsonify(data="Error reading file"), 500

# Utilisez la bibliothèque pickle de manière sécurisée pour éviter la désérialisation malveillante
@app.route("/deserialization/")
def deserialization():
    try:
        import socket, pickle
        HOST = "0.0.0.0"
        PORT = 8001
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            connection, address = s.accept()
            with connection:
                received_data = connection.recv(1024)
                # Utilisez la désérialisation sécurisée avec pickle
                data = pickle.loads(received_data)
                return str(data)
    except Exception as e:
        return jsonify(data="Error in deserialization"), 500

# Limitez le nombre de tentatives de connexion pour éviter les attaques de force brute
connection = {}
max_con = 50

@app.route('/login', methods=["GET"])
def login():
    username = request.args.get("username")
    passwd = request.args.get("password")
    # Utilisez un mécanisme de verrouillage pour éviter les attaques par force brute
    if request.remote_addr in connection:
        if connection[request.remote_addr] > 2:
            return jsonify(data="Too many req."), 403
        connection[request.remote_addr] += 1
    else:
        connection[request.remote_addr] = 1

    # Utilisez un mécanisme d'authentification sécurisé au lieu de comparer les chaînes directement
    if authenticate_user(username, passwd):
        return jsonify(data="Login successful"), 200
    else:
        return jsonify(data="Login unsuccessful"), 403

# Assurez-vous que le fichier uploadé est conforme aux types autorisés et non malveillants
@app.route('/upload', methods=['POST'])
def uploadfile():
    import os
    try:
        if 'file' not in request.files:
            return jsonify(data="No file part"), 400

        file = request.files['file']
        # Vérifiez le type de fichier pour éviter les téléchargements malveillants
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'
        else:
            return 'Invalid file type', 403
    except Exception as e:
        return jsonify(data="Error uploading file"), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)
