
## BBSW
This is a django project and web project so there is no need to compile deploy.

##### Steps to deploy:

- Install python2.7
```
apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
pip install -r requirements.txt
```

- Git clone the source code to the server's specific path

(assume /root as follows)

```
git clone <repo>
```

- register download cron
```
crontab -e

*/10 * * * * python /root/Appeagle_scrape_price_strategy_compare/download_reports.py

```
Here you can change the interval. Now it is 10 minutes

- Migrate the server
```
python manage.py makemigrations general
python manage.py migrate
```
- Make a super user
```
python manage.py createsuperuser
```
- Launch the site
```
cd /root/Appeagle_scrape_price_strategy_compare
nohup python manage.py runserver 0.0.0.0:80 < /dev/null &
```
- check site
```
http://<ip_address>/admin
```
login with the credential for superuser you created.

- Define the interval for the cron job (in minute)
```
http://<ip_address>/admin/general/interval/

```
