# Framework

> Framework vs Library 

* Framework is a piece of code that dictates the architecture of your project and aids in programs
* pre-written JavaScript which allows for easier development of JavaScript-based applications

## Jquery

* introduces css-like syntax and several visual and UI enhancements 
* simplifies the use of Javascript in websites 
* an abstraction of the core language

### Syntax

> Install

```html
// check jQuery version
// console.log(jQuery.fn.jquery)
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.js"></script>
```

> Variable

```js
const $a = $('#id');        // variable starts with $
const $b = $('.classname')
$('element:hidden/visible')              // Matches all elements that are hidden / visible
$('#container').children(':visible');    // Get visible children
```

* each()

```js
$( "li" ).each(function( index ) {
  console.log( index + ": " + $( this ).text() );
});
```

> Error

* Uncaught TypeError: Cannot read property 'call' of undefined
  * each() requires a handler use on() instead

## Vue

* model–view–viewmodel front end JavaScript framework for building user interfaces and single-page applications.

## React

* Create-react-app → Need node > 6
* Webpack development environment → run live server and a development environment
* babel → manage your code, make it write a version compatible with older browsers

```sh
npx create-react-app <name>    # don’t have to download create-react-app
```

> Term

* JSX
  * React DOM escapes any values embedded in JSX before rendering them → Prevents Injection Attacks
  * Babel compiles JSX down to React.createElement() calls

* Element
  * React elements are immutable → can’t change its children or attributes
  * ReactDOM.render() every second from a setInterval() callback → usually called once

* Key
  * special string attribute you need to include when creating lists of elements
  * key only has to be unique among its siblings, not globally unique

* Props
  * props are read only

> Errors

* Use uuid as a key

```js
function NumberList(props) {
    return (
        <ul>{props.numbers.map((number) => <li>{number}</li>);}</ul>
    );
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);

const uuid = require('uuid/v1');
const todoItems = todos.map((todo, index) =>
  <li key={uuid()}> {todo.text} </li>
);
```

> Component

* Class Component
  * functions accept inputs (props) and return elements
  * must have only one div
  * starts with upper-cass

```js
class Movie extends React.Component{
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }
  render () {
    return (<div>
              <h1> {this.props.title} </h1>
              <h2> {this.props.genre} </h2>
           </div>)
  }
}
```

* Functional Component
  * Hook allows you to use functional component
  * Only call Hooks at the top level. Don’t call Hooks inside loops, conditions, or nested functions.
  * Only call Hooks from React function components. Don’t call Hooks from regular JavaScript functions

```js
const [count, setCount] = useState(0);

// Similar to componentDidMount and componentDidUpdate:
useEffect(() => {
  // Update the document title using the browser API
  document.title = `You clicked ${count} times`;
});

return (
  <div>
    <p>You clicked {count} times</p>
    <button onClick={() => setCount(count + 1)}>
      Click me
    </button>
  </div>
);
```

> Dom

* Update real DOM for only those objects which are changed in Virtual DOM
* To allow React to create a Virtual DOM, you will need React’s Components
* Replace class attribute name to className, because it is reserved in javascript

```js
function tick() {
  const element = (<div>
    <h1>Hello, world!</h1>
    <h2>It is {new Date().toLocaleTimeString()}.</h2></div>
  );
  ReactDOM.render(element, document.getElementById('root'));
}
setInterval(tick, 1000);

import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
export default class App extends Component {
  render() {
    return (<Router>
        <div>
          <Nav />
          <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/about" component={About} />
            <Route exact path="/shop" component={Shop} />
          </Switch>
        </div>
      </Router>
    );
  }
}
```

> States

* Read-only
* share state by moving to closest common ancestor of the components that need it → lifting state up
* State is reserved only for interactivity, that is, data that changes over time

```js
constructor(props) {
  super(props);
  this.state = {
    brand: "Ford",
    model: "Mustang",
    color: "red",
    year: 1964
  };
}

state = {
  brand: "Ford",
  model: "Mustang",
  color: "red",
  year: 1964
};

// Put into HTML
<div>
  {this.state.todos.map(todo => (
    <Todo key={todo.key} content={todo.content} />
  ))}
</div>
```

```js
// Add, delete, update
this.setState(prev => ({  v: [...prev.v, added]}))
this.setState(prev => ({ v: prev.v.filter(n => n !== e.target.value) }));
this.setState({ v: update(this.state.v, {1: {name: {$set: 'updated field name'}}})})
```

### Nav

> Router nav bar

```js
import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class Nav extends Component {
  render() {
    const navStyle = {
      color: "white"
    };
    return (
      <nav>
        <h3>logo</h3>
        <ul className="nav-links">
          <Link style={navStyle} to="/about">
            <li>About</li>
          </Link>
        </ul>
      </nav>
    );
  }
}
```

### Material UI

* Explicitly built for react
* Flexibility, customize than bootstrap and semantic UI
* Active development, hooks

### Native

* Crossplatform application

```sh
npm i -g create-react-native-app
create-react-native-app my-project
cd my-project
npm start
yarn add react-native-elements
```

### Expo

> Lan

* For this to work, on the same wifi network as your computer
* Fastest, safest. The phone connects to your computer just through your router.

> Tunnel 

* Under tunnel setting, your computer will setup a tunnel to exp.direct, 
* a domain using the ngrok tunnel service. 
* all traffic will go through a proxy in the cloud, but it can punch through most firewalls, 
* it will work under more conditions.

> download

```
npm install -g expo-cli
expo init my-new-project
cd my-new-project
expo start
npm run eject    # removes the app from the Expo framework
```