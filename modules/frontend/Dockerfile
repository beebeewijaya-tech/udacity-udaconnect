FROM node:14.15.0-alpine3.12

WORKDIR .

COPY package.json ./

RUN npm install -g yarn --force
RUN yarn

CMD ["pwd"]
COPY . ./

EXPOSE 3000

CMD ["npm", "start"]

