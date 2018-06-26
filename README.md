# Blog API Demo

This RESTful web service can be deployed on most Linux variants with the following steps (/opt/apps must exist with write permissions for the user that will be running the application):


1. Prepare virtual environment:

    `wwwuser@host:~$ virtualenv /opt/apps/blog`
    
    `wwwuser@host:~$ source /opt/apps/blog/bin/activate`
    
    `wwwuser@host:~$ pip install uWSGI Flask`


2. Copy blog.db and blog_api.py from this repo into /opt/apps/blog/. 


3. Start the application:

    `/opt/apps/blog/bin/uwsgi -s :8080 --protocol=http --wsgi-file /opt/apps/blog/blog_api.py --callable blog_api`
    


The API will be accessible on all interfaces of your webserver at http://HOSTNAME:8080/. Alternatively, to have the application start and stop automatically as a SystemD service you can copy uwsgi.service from this repo into /etc/systemd/system/ and run:

    systemctl start uwsgi.service
    
This implementation does not address the security ramifications of opening a database file for reading and writing through a webservice such as this, nor does it address the scalability and multi-user handling that might be required.

There are also ambiguities in the design requirements. For example, the blog post sender must utilize JSON formatting, but there is no requirement that their HTTP header specify the content type. This can confuse some third party libraries and lead to issues. Or can a blog post / title be composed of any valid Unicode character(s)? W3C best practices do not guarantee that anyone will follow them.

If this were destined for production additional error handling logic would be needed to sanitize input and handle errors gracefully, particularly surrounding database access. As with any database, however small, scheduled health checks are a must (SQLite vacuuming at the very least, although currently there is no means of *deleting* a blog post). Log rotation of some sort to avoid filling up the disk is also necessary, and uWSGI really shouldn't be running as root - but the deployment environment is unknown and any UID switching would need to be put into the service definition file.

In the real world this API would likely be part of a larger OSS environment, which would hopefully handle the SSL termination and perhaps provide a more robust web frontend than uWSGI. But if there are no further requirements declared, this solution should work for the foreseeable future (pending a security review and QA / stress testing. Writing to a sqlite file will likely have some file system speed limitations under heavy usage compared to other backend options).
