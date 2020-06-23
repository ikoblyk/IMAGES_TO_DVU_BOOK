#!/bin/bash
docker build -t ikoblyk/bookhack:latest . && docker run ikoblyk/bookhack:latest && docker ps
