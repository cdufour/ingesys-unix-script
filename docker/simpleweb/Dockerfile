FROM node:14.15.5-alpine

WORKDIR /app

COPY package.json .

# produit en sortie un dossier "node_modules" contenant les dépendances
RUN npm install

COPY server.js .

CMD ["node", "server.js"]