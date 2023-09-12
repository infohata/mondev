# syntax=docker/dockerfile:1
FROM nginx:latest
ARG run_as
# ENV run_as=${run_as}
# RUN adduser $run_as
WORKDIR /app
COPY ./monda_live.conf /etc/nginx/conf.d/default.conf
