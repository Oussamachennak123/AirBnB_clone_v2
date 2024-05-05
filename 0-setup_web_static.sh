#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# install Nginx
sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx

# reate the folder /data/web_static/releases/test/
sudo mkdir -p /data/web_static/releases/test/

# Create the folder /data/web_static/shared/
sudo mkdir -p /data/web_static/shared/

# create fake html
echo 'This is a fake html' | sudo tee /data/web_static/releases/test/index.html

# ls -sf : create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# change ownership
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#restart Nginx
sudo service nginx start
