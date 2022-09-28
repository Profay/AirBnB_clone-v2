#!/usr/bin/env bash
# Script that deploy hbnb_static web server
if [ ! -x /usr/sbin/nginx ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
    sudo service nginx start
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R $USER:$USER /data
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t' /etc/nginx/sites-enabled/default

sudo service nginx restart
