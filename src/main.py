import secrets
from flask import Flask, redirect, url_for, make_response, request
app = Flask(__name__)

DOMAIN = 'safaridemo.local'
C = 'BENSESSION'

# SAME_SITE = 'Lax'
SAME_SITE = None

app.config.update(
        SERVER_NAME = '%s:5000' % DOMAIN,
)

@app.route('/')
def index():
    return 'ok good. <a href="%s">login</a>' % (url_for('logon'))

@app.route('/api/logon')
def logon():
    resp = redirect(url_for('app_index'))
    cookie_params = {
        'samesite': SAME_SITE,
        'domain': '.%s' % DOMAIN,
        'httponly': True
    }
    resp.set_cookie(C, 'sess_%s' % secrets.token_urlsafe(16), **cookie_params)
    return resp

@app.route('/', subdomain='app')
def app_index():
    msg = 'app good'
    if request.cookies.get(C):
        msg += '. Got session cookie: %s \n' % request.cookies[C]
        msg += '''
            <br><a id="js1" href="#">Send fetch()</a>
            <script>
                document.getElementById('js1').onclick = () => {
                    fetch('/query', {credentials:'include'})
                        .then(r => r.text())
                        .then(r => { console.log(`fetch ok. ${r}`); })
                        .catch(z => { console.error('fetch reject', z); })
                };
            </script>
        '''
    return msg

@app.route('/query', subdomain='app')
def app_query():
    return {C: request.cookies.get(C)}
