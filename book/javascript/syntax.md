# Syntax

## IO

> comment

```js
//      // single line
/* */    // multi line
```

### Print

```js
console.log();      
process.stdout.write():  // without newline
console.table([])       // print in table foramt
console.log(JSON.stringify(data))   // print in nice format
```

> Error

```js
console.trace();        // print stack trace when error
```

### Keywords

> const

* cannot change constant primitive, but can change the properties of constant objects
* Redeclaring an existing const variable, in the same scope is not allowed

```js
const x = 2;      // Allowed
const x = 3;      // Not allowed
{
  const x = 2;    // Allowed
}
```

> let vs var

* let variables are scoped to the immediate enclosing block denoted by { } (hence the block scope)

```js
{ let baz = "Bazz";}  // Reference error
console.log(baz);
```

> strict mode

* 'use strict';
* eliminates some JavaScript silent errors by changing them to throw errors
* attempting to assigning a value to an undeclared variable throws an error.
* Prevents accidental globals.

```js
x = 3.14;       // Reference error
delete x;       // Syntax error
function x(p1, p2) {};  
```

## Operation

> Backticks

```js
name = “sean”
`hi ${name}`    // hi sean
```

> Destructuring

```js
const {firstName: fn, lastName: ln} = person
console.log(`${fn} ${ln}`)
let [first, last] = ['sean', 'hwang']    // Destruct Array
console.log(first);
```

> Spread

* ..., use to copy contents of objects

```js
var arr = ['a','b', 'c']
var added = [...arr, 'd']                // Copy Array

function add(x, y, z) { console.log(x+y+z) }  // Pass array as parameter
var args = [0, 1, 2, 3] 
add(...args)

var obj1 = { foo: 'bar', x: 42 };
var clonedObj = { ...obj1 };            // Clone and merge object

var obj2 = { foo: 'baz', y: 13 };
var mergedObj = { ...obj1, ...obj2 };    // merge objects
```

> Artihmetics

```js
+ -  * /  // Addition / Subtraction / Multiplication / Division
** %      // Exponentiation (ES2016) / Modulus 
++ --     // Increment / Decrement
& | ^     // AND / OR / XOR
~         // NOT
<< <<<    // Unsigned(shifted off to right are discarded) / signed shift left
>> >>>    // Unsigned(shifted off to right are discarded) / signed shift right
typeof    // Returns the type of a variable
instanceof  // Returns true if an object is an instance of an object type
```

> Math

```js
E / PI 
abs() ceil() floor() round()  // floating point
sin() cos() tan() tanh()      // trig function
pow() exp() sqrt() log() cbrt()
max() min()               // 
random()                  // return 0 or 1
trunc()


// integer division
var quotient = Math.floor(y/x);
```

### Condition

> if

```js
(1+1==2) ? "Pass" : "Fail"
```

> switch

```js
switch(expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}
```

### Variable

* All JavaScript values, except primitives, are objects 
* Don’t Declare Number, String, Boolean Objects → slows down execution speed
* typeof() returns data types
* Objects are mutable: They are addressed by reference, not by value

```js
// compare address
var x = "John";             
var y = new String("John");
(x === y)     // false

// All of these evaluate to true
console.log(false == '0');
console.log(null == undefined);
console.log(" \t\r\n" == 0);
console.log('' == 0);
if ({}) // ...
if ([]) // ...
```

* JavaScript is loosely typed, so it can change its data type

```js
var x = 5 + "7";    // x.valueOf() is 57,  typeof x is a string
var x = "5" + 7;    // x.valueOf() is 57,  typeof x is a string
var x = 5 - "x";    // x.valueOf() is NaN, typeof x is a number
```

> Number

```js
EPSILON
MAX_SAFE_INTEGER
MAX_VALUE
MIN_SAFE_INTEGER
MIN_VALUE          // the smallest positive numeric value
NEGATIVE_INFINITY
NaN
POSITIVE_INFINITY
prototype

isFinite()
isInteger()
isNaN()
isSafeInteger()
parseFloat()
parseInt((radix))
toString((radix))

// Floating point
Number((6.688689).toFixed(1));  // 6.7
```

> Primitives

```js
===        // returns true if both operands are of the same type and contain the same value

ret = ret.replace(/that $/,'it');
'hi there how are you'.match(/\s/g).length;

process.stdin.addListener("data", (data)=>{
    var x = data.toString().split(/[\s,]+/).trim()
})

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

process.stdout.write("Download" + data.length + "%\r"); // overwrite line
```

### Iterables

* in vs of

```js
for...in Loop   // iterates over the index in the array.
for...of Loop   // iterates over the object of objects.
```

* comprehension

```js
[for (x of iterable) x]
[for (x of iterable) if (condition) x]
[for (x of iterable) for (y of iterable) x + y]
```

> String

