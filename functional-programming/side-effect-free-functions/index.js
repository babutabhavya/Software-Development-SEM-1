// Example of a function with side effects
var originalNumbers = [1, 2, 3, 4, 5];

// Function modifies the original array by filtering out even numbers
function filterWithSideEffects(array) {
  for (var i = 0; i < array.length; i++) {
    if (array[i] % 2 === 0) {
      array.splice(i, 1);
      i--;
    }
  }
}

console.log(filterWithSideEffects(originalNumbers));

// Example of a side-effect-free function
// Function takes an array, filters out even numbers, and returns a new array without modifying the original
const filterOutEvensWithoutSideEffects = (array) =>
  array.filter(
    (number) => number % 2 !== 0 // Does not modify the original array
  );

console.log(filterOutEvensWithoutSideEffects([1, 2, 3, 4, 5]));
