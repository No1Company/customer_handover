FROM node:current-slim

WORKDIR usr/src/app

COPY package.json .

RUN npm install

EXPOSE 8080

CMD ["node", "index.js", "--host 0.0.0.0"]

COPY . .