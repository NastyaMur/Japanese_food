FROM node:18.14.2-alpine3.17
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
ENV HOST=0.0.0.0
COPY package.json .
COPY package-lock.json .
RUN npm install
CMD ["npm", "run", "dev"]