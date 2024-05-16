**0x1A-application_server
[Github](https://github.com/PrimotionStudio)
task 0

[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=ubuntu
Group=www-data
#WorkingDirectory=/home/ubuntu/AirBnb_clone_v2/web_flask
#Environment="PATH=/home/ubuntu/AirBnb_clone_v2/web_flask"
#ExecStart=gunicorn --workers 3 --bind unix:/home/ubuntu/AirBnb_clone_v2/web_flask/hbnb.sock -m 007 web_flask.0-hello_route:app
WorkingDirectory=/home/ubuntu/AirBnB_clone_v2/
Environment="PATH=/usr/bin:/bin:/usr/local/bin"
ExecStart=gunicorn --workers 3 --bind unix:/home/ubuntu/AirBnB_clone_v2/web_flask/hbnb.sock -m 007 web_flask.0-hello_route:app
#Environment="PATH=/home/ubuntu/AirBnb_clone_v2/hbnbenv/bin"
#ExecStart=/home/ubuntu/AirBnb_clone_v2/hbnbenv/bin/gunicorn --workers 3 --bind unix:hbnb.sock -m 007 wsgi:app
#ExecStart=/usr/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/AirBnb_clone_v2/web_flask/hbnb.sock -m 007 web_flask.0-hello_route:app

[Install]