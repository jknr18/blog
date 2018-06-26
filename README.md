# Blog API Demo

This RESTful web service can be deployed on most Linux variants with the following steps:


1. Prepare virtual environment:

    `user@host:~$ virtualenv /opt/apps/blog`
    `user@host:~$ source /opt/apps/blog/bin/activate`
    `user@host:~$ pip install uWSGI Flask`


2. Copy blog.db and blog_api.py from this repo into /opt/apps/blog/. Copy uwsgi.service into /etc/systemd/system/


4. Start the application service:

    `user@host:~$ sudo systemctl start uwsgi.service`

Alternatively, you can start the application directly:

    `/opt/apps/blog/bin/uwsgi -s :8080 --protocol=http --wsgi-file /opt/apps/blog/blog_api.py --callable blog_api`

