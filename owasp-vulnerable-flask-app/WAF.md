#  WAF

Pour utiliser le script Flask WAF (Web Application Firewall) que nous avons créé, suivez ces étapes :

Installation de Flask : Assurez-vous que Flask est installé. Vous pouvez l'installer en utilisant la commande suivante dans votre terminal ou invite de commande :

```
pip install Flask
```

Copiez le Code : Copiez le code du script dans un fichier Python avec une extension .py. Par exemple, vous pouvez créer un fichier nommé app.py et y coller le code.

Exécution du Script : Exécutez le script en utilisant la commande suivante dans votre terminal ou invite de commande :

```
python app.py
```

Cela démarrera le serveur Flask.

Accédez à l'Application : Ouvrez votre navigateur et accédez à l'URL http://127.0.0.1:5000/ (ou à l'URL spécifiée dans la console après avoir démarré le serveur).

**Testez le WAF :**

Vous pouvez tester le WAF en accédant à différentes URLs qui incluent des motifs d'attaque spécifiés dans le script. Par exemple, essayez d'accéder à http://127.0.0.1:5000/?param=<script> pour tester la protection contre les attaques XSS.

**Observez la Réponse du WAF :**

Si une attaque est détectée, le serveur Flask renverra une réponse JSON indiquant que la requête a été bloquée par le WAF, ainsi qu'un code d'erreur HTTP 403.

**Personnalisez le WAF (Facultatif) :**

Si nécessaire, vous pouvez personnaliser la liste attack_patterns dans le script en ajoutant ou supprimant des motifs d'attaque selon vos besoins spécifiques.

N'oubliez pas que ce script est un exemple basique et ne couvre pas tous les aspects de la sécurité d'une application. Dans un environnement de production, vous voudrez peut-être explorer des solutions de sécurité plus robustes et bien établies, en utilisant des outils tels que des pare-feu applicatifs Web (WAF) tiers, des services de sécurité gérés, etc

## Intégrer un WAF (Web Application Firewall) à l'architecture d'une application web

Intégrer un WAF (Web Application Firewall) à l'architecture d'une application web en Python peut se faire de plusieurs manières en fonction de l'infrastructure et des besoins spécifiques de l'application. Voici quelques approches générales :

**Middleware dans le Framework Web :**

Si votre application web utilise un framework tel que Flask ou Django, vous pouvez intégrer le WAF en tant que middleware dans le framework.
Dans le cas de Flask, comme nous l'avons vu précédemment, vous pouvez utiliser @app.before_request pour exécuter du code avant chaque requête. Ceci peut servir à effectuer des vérifications de sécurité, y compris celles d'un WAF.

**Reverse Proxy :**

Placez le WAF en tant que reverse proxy devant votre serveur web principal. Les reverse proxies tels que Nginx ou Apache peuvent être configurés pour agir comme des pare-feu applicatifs Web.
Le WAF interceptera les requêtes avant qu'elles n'atteignent votre application et les inspectera pour détecter d'éventuelles attaques.

**Service Cloud WAF :**

Utilisez un service de sécurité cloud qui propose des fonctionnalités de WAF. Certains fournisseurs de services cloud offrent des solutions WAF en tant que service géré.
Configurez votre application pour acheminer le trafic web via ce service cloud.
Middleware personnalisé dans le Framework Web :

Si votre application utilise un framework web personnalisé, vous pouvez créer un middleware personnalisé pour gérer la sécurité, y compris les aspects du WAF.
Assurez-vous que le middleware est correctement configuré pour être exécuté avant le traitement de la requête.
Voici un exemple de middleware générique pour Flask qui pourrait être utilisé comme point de départ pour une intégration de WAF :

```python

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Liste des attaques à bloquer avec des expressions régulières
attack_patterns = {
    # ... (comme défini précédemment)
}

# Middleware Flask pour le WAF
@app.before_request
def waf_protection():
    for attack, patterns in attack_patterns.items():
        if any(re.search(pattern, request.url, re.IGNORECASE) for pattern in patterns):
            return jsonify(error=f"Blocked by WAF: {attack}"), 403

# Route d'exemple
@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

```

Notez que cette approche générique nécessite une adaptation en fonction de la complexité de votre application et des attaques spécifiques que vous souhaitez détecter. Les solutions de sécurité doivent être intégrées de manière à ne pas compromettre la fonctionnalité de l'application tout en fournissant une protection adéquate contre les menaces.

## Exemples d'URLs pour Tester le WAF

