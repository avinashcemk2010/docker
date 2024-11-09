FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

#expose the application on port 80 inside the application
EXPOSE 80 

ENV MONGODB_USERNAME=root
ENV MONGODB_PASSWORD=secret

#in CMD we can pass command followed by multiple arguments
CMD ["npm", "start"]