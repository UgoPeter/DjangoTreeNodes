# How to run the project
## Requirements
  - python==3.9.13
  - pip==22.3.1
  - docker==20.10.*
## Steps to follow
### If you don't have virtual environment yet. Do this before next step
  - Documentation - https://docs.python.org/3.9/library/venv.html
  - (Linux) Create virtual environment in project root catalog - `python3 -m venv env`
### When you have venv
  - Activate virtual environment - `source env/bin/activate`
  - In djangoproject run command `pip install -r requirements.txt`
  - In root project catalog run `docker compose up -d`
    - check with `docker ps` if the mysql instance is up and running
  - In djangoproject catalog run `python manage.py migrate` and after `python manage.py runserver`
    - When server started, you can axces tree endpoint under `127.0.0.1:8000/tree`
## Tests 
  - In djangoproject catalog run command `python manage.py test`
# Implementation description
## Choosing algorithm 
#### MPTT - Modified Preorder Tree Traversal ( saving a start- & end-point) :
Based on the requirement for higher read performance compared to write and update, I chose the MPTT algorithm
  - Pros:
    - Retrieving a whole tree is easy and cheap
    - Finding all parents is cheap
    - Needed Fields directly accessible in SQL
    - Bonus: you're saving the order of childnodes within its parentnode too
  - Cons:
    - Inserting / Updating can be very expensive, as you'll maybe have to update a lot of nodes
### Other algorithms I considered:
#### Naive Approach with parent-id:
  - Pros:
    - Easy to implement
    - Easy to move a big subtree to another parent
    - Insert is cheap
    - Needed Fields directly accessible in SQL
  - Cons:
    - Retrieving a whole tree is recursive and therefore expensive
    - Finding all parents is expensive too ( SQL doesn't know recursions... )

#### Saving a path in each Node:
  - Pros:
    - Finding all parents is cheap
    - Retrieving a whole tree is cheap
    - Inserting is cheap
  - Cons:
    - Moving a whole tree is expensive
    - Depending on the way you save the path, you won't be able to work with it directly in SQL, so you'll always need to fetch & parse it, if you want to change it.

#### Closure table
  - Pros:
    - Easy to implement
    - Finding all parents is cheap
    - Inserting is cheap
    - Retrieving whole trees is cheap
  - Cons:
    - Needs an additional table
    - Takes up a lot of space compared to other approaches
    - Moving a subtree is expensive
## Choosing technology
  - Django-MPTT documentation: https://django-mptt.readthedocs.io/en/latest/ 
  - The MPTT library implements, as the name states, a modification of pre-order tree traversal; each node of the tree has two extra values associated to it, to assist in the traversal of the tree https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
  - Technologies I used for: 
     - Django
     - RestFramework
     - Django-MPTT
       - I considered using the django-treebeard library, but it only supports django up to version 3.2
  - I would use the MPTT library in production, but to avoid dependency hell in the future, I would move it as part of the project and take care of maintenance
# Future plans
  - Optimization for more than 500 nestings (python has recursion limit) 
  - Performance tests
  - Ability to specify certain tree we want to fetch from API 
  - Implementation of qunicorn and moving the project fully to docker