| URL d'Exemple                                  | Attaque Détectée        | Réponse Attendue                                      | Explications et Commentaires                                     |
|-----------------------------------------------|------------------------|-------------------------------------------------------|-----------------------------------------------------------------|
| `http://127.0.0.1:5000/?param=select`         | SQL Injection          | `{"error": "Blocked by WAF: SQLInjection"}`           | Tentative d'injection SQL avec le mot-clé `select` dans l'URL   |
| `http://127.0.0.1:5000/?param=<script>`       | XSS                    | `{"error": "Blocked by WAF: XSS"}`                   | Tentative d'injection de script XSS dans l'URL                |
| `http://127.0.0.1:5000/?param=;ls`            | Command Injection      | `{"error": "Blocked by WAF: CommandInjection"}`      | Tentative d'injection de commande avec le point-virgule       |
| `http://127.0.0.1:5000/?param=../../etc/passwd`| Path Traversal         | `{"error": "Blocked by WAF: PathTraversal"}`         | Tentative de traversée de chemin vers /etc/passwd             |
| `http://127.0.0.1:5000/?param=file:///etc/passwd`| Remote Code Execution | `{"error": "Blocked by WAF: RemoteCodeExecution"}` | Tentative d'exécution de code à distance avec `file://`       |
| `http://127.0.0.1:5000/?param=%0D%0ASet-Cookie`| HTTP Response Splitting| `{"error": "Blocked by WAF: HTTPResponseSplitting"}`| Tentative de division de la réponse HTTP avec des caractères spéciaux |
| `http://127.0.0.1:5000/?param=<!ENTITY`        | XML External Entity    | `{"error": "Blocked by WAF: XMLExternalEntity"}`    | Tentative d'injection d'entité XML externe                    |
| `http://127.0.0.1:5000/?param=http://localhost`| Server Side Request Forgery | `{"error": "Blocked by WAF: ServerSideRequestForgery"}` | Tentative de requête côté serveur avec une URL locale         |
| `http://127.0.0.1:5000/?param=_csrf_token`     | Cross-Site Request Forgery | `{"error": "Blocked by WAF: CrossSiteRequestForgery"}` | Tentative de CSRF avec un paramètre `_csrf_token`             |
| `http://127.0.0.1:5000/?param=%0D%0A`          | HTTP Response Splitting | `{"error": "Blocked by WAF: HTTPResponseSplitting"}`| Tentative de division de la réponse HTTP avec des caractères spéciaux |
| `http://127.0.0.1:5000/?param=<?php echo "Hello"; ?>` | Server Side Scripting | `{"error": "Blocked by WAF: ServerSideScripting"}`  | Tentative d'injection de script côté serveur avec PHP         |
| `http://127.0.0.1:5000/?param={{2+2}}`         | Server Side Template Injection | `{"error": "Blocked by WAF: ServerSideTemplateInjection"}` | Tentative d'injection de template côté serveur avec Jinja2 |
| `http://127.0.0.1:5000/?param=pickle.loads`    | Insecure Deserialization | `{"error": "Blocked by WAF: InsecureDeserialization"}` | Tentative d'injection de désérialisation non sécurisée avec Pickle |
| `http://127.0.0.1:5000/?param=/etc/passwd`     | Insecure Direct Object Reference | `{"error": "Blocked by WAF: InsecureDirectObjectReference"}` | Tentative d'accéder à un objet direct sans validation |
| `http://127.0.0.1:5000/?param=redirect:`      | Unvalidated Redirects and Forwards | `{"error": "Blocked by WAF: UnvalidatedRedirectsAndForwards"}` | Tentative de redirection non validée avec le préfixe `redirect:` |
| `http://127.0.0.1:5000/?param=ng-bind-html`   | Cross-Site Scripting AngularJS | `{"error": "Blocked by WAF: CrossSiteScriptingAngularJS"}` | Tentative d'injection XSS avec ng-bind-html dans AngularJS     |
| `http://127.0.0.1:5000/?param=dangerouslySetInnerHTML` | Cross-Site Scripting React | `{"error": "Blocked by WAF: CrossSiteScriptingReact"}` | Tentative d'injection XSS avec dangerouslySetInnerHTML dans React |
| `http://127.0.0.1:5000/?param=%7B%7B2%2B2%7D%7D` | Server Side Template Injection (Encoded) | `{"error": "Blocked by WAF: ServerSideTemplateInjection"}` | Tentative d'injection de template côté serveur encodée avec URL |
| `http://127.0.0.1:5000/?param=pickle.dumps`   | Autres Méthodes Pickle  | `{"error": "Blocked by WAF: InsecureDeserialization"}` | Tentative d'utilisation d'autres méthodes de Pickle pour contourner la désérialisation sécurisée |

## Intégrer Nginx en tant que WAF (Web Application Firewall) 

Intégrer Nginx en tant que WAF (Web Application Firewall) peut être réalisé en utilisant le module Nginx ModSecurity. ModSecurity est un pare-feu d'application web open source qui peut être utilisé pour détecter et prévenir diverses attaques web. Voici les étapes pour configurer Nginx avec ModSecurity en tant que WAF :

Étapes Générales :

**Installer Nginx avec ModSecurity :**

Assurez-vous que Nginx est installé sur votre serveur.

