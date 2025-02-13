# Use an official Node runtime as a base image running on top of Alpine Linux.
FROM node:14-alpine

# Set the working directory.
WORKDIR /app

# Copy package files and install dependencies.
COPY package*.json ./
RUN npm install

# Copy the rest of the application code.
COPY . .

# Expose the port that the app will run on.
EXPOSE 3000

# Start the application.
CMD ["npm", "start"]
