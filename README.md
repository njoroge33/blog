# BLOG
A personal blogging website where you can create and share your opinions and other users can read and comment on them.
## Built By [John Gichuhi](https://github.com/njoroge33/)
## Description
A personal blogging website where you can create and share your opinions and other users can read and comment on them.
You can view the site at: https://njoroblog.herokuapp.com/
## User Stories
These are the behaviours/features that the application implements for use by a user.
As a user I would like to:
- See the blogs other people have posted
- Signed in for me to leave a comment
- View the blogs i have created in profile page
- Click on the blog and leave a feedback
## Specifications
| Behaviour                                  |            Input             |                                                               Output |
| :----------------------------------------- | :--------------------------: | -------------------------------------------------------------------: |
| Display comments                           |       **On page load**       |           List of various comments sources is displayed per blog|
| Display comments from people who signed in |  **Click on the blog**   |         Redirected to a page with a list of comments from the source |
| Display the blogs and comments           |       **On page load**       |                 Each blog displays an title, description and author |
| Go back to click on the blog you need          |        **Click Home**        |                                  Redirected to the post a blog area | 
## SetUp / Installation Requirements
### Prerequisites
- python3.6
- pip
- virtualenv
### Cloning
- In your terminal:
  -$ git clone https://github.com/njoroge33/blog.git
  -$ cd blog
## Running the Application
- Creating the virtual environment
    -$ python3.6 -m venv --without-pip virtual
    -$ source virtual/bin/env
- Installing Flask and other Modules
  -$ python3.6 -m pip install Flask
       - $ python3.6 -m pip install Flask-Bootstrap
  -$ python3.6  pip install flask-migrate
        -$ python3.6 manage.py db init
  -$ python3.6 manage.py db migrate -m "Initial Migration"
       - $ python3.6 manage.py db upgrade
  -$ pip install flask-SQLAlchemy
        -$ pip install psycopg2
- To run the application, in your terminal:
  -$./start.sh or python3.6 manage.py server
## Testing the Application
- To run the tests for the class files:
  -$ cd app
        -$ python3.6 test_user.py
## Technologies Used
- Python3.6
- Flask
## License
MIT &copy;2019 [John Gichuhi](https://github.com/njoroge33)
BLOG
