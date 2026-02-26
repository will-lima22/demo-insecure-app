from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Liste des attaques à bloquer avec des expressions régulières
attack_patterns = {
    'SQLInjection': [r'\bselect\b', r'\bunion\b', r'\binsert\b', r'\bdelete\b', r'\bfrom\b', r'\bwhere\b'],
    'XSS': [r'<script>', r'onload=', r'javascript:', r'alert\(', r'prompt\(', r'confirm\('],
    'CommandInjection': [r';', r'\bexec\b', r'\bsh\b', r'\bpowershell\b', r'\bpython\b'],
    'PathTraversal': [r'\.\./', r'\.\.\\', r'\betc\b'],
    'RemoteCodeExecution': [r'\bexec\b', r'\bshell\b', r'\bsystem\b', r'\bpassthru\b', r'\bproc_open\b'],
    'LDAPInjection': [r'\b(|)\b', r'\b*\b', r'\b)\(|\)\b', r'\b(\|\()\b', r'\b(\*\()\b'],
    'CrossSiteRequestForgery': [r'\b_csrf_token\b', r'\bcsrfmiddlewaretoken\b', r'\bantiForgeryToken\b'],
    'HTTPResponseSplitting': [r'%0D%0A', r'%0D%0ASet-Cookie'],
    'XMLExternalEntity': [r'<!ENTITY', r'SYSTEM'],
    'ServerSideRequestForgery': [r'\bfile://\b', r'\bdict://\b', r'\bhttp://localhost\b'],
    'CrossSiteScriptingFlash': [r'\bExternalInterface.call\b', r'\bloadPolicyFile\b', r'\bURLRequest\b'],
    'SecurityMisconfiguration': [r'\.svn/', r'\.git/', r'\.bash_history'],
    'InsecureDirectObjectReference': [r'/etc/passwd', r'/etc/shadow', r'/etc/hosts'],
    'UnvalidatedRedirectsAndForwards': [r'\bredirect:\b', r'\bforward:\b', r'\breturn:\b'],
    'CrossSiteScriptingAngularJS': [r'\bng-bind-html\b', r'\bng-include\b', r'\bng-style\b'],
    'CrossSiteScriptingReact': [r'\bdangerouslySetInnerHTML\b', r'\breact-dangerous-html\b'],
    'InsecureDeserialization': [r'\bpickle.loads\b', r'\bjava\.io\.ObjectInputStream\b'],
    'ServerSideTemplateInjection': [r'\{\{.*\}\}', r'{%.*%}', r'<%.*%>', r'{{.*}}', r'{%.*%}', r'<?.*?>'],
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
