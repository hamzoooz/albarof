mohmadalhadi5@gmail.com

Hamzoooz@0784512346#themezoz.com

sudo apt-get update & sudo apt-get upgrade -y 
sudo adduser hamzoooz 
sudo usermod -aG sudo hamzoooz
sudo visudo # to don't ask for passowrd always 
# in file add the folloing line   
hamzoooz  ALL=(ALL) NOPASSWD:ALL   
themezoz  ALL=(ALL) NOPASSWD:ALL   
ibnKathir  ALL=(ALL) NOPASSWD:ALL   
alheib  ALL=(ALL) NOPASSWD:ALL   
django   ALL=(ALL) NOPASSWD:ALL   

django  
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql

CREATE DATABASE themezoz;

CREATE USER themezoz WITH PASSWORD 'Hamzoooz&0784512346#themezoz.com';
ALTER ROLE themezoz SET client_encoding TO 'utf8';
ALTER ROLE themezoz SET default_transaction_isolation TO 'read committed';
ALTER ROLE themezoz SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE themezoz TO themezoz;
ALTER DATABASE themezoz  OWNER TO themezoz;
\q

sudo nano /etc/postgresql/<version>/main/postgresql.conf
listen_addresses = '*'
sudo systemctl restart postgresql

sudo nano /etc/postgresql/<version>/main/pg_hba.conf
host    replication     all             192.168.1.100/24        md5
host    replication     all             20.56.150.190/24        md5
host    themezoz        themezoz        0.0.0.0/8            md5

local   all   themezoz   md5

sudo -u postgres psql -d template1
\q

sudo systemctl start postgresql
sudo systemctl enable postgresql

<!-- python -c "import sqlparse; print(sqlparse.format(open('data_dump.sql').read(), reindent=True, keyword_case='upper'))" > postgresql_data_dump.sql
psql -U themezoz -d themezoz -f postgresql_data_dump.sql -->

<!-- cat /root/.digitalocean_passwords -->

## create djanog on home
sudo mkdir themezoz
sudo chown hamzoooz:hamzoooz -R themezoz 
# To check the Check the woner for dir must be for new user  


# Step tow 
su - hamzoooz # login to your account 
install python3-venv python3-pip supervisor -y  # gunicorn 
sudo apt-get install python3-venv python3-pip supervisor gunicorn  -y  # 
# create env and active and 
# and clone your project and install requerment filse 
python3 -m venv env 
source  env/bin/activate


git clone djanog 
git clone git@github.com:hamzoooz/themezoz.git
pip install -r requirements.txt 
supervisor 
sudo apt-get install supervisor   nginx
sudo apt-get install nginx 

pip install gunicorn 
## to check every thing it work good or no 
### you must be allow setup djanog and server to allow run in this port 

python manage.py runserver 0.0.0.0:8000

    gunicorn  --bind 0.0.0.0:8000 ibnkathir.wsgi:application

# Step Three Supervisor and gunicorn 
sudo nano /etc/supervisor/conf.d/ibnkathir.conf
 
[program:gunicorn]
directory =/home/ibnkathir/ibnkathir/ibnkathir
command = /home/ibnkathir/ibnkathir/env/bin/gunicorn --workers 3 --bind unix:/home/ibnkathir/ibnkathir/ibnkathir/ibnkathir/app.sock ibnkathir.wsgi:application
autostart=true
autorestart=true
stderr_logfile= /var/log/gunicorn/gunicorn.err.log
stdout_logfile=/var/log/gunicorn/gunicorn.out.log
[group:guni]
programs:gunicorn

~~~
sudo mkdir /var/log/gunicorn

# check it work ? 
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status 

<!-- cange the user  -->
sudo nano /etc/nginx/nginx.conf
sudo chown themezoz.com:themezoz.com@gmail.com -R /etc/nginx/nginx.conf


#Step Four NGINX 
sudo apt install nginx
sudo nano /etc/nginx/sites-available/albarof.conf


server {
    listen 80;
    server_name albarof.com www.albarof.com ;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
	autoindex on;
        alias /home/themezoz.com/albarof/staticfiles/;
    }
    location /media/ {
        alias /home/themezoz.com/albarof/media/;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/themezoz.com/albarof/app.sock;
    }
}

cd /etc/nginx/sites-available/
sudo chown hamzoooz:hamzoooz -R djanog.conf 
sudo ln /etc/nginx/sites-available/albarof.conf  /etc/nginx/sites-enabled/

sudo service nginx restart
sudo nginx -t 

