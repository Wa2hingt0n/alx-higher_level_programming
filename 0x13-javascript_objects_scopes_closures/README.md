# 0x13 JavaScript - Objects, Scopes and Closures

## Overview

This project introduces the concept of objects in Javascript as well as their use in JavaScript object-oriented programming. The learning objectives of the project included:
- How to create an object in JavaScript
- What `this` means in the context of JavaScript objects
- What `undefined` means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Files

### [0-rectangle.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/0-rectangle.js)
This script creates an empty class `Rectangle` that defines a rectangle, using the class notation.

### [1-rectangle.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/1-rectangle.js)
Creates a class `Rectangle` that defines a rectangle with a constructor that taks two arguments, `w` for the width and `h` for the height.

### [2-rectangle.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/2-rectangle.js)
Defines a class `Rectangle` as in `1-rectangle.js` but if `w` or `h` is equal to 0 or not a positive integer, an empty object is created.

### [3-rectangle.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/3-rectangle.js)
Defines a class `Rectangle` as in `2-rectangle.js` and includes an instance method `print()` that prints the rectangle using the character `X`.

### [4-rectangle.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/4-rectangle.js)
Adds onto the class `Rectangle` created in `3-rectangle.js` by creating two additional instance methods:
 - `rotate()` that exchanges the `width` and `height` of the rectangle
 - `double()` that multiplies the `width` and the `height` of the rectangle by 2

### [5-square.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/5-square.js)
Creates a class `Square` that defines a square and inherits from `Rectangle` of
`4-rectangle.js`

### [6-square.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/6-square.js)
Creates a class `Square` that inherits from `Sqaure` of `5-square.js`. It includes an instance method called `charPrint(c)` that prints the rectangle using the character `c`, unless the argument to the method is `undefined`.

### [7-occurrences.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/7-occurrences.js)
Defines a function that returns the number of occurrences in a list.

### [8-esrever.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/8-esrever.js)
Defines a function that returns the reversed version of a list, without using the built-in method reverse.

### [9-logme.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/9-logme.js)
Prints the number of arguments already printed and the new argument value, in the format: `<number of arguments already printed>: <current argument value>`

### [10-converter.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/10-converter.js)
Defines a function that converts a number from base 10 to another base passed as argument.

### [100-map.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/100-map.js)
Imports an array and computes a new array.

### [101-sorted.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/101-sorted.js)
Imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

### [102-concat.js](https://github.com/Wa2hingt0n/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/102-concat.js)
Concatenates two files.