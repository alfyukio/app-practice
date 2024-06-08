# Template Project for Apache HTTP Server with Python 3 CGI Support


中学生向けのpython cgi作成のための環境

## Directories
* apache-python-image: 超シンプルなdockerfile
* cgi-bin: pythonプログラムを置く場所
* htdocs: 静的なhtmlを置く場所

## Run
To run this image, simply issue the command
```bash
# docker-compose up
```
or
```bash
# docker-compose up -d
```
with detached shell.

## Python Module
To add module(s) to Python 3 either using PIP or APT, rewrite Dockerfile in apache-python-image like:
```Dockerfile
FROM httpd:2.4
RUN apt-get update && apt-get install -y python3 apt-utils coreutils python3-pip python3-SOMEMODULE && apt-get upgrade -y
RUN pip3 install SOMEMODULE
```
And then rebuild it with command
```bash
# docker-compose up --build
```
