#!/bin/sh

docker stop guess-what
docker rm guess-what
docker build -t guess-what-img:latest --target streamlit .
docker run --restart unless-stopped -p 8501:8501 --name guess-what -d guess-what-img
