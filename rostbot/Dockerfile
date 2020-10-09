FROM node:current-slim

WORKDIR usr/src/app

COPY package.json .

RUN npm install

EXPOSE 3978:3978

CMD ["node", "index.js"]

COPY . .