Installez ModSecurity. La manière précise dépend de votre système d'exploitation. Pour Ubuntu, vous pouvez utiliser la commande suivante :

```bash
sudo apt-get install libnginx-modsecurity
```

**Configurer ModSecurity :**

La configuration de ModSecurity se trouve généralement dans /etc/nginx/modsecurity.

Créez ou modifiez le fichier de configuration principal de ModSecurity, par exemple, /etc/nginx/modsecurity/modsecurity.conf. Assurez-vous que SecRuleEngine est réglé sur On pour activer ModSecurity.

```nginx
SecRuleEngine On
```
Configurez d'autres règles de sécurité selon vos besoins dans le même fichier ou dans des fichiers inclus.

Configurer Nginx pour Utiliser ModSecurity :

Dans la configuration Nginx principale (généralement /etc/nginx/nginx.conf), ajoutez la ligne suivante dans le bloc http pour charger le module ModSecurity :

```nginx
load_module modules/ngx_http_modsecurity_module.so;
```
Ajoutez la configuration ModSecurity dans le bloc server de votre site :

```nginx

server {
    # ... Autres configurations ...

    location / {
        ModSecurityEnabled on;
        ModSecurityConfig modsecurity.conf;
        # ... Autres configurations ...
    }
}
```

Redémarrez Nginx :

Après avoir apporté des modifications à la configuration, redémarrez Nginx pour appliquer les changements.

```bash
sudo service nginx restart
```

Notes Importantes :
Assurez-vous de tester soigneusement votre application après avoir activé ModSecurity. Certaines règles peuvent interférer avec le fonctionnement normal de votre application.
Surveillez les logs de ModSecurity (généralement situés dans /var/log/nginx/error.log ou /var/log/modsec_audit.log) pour détecter des événements de sécurité.
Personnalisation des Règles ModSecurity :
Vous pouvez personnaliser les règles ModSecurity pour répondre aux besoins spécifiques de votre application. Les règles sont généralement configurées dans des fichiers .conf dans le répertoire de configuration de ModSecurity.

Documentation Supplémentaire :
Documentation ModSecurity pour Nginx
ModSecurity Reference Manual
Ces étapes devraient vous aider à configurer Nginx avec ModSecurity en tant que WAF pour votre application web.

## Comportements de Nginx avec ModSecurity - Exemples

| Exemple | URL d'Exemple | Comportement Attendu | Explications et Commentaires |
|---------|---------------|-----------------------|------------------------------|
| 1       | `http://example.com/?param=select` | Requête bloquée | ModSecurity détecte une injection SQL dans le paramètre et bloque la requête. |
| 2       | `http://example.com/?param=<script>` | Requête bloquée | ModSecurity détecte une tentative d'injection de script XSS et bloque la requête. |
| 3       | `http://example.com/?param=;ls` | Requête bloquée | ModSecurity détecte une tentative d'injection de commande et bloque la requête. |
| 4       | `http://example.com/?param=../../etc/passwd` | Requête bloquée | ModSecurity détecte une tentative de traversée de chemin et bloque la requête. |
| 5       | `http://example.com/?param=file:///etc/passwd` | Requête bloquée | ModSecurity détecte une tentative d'exécution de code à distance et bloque la requête. |
| 6       | `http://example.com/?param=%0D%0ASet-Cookie` | Requête bloquée | ModSecurity détecte une tentative de division de la réponse HTTP et bloque la requête. |
| 7       | `http://example.com/?param=<!ENTITY` | Requête bloquée | ModSecurity détecte une tentative d'injection d'entité XML externe et bloque la requête. |
| 8       | `http://example.com/?param=http://localhost` | Requête bloquée | ModSecurity détecte une tentative de requête côté serveur avec une URL locale et bloque la requête. |
| 9       | `http://example.com/?param=_csrf_token` | Requête bloquée | ModSecurity détecte une tentative de Cross-Site Request Forgery (CSRF) et bloque la requête. |
| 10      | `http://example.com/?param=%0D%0A` | Requête bloquée | ModSecurity détecte une tentative de division de la réponse HTTP avec des caractères spéciaux et bloque la requête. |

**Explications et Commentaires :**

- Ces exemples représentent différentes attaques potentielles, et ModSecurity est configuré pour les détecter et bloquer.
- La configuration précise dépend des règles spécifiques que vous avez activées dans ModSecurity.
- Les événements de sécurité sont généralement enregistrés dans les logs de ModSecurity, ce qui permet une analyse ultérieure.
- Il est important de tester attentivement ces règles pour éviter de bloquer des requêtes légitimes de l'application.
- La personnalisation des règles est essentielle pour s'assurer que le WAF répond spécifiquement aux besoins de sécurité de votre application.
- Assurez-vous de surveiller régulièrement les logs pour identifier de nouvelles menaces et ajuster les règles en conséquence.

