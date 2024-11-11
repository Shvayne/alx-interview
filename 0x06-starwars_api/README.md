# 0x06. Star Wars API

## Description

This project involves creating a Node.js script that interacts with the Star Wars API to fetch and display information about characters based on a provided movie ID. The project focuses on understanding how to make HTTP requests, handle asynchronous operations, and manage command-line arguments to create an efficient and interactive experience for retrieving data from external APIs.

## Concepts Covered

- **HTTP Requests in JavaScript**: Making HTTP requests to external services, specifically using the `request` module in Node.js.
- **Working with APIs**: Understanding RESTful APIs, parsing JSON responses, and handling data asynchronously.
- **Asynchronous Programming**: Using callbacks, promises, and async/await to manage API response data.
- **Command Line Arguments in Node.js**: Accessing command-line arguments via `process.argv`.
- **Array Manipulation and Iteration**: Iterating over arrays and structuring data to display character names.

## Requirements

- **Environment**:
  - Node.js version 10.x
  - Ubuntu 20.04 LTS
- **Standards**:
  - Code should be semistandard-compliant.
  - Use `const` or `let`; `var` is not allowed.
  - Files should be executable and end with a new line.
  - Follow AirBnB style where applicable.

## Project Setup

1. **Install Node 10**:
   ```bash
   $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   $ sudo apt-get install -y nodejs
  ```
2. **Install semistandard**:
   ```bash
   $ sudo npm install semistandard --global
   ```
3. **Install the request module**:
   ```bash
   $ sudo npm install request --global
   $ export NODE_PATH=/usr/lib/node_modules
   ```
## Usage
   To run the script, provide a movie ID as a command-line argument:
   ```bash
   ./0-starwars_characters.js <movie_id>
   ```
