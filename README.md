# Blog API Demo

This RESTful web service can be deployed on most Linux versions with the following steps:

1. Install Flask

    `user@host:~$ pip install Flask `

2. Copy blog.db and blog_api.py into your installation directory, e.g. /opt/apps/blog/.

3. Set the following environment variable:

    `user@host:~$ export FLASK_ENV=development`

4. Launch the application:

    `user@host:~$ python blog_api.py`