```js
charAt / charCodeAt()
concat()
constructorendsWith()
fromCharCode()
includes()
lastIndexOf()
lengthlocaleCompare()
prototyperepeat()
search()
startsWith()
substr()
substring()
toLocaleLowerCase / UpperCase()
toLowerCase / UpperCase()
toString()
trim()
valueOf()

> indexOf()
var i = s.indexOf(" ")
var splits = [s.slice(0, i) + s.slice(i + 1)]   // split string manually

> match()                     // search a string for a match and returns matches
"a,b".match(/([^,]*,(.*)/))   // split once using regex

> split(delim, time)                
str.split("o").length-1   // count number of occurence → 

> replace()   
("bef", "aft")            // only once
(/bef/g, "after")         // replace all

> slice(start, end)       // extract parts of a string
.slice(1, end - 1)        // removes first and last char
("000" + n).splice(-4)    // rihgt pad
(n + "000").splice(4)     // rihgt pad

hit.objectID.split('-').slice(0, -1).join('-')    // python rsplit
```

> regex

```js
/()/;
```

> Array

```js
length               // Size of array
concat()
copyWithin()
entries()
every()
fill()
filter()             // array.filter(value => value < 0);
find()
findIndex()
forEach()            // arr.forEach((num, index) => { arr[index] = num * 2; });
from()
includes()
indexOf()
isArray()
join()
keys()
lastIndexOf()
map()                // let doubled = arr.map(num => { return num * 2; });
pop()
prototype
push()
reduce()             // [].reduce((a, b) => a + b);        // sum
reduceRight()
reverse()            // loop backward
shift()              // get first element = poll in queue
slice()
some()
sort()               // items.sort((a, b) => { return a.value - b.value; });
splice()             // items.splice(pos, num, newval);
toString()
unshift()
valueOf()

splice(index, delete);    // remove elements
split(',').map(Number);   // split as an integer
map(x=>x[0]);             // first column of 2d array
```

* Examples

```js
new Array(len).fill(0);   // Create empty array

// Uppercase all array
var fruits = ["Banana", "Orange", "Apple", "Mango"];
Array.prototype.myUcase = function() {
    for (i = 0; i < this.length; i++)
        this[i] = this[i].toUpperCase();
};
```

### Hashable

> Set

```js
var set = new Set();
new Set([1, 2, 3, 4, 5]);

length
add()
clear()
delete(value)
has()
```

* Example

```js
// Remove duplicate in array
const numbers = [2,3,4,4,2,3,3,4,4,5,5,6,6,7,5,32,3,4,5]
console.log([...new Set(numbers)]) 
```

> Object


```js
// Create
var person = {firstName:"John", lastName:"Doe", age:50};
var person = new Object();
person.firstName = "John";
person.lastName = "Doe";
person.age = 50;

obj.[key] || 0           // Use default
delete dict[entry[0]]    // Delete Keys
Object.keys(obj).reduce((a, b) => obj[a] > obj[b] ? a : b);    // Get the largest keys

// Merge Object using spread operator
var obj2 = { foo: 'baz', y: 13 };
var mergedObj = { ...obj1, ...obj2 };                    // merge objects

const person = {firstName: “sean”, lastName: “hwang”}   // Destruct object

Object.keys(myObject).length                            // Iterate key value
Object.entries(obj).forEach(([key, value]) => { console.log(key, value); });

// remove key
delete query["obsolte"];

// optional key
where: {
  ...(params.val && {key : val}),
}
```

### Time

> Date

```js
new Date()
new Date(year, month, day, hours, minutes, seconds, milliseconds)   // month from 0
new Date(milliseconds)
new Date(date string)

toDateString()
toUTCString()
toString()
```

* Example

```js
// Check Same date
var isSameDay = (dateToCheck.getDate() === actualDate.getDate() 
     && dateToCheck.getMonth() === actualDate.getMonth()
     && dateToCheck.getFullYear() === actualDate.getFullYear())


// Add Days
Date.prototype.addDays = function(d) {
  return new Date(this.valueOf() + 864E5 * d);
}
```

* Iterate date

```js
var now = new Date();
var daysOfYear = [];
for (var d = new Date(2012, 0, 1); d <= now; d.setDate(d.getDate() + 1)) {
    daysOfYear.push(new Date(d));
}
```


### Dom

> document

```js
children
classList                   // list of class
.add / remove('MyClass');   // add / remove to class

getElementById(id)          // get all elements with id
getElementByClassName(cls)  // get all elements with className

> querySelector
'tag.class#id';             // using query selector
'.class1, .class2'          // class1 or class2
'.class1.class2'            // class1 and class2
[style="display: none;"]    // display is 

setAttribute(name, value)

.querySelectorAll('.hideable').forEach(function(el) {
   el.style.display = 'none';
});
```

* toggle division

