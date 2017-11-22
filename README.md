
## BBSW
This is a django project and web project so there is no need to compile deploy.

##### Steps to deploy:

1. Install python2.7
```
apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
pip install -r requirements.txt
```

2. Git clone the source code to the server's specific path

(assume /root as follows)

```
git clone <repo>
```

3. register download cron
```
crontab -e

*/10 * * * * python /root/Appeagle_scrape_price_strategy_compare/download_reports.py

```
Here you can change the interval. Now it is 10 minutes

4. Migrate the server
```
python manage.py makemigrations
python manage.py migrate
```
5. Make a super user
```
python manage.py createsuperuser
```
6. Launch the site
```
cd /root/Appeagle_scrape_price_strategy_compare
nohup python manage.py runserver 0.0.0.0:80 < /dev/null &
```
7. check site
```
http://<ip_address>/admin
```
login with the credential for superuser you created.

8. Define the interval for the cron job (in minute)
```
http://<ip_address>/admin/general/interval/

```
