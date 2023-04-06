FROM node:18.14.2-alpine3.17
WORKDIR /app/Front
COPY ./package*.json ./
RUN npm install
RUN npm install -g http-server
COPY . .
# RUN npm run build
# EXPOSE 8081
# CMD ["npm", "test:dev"]