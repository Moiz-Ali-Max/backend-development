# Group Routers
It's way of writing or implementing ow we can define multiple routes. We don't create all routes on our app file (main.py), so there's a concept of group routers. For same routes we can group them in one file.

For example: We want to make a user, faculty routes, so we don't make routes in our main file, instead we do group routing

### How to do this?
Problem Statement: User/Faculty Routes
1. FastAPI gives us the API Router.
    - So we make a folder routers, and in that folder we make a file called users.py.
    - In that user.py file all the routes of users.

2. Secondly if we want to create routes of faculty
    - Then we make a file of faculty.py inside the routers folder

3. Thirdly we include all these routes into our main file. B/c that is our main so we just include them


### Utility Function:
It's also an way to make functions in organized way
- Let's say we make routes of user and faculty if we want to show some data to user's and faculty to show like pdf, or any other. So we don't write these extra logics on user.py file or faculty.py file.
- Instead we make another folder of utility function. And we only do function calling in these routes.

Group Routers makes our code structured and we write logic in organized way