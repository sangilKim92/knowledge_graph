const { ApolloError } = require('apollo-server-errors')

const error =  class MyError extends ApolloError {
    constructor(message) {
      super(message, 'MY_ERROR_CODE');
  
      Object.defineProperty(this, 'name', { value: 'MyError' });
    }
  }

module.exports = error;