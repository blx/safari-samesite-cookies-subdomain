# safari-cookies demo

Demonstrates Safari `SameSite=Lax` cookie behaviour difference from chrome, firefox.

## Setup

Make the subdomains resolve correctly:

```
sudo echo '127.0.0.1 safaridemo.local' >> /etc/hosts
sudo echo '127.0.0.1 app.safaridemo.local' >> /etc/hosts
```

Install dependencies:

```
virtualenv -p python3 .env
. .env/bin/activate
pip install -r requirements.txt
```

Start dev server:

```
FLASK_APP=src/main flask run
```

Open browser to `http://safaridemo.local:5000`. Open dev console.

Click login link. This returns a 302 redirect to a subdomain, plus sets a cookie.

See a session ID printed out.

Click `Send fetch()`. Look in console.

**If main.py SAME_SITE param is `'Lax'`, then Safari should console.log `fetch ok` along with the session ID. If main.py SAME_SITE param is None, then Safari should console.log `fetch ok` along with a null session. In either case, Chrome and Firefox should show the session id.**
