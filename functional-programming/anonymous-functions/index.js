/* 1. Anonymous Function Expression for Subtraction
   These functions do not have a name but
   are assigned to a variable and
   invoked using the variable
*/
var mergeArrays = (array1, array2) => [...array1, ...array2];

/* 2. Immediately Invoked Anonymous Function Expression for Division
   Such functions are also Anonymous and are directly invoked when created
*/
(function (a, b) {
  console.log(a / b);
})(8, 2);

/* 3. Mapping an array with an Anonymous Function for Doubling
   These are anonymous functions that can be used on data structures
   for manipulation
*/
var doubled = [1, 2, 3, 4, 5].map((num) => num * 2);

/* 4. Event Handler with an Anonymous Function for Mouseover
   These are the callback functions for whenever
   an event is fired in JavaScript
*/
var hoverElement = document.getElementById('hoverElement');
hoverElement.addEventListener('mouseover', () =>
  console.log('I just got hovered!')
);

/* 5. setTimeout with an Anonymous Function for Logging a Message after a Delay
   This is an anonymous function used as a callback for setTimeout
*/
setTimeout(
  () =>
    console.log(
      'I will execute after 2 seconds, only if you run me in SD project'
    ),
  2000
);
