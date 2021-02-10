# Long-Polling

### Requirements
- Python: 3.7.1
- Flask: 1.0.2
- Flask-marshmallow: 0.9.0
- marshmallow: 3.0.0b6
- marshmallow-sqlalchemy: 0.15.0
- sqlalchemy: 1.2.12
- Flask-sqlalchemy: 2.3.2
- Flask-script: 2.0.6
- Flask-Cors: 3.0.7

### How to run
After installing the requirements, create the database by below command:
```
  python manage.py initdb
```
 **Note:** Path of the database is *relative*, so if you encountered a database error enter the path *explicitly* (set   the dir_path variable)
Now run the Server using below command:
```
  python manage.py run
```
   Server will be run on Ip: *localhost* and port: *5000* by default.<br />
Open admin.html and click on *View Posts* and *New Post* and open them in seperate tabs.<br />
Add some posts and now you can see that new posts can be seen in view posts tab dunamically and on-demand. You can also edit or delete posts and see that all changes can be updated without **ANY REFRESH**.
