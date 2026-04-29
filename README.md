# Chatroom
<div>
  <img src="https://img.shields.io/github/last-commit/nahuelmol/chatroom.django"/>
  <img src="https://img.shields.io/github/languages/code-size/nahuelmol/chatroom.django"/>
  <img src="https://img.shields.io/github/languages/top/nahuelmol/chatroom.django"/>
</div>

## Goal

The goal is to create a workspace where team members can communicate and stay connected for the sake of an efective workflow.

## Tools

Uvicorn and Daphne are possible to use on Windows:

* Uvicorn
  
```
uvicorn chatroom.asgi:application --host 127.0.0.1 --port 8000
```
 
* Daphne

```
daphne -b 127.0.0.1 -p 8000 chatroom.asgi:application
```
  
