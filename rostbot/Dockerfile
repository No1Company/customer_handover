FROM node:current-slim

WORKDIR usr/src/app

COPY package.json .

RUN npm install

EXPOSE 3978

CMD ["node", "index.js", "--host 0.0.0.0"]

COPY . .