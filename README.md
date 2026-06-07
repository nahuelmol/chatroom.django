# Chatroom
<div>
  <img src="https://img.shields.io/github/last-commit/nahuelmol/chatroom.django"/>
  <img src="https://img.shields.io/github/languages/code-size/nahuelmol/chatroom.django"/>
  <img src="https://img.shields.io/github/languages/top/nahuelmol/chatroom.django"/>
</div>

## Goal

The goal is to create a workspace where team members can communicate for an efective workflow.

## Used tools

* django-channels
* whitenoise : serves static files 

This is the Workflow:
        - Daphne receives the HTTP request.
        - WhiteNoise interpretes URLs that start with STATIC_URL.
        - WhiteNoise read the files from STATIC_ROOT.
        - WhiteNoise returns the content with the right MIME.
        - Daphne sends the response to the browser.

## Tools

Uvicorn and Daphne are possible to use on Windows and Linux:

* Uvicorn
  
```
uvicorn chatroom.asgi:application --host 127.0.0.1 --port 8000
```
 
* Daphne

```
daphne -b 127.0.0.1 -p 8000 chatroom.asgi:application
```
  