```js
<script>
function toggle(id){
  for (let element of document.getElementsByClassName("hideable")){
   element.style.display="none";
  }
  document.getElementById(id).style.display = "block";
}
</script>
<a href="#" onclick="toggle('div1');">div1</a>
<a href="#" onclick="toggle('div2');">div2</a>
<a href="#" onclick="toggle('div3');">div3</a>


<div class="hideable" id="div1" style="display:block">Div 1</div>
<div class="hideable" id="div2" style="display:none">Div 2</div>
<div class="hideable" id="div3" style="display:none">Div 3</div>
```

* add

{% tabs %}
{% tab title="index.html" %}

```html
<body>
  <script src="index.js"> </script>
</body>
```

{% endtab %}
{% tab title="index.js" %}

```js
const foods = ["pizza"];

function getFoods() {
  setTimeout(() => {
    let output = "";
    foods.forEach(food => {
      output += `<li>${food}</li>`;
    });
    document.body.innerHTML = output;
  }, 1000);
}

function addFood(food) {
  setTimeout(() => {
    foods.push(food);
    resolve();
  }, 1000);
}

async function init() {
  await addFood("hotdog");
  getFoods();
}

init();
```

{% endtab %}
{% endtabs %}

> window

```js
href         // entire URL
protocol     // protocol of the URL
host         // hostname and port of the URL
hostname     // hostname of the URL
port         // port number the server uses for the URL
pathname     // path name of the URL
search       // query portion of the URL
hash         // anchor portion of the URL
```

## OOP

### Function

* function is called with a missing argument, the value of the missing argument is set to undefined
* Pure function don’t attempt to change inputs, and always return the same result for the same inputs

> Impure Function

* Modify contents of argument

```js
function withdraw(account, amount) {
  account.total -= amount;
}
```

> Arrow 

```js
hello = () => "Hello World!";        # works if only has one statement
```

> map 6 returns new object

```js
var elements = ['Hydrogen', 'Helium', 'Lithium',];
elements.map(function(element) {  return element.length;});        // [8, 6, 7]
elements.map((element) => {  return element.length;});
elements.map(element => element.length);
```

> HTML

```js
class LoggingButton extends React.Component {
  handleClick = () => { console.log('this is:', this); }
  render() { return (<button onClick={this.handleClick}> Click me </button>); }
}
```

> Closure

* Basic Example

```js
function html_tag(tag) { 
  function wrap_text(msg) { 
    console.log('<' + tag + '>' + msg + '</' + tag + '>')
  } 
  return wrap_text
}

print_h1 = html_tag(‘h1’)
print_h1(‘sean’)
```

* Private variable using closure

```js
var makeCounter = function() {
  var privateCounter = 0;
  function changeBy(val) { privateCounter += val; }
  return {
    increment: function() { changeBy(1); },
    decrement: function() { changeBy(-1); },
    value: function() { return privateCounter; }
  }
};

var counter1 = makeCounter();
var counter2 = makeCounter();

alert(counter1.value());  // 0.

counter1.increment();
counter1.increment();
alert(counter1.value()); // 2.

counter1.decrement();
alert(counter1.value()); // 1.
alert(counter2.value()); // 0.
```

### Class

* Private variable is started with #
* JavaScript, class methods are not bound by default → arrow function

* this

```js
class Foo {
  constructor(name){
    this.name = name
  }
  display(){
    console.log(this.name);
  }
}

var foo = new Foo('Saurabh');
foo.display(); // Saurabh

// The assignment operation below simulates loss of context 
// similar to passing the handler as a callback in the actual 
// React Component
var display = foo.display; 
display(); // TypeError: this is undefined
```

* Mixin

```js
const Tracer = (SuperClass) => class extends SuperClass { 
    trace(msg) { console.info(`Message: ${msg}`); } 
}

class NiceWidget extends Tracer(Widget) { drawingNicely() { this.trace(); } }
```

### Concurrency

* Race Control

```js
const foods = ["pizza"];
function getFoods() {
    setTimeout(() => {
        foods.forEach(food => { document.body.innerHTML += `<li>${food}</li>`; });
    }, 1000);
}

function addFood(food) {
    setTimeout(() => {
        foods.push(food);
    }, 1000);
}

addFood("hotdog");
getFoods();                // doesn’t render hotdog
```

* Await

async function init() {
  await addFood("hotdog");
  getFoods();
}
init();

* Callback

```js
function addFood(food, callback) {
    setTimeout(() => {
        foods.push(food);
        resolve();
    }, 1000);
}
addFood("hotdog", getFoods);
```

* Promise

```js
function addFood(food) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      foods.push(food);
      resolve();
    }, 1000);
  });
}

addFood("hotdog").then(getFoods);
```

* multiple promise

```js
Promise.all([promise1, promise2]).then(values=>console.log(values))
```
