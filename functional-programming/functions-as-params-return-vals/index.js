// 1. Function as a Parameter
const operate = (str1, str2, operation) => operation(str1, str2);

// Concatenation function
const concat = (a, b) => a + b;

// Uppercase transformation function
const uppercase = (str) => str.toUpperCase();

// Using operate function with different operations
console.log(operate('Hello', ' World', concat));
console.log(operate('abc', null, uppercase));

// 2. Function as a Return Value
const stringAppender = (suffix) => (str) => str + suffix;

// Creating specific string appenders
var exclamate = stringAppender('!');

// Using the created functions
console.log(exclamate('Good'));
console.log(exclamate('Morning'));
