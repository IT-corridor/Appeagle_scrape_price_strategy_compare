
## BBSW
This is a django project and web project so there is no need to compile deploy.

##### Steps to deploy:

1. Git clone the source code to the server's specific path

(assume /root as follows)

```
git clone <repo>
```


2. register download cron
```
crontab -e

*/10 * * * * python /root/Appeagle_scrape_price_strategy_compare/download_reports.py

```
Here you can change the interval. Now it is 10 minutes

3. Migrate the server
```
python manage.py makemigrations
python manage.py migrate
```
4. Make a super user
```
python manage.py createsuperuser
```
5. Launch the site
```
cd /root/Appeagle_scrape_price_strategy_compare
nohup python manage.py runserver 0.0.0.0:80 < /dev/null &
```
6. check site
```
http://<ip_address>/admin
```
login with the credential for superuser you created.

7. Define the interval for the cron job (in minute)
```
http://<ip_address>/admin/general/interval/

```