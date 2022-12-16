FROM node:13.12.0-alpine as build
WORKDIR /app
COPY package*.json ./
RUN apk add --update python make g++  && rm -rf /var/cache/apk/*
RUN npm install -g npm@7.24.0
RUN npm i
COPY . ./
RUN ls -la
CMD npm run build