<!-- go to project dir  -->
<!-- cd /home/hamzoooz/themezoz -->
python manage.py  collectstatic
# Step Five in install Free SSL with certbot 
=======
```



sudo nginx -t
sudo service nginx restart

python manage.py collectstatic
 
sudo apt install certbot python3-certbot-nginx -y 
sudo certbot 

[program:gunicorn-albarof.service]
command = /home/hamzoooz/env/bin/gunicorn albarof.wsgi -b 127.0.0.1:8000 -w 3
directory = /home/hamzoooz/albarof/


sudo ln -s /etc/nginx/sites-available/djanog.conf /etc/nginx/sites-enabled/







<!-- on digital ocean  -->
ssh root@143.198.149.190
ssh hamzoooz@143.198.149.190

adduser hamzoooz

usermod -aG sudo hamzoooz

sudo ufw app list
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status
rsync --archive --chown=hamzoooz:hamzoooz ~/.ssh /home/hamzoooz

sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
Hamzoooz@0784512346#themezoz.com

sudo -u postgres psql

CREATE DATABASE themezoz;

CREATE USER themezoz WITH PASSWORD 'Hamzoooz&0784512346#themezoz.com';
CREATE USER hamzoooz WITH PASSWORD 'Hamzoooz&0784512346#themezoz.com';

ALTER ROLE themezoz SET client_encoding TO 'utf8';
ALTER ROLE themezoz SET default_transaction_isolation TO 'read committed';
ALTER ROLE themezoz SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE themezoz TO themezoz;
GRANT ALL PRIVILEGES ON DATABASE themezoz TO hamzoooz;

ALTER DATABASE <db_name> OWNER TO <db_user>;
ALTER DATABASE themezoz OWNER TO hamzoooz;
\q

mkdir ~/themezoz
cd ~/themezoz

python3 -m venv env
source env/bin/activate

pip install django gunicorn psycopg2-binary

nano ~/themezoz/myproject/settings.py 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'themezoz',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

~/themezoz/manage.py makemigrations
~/themezoz/manage.py migrate

~/themezoz/manage.py createsuperuser

~/themezoz/manage.py collectstatic

sudo ufw allow 8000
~/themezoz/manage.py runserver 0.0.0.0:8000
http://server_domain_or_IP:8000


cd ~/themezoz
gunicorn --bind 0.0.0.0:8000 themezoz.wsgi
deactivate

sudo nano /etc/systemd/system/gunicorn.socket

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=ibnkathir daemon
Requires=ibnkathir.socket
After=network.target

[Service]
User=ibnkathir
Group=www-data
WorkingDirectory=/home/ibnkathir/ibnkathir/ibnkathir
ExecStart=/home/ibnkathir/ibnkathir/env/bin/gunicorn --access-logfile -  --workers 3 --bind unix:/run/gunicorn.sock ibnkathir.wsgi:application

[Install]
WantedBy=multi-user.target



sudo systemctl enable ibnkathir.socket
sudo systemctl start ibnkathir.socket

sudo systemctl status gunicorn.socket

file /run/gunicorn.sock

sudo journalctl -u gunicorn.socket

sudo systemctl status gunicorn

sudo journalctl -u gunicorn


sudo systemctl daemon-reload
sudo systemctl restart gunicorn


sudo nano /etc/nginx/sites-available/albarof

server {
    listen 80;
    server_name ibnkathir.net www.ibnkathir.net;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /staticfiles/ {
        root /home/ibnkathir/ibnkathir/ibnkathir/staticfiles;
    }

        location /media/ {
        root /home/ibnkathir/ibnkathir/ibnkathir/media;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}





sudo ln -s /etc/nginx/sites-available/ibnkathir /etc/nginx/sites-enabled


sudo nginx -t
sudo systemctl restart nginx


sudo ufw allow 8000
sudo ufw allow 'Nginx Full'


sudo tail -F /var/log/nginx/error.log


namei -l /run/gunicorn.sock


sudo systemctl status postgresql


sudo systemctl enable postgresql
sudo systemctl start postgresql


sudo systemctl daemon-reload
sudo systemctl restart ibnkathir.service
sudo systemctl enable ibnkathir.socket gunicorn.service 
sudo systemctl restart ibnkathir.service
sudo nginx -t && sudo systemctl restart nginx




chown -R www-data:www-data /var/www/book-hope.com




root@themezoz:~# cat /root/.digitalocean_passwords
DJANGO_USER=django
DJANGO_USER_PASSWORD=00452d29d464381405adf87d9dbbbc77
DJANGO_POSTGRESS_PASS=4cd39fb8bdb33da52f014535ec2b7f63
DJANGO_SECRET_KEY=949ce581a60e01e5a495cdecfb071efe
SECRET_KEY=ae0367c012e04751f858e52fe430a48f
SETTINGS_FILE=/home/django/django_project/django_project/settings.py




ExecStart=/home/hamzoooz/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          ibnkathir.wsgi:application
















[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=themezoz
Group=www-data
WorkingDirectory=/home/themezoz/albarof
ExecStart=/home/themezoz/albarof/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          albarof.wsgi:application

[Install]
WantedBy=multi-user.target

server {
    listen 80;
    server_name albarof.com www.albarof.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/themezoz/albarof/albarof/staticfiles;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
