
## BBSW
This is a django project and web project so there is no need to compile deploy.

##### Steps to deploy:

- Install python2.7
```
apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
pip install -r requirements.txt
```

- Install PhantomJS

```
apt-get update
apt-get install build-essential chrpath libssl-dev libxft-dev
apt-get install libfreetype6 libfreetype6-dev
apt-get install libfontconfig1 libfontconfig1-dev
cd ~
export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
sudo tar xvjf $PHANTOM_JS.tar.bz2
sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
phantomjs --version
```

- Git clone the source code to the server's specific path

(assume /root as follows)

```
git clone <repo>
```

- register download cron

First check credentials in download script.
```
crontab -e

*/10 * * * * python /root/Appeagle_scrape_price_strategy_compare/download_reports.py

```
Here you can change the interval. Now it is 10 minutes

- copy 30DR to /root
```
cp 30DR /root
```

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
