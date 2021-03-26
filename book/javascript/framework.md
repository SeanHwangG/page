# Framework

> Framework vs Library

* Framework is a piece of code that dictates the architecture of your project and aids in programs
* pre-written JavaScript which allows for easier development of JavaScript-based applications

## Jquery

* introduces css-like syntax and several visual and UI enhancements
* simplifies the use of Javascript in websites
* an abstraction of the core language

### Syntax

> Variable

* variable starts with $
* $('#id');
* $('.classname')
* $('element:hidden/visible') : Matches all elements that are hidden / visible
* $('#container').children(':visible'); : Get visible children

* each()

{% tabs %}
{% tab title='jquery.js' %}

```html
<!-- check jQuery version -->
<!-- console.log(jQuery.fn.jquery) -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.js"></script>
```

{% endtab %}
{% tab title='each.js' %}

```js
$( "li" ).each(function( index ) {
  console.log( index + ": " + $( this ).text() );
});
```

{% endtab %}
{% endtabs %}

> Error

* Uncaught TypeError: Cannot read property 'call' of undefined
  * each() requires a handler use on() instead

## Vue

* model–view–viewmodel front end JavaScript framework for building user interfaces and single-page applications

## React

* Create-react-app → Need node > 6
* Webpack development environment → run live server and a development environment
* babel → manage your code, make it write a version compatible with older browsers

* npx create-react-app <name> : don’t have to download create-react-app

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

{% tabs %}
{% tab title='uuid.js' %}

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

{% endtab %}
{% endtabs %}

> Component

* Class Component
  * functions accept inputs (props) and return elements
  * must have only one div
  * starts with upper-cass

{% tabs %}
{% tab title='class_component.js' %}

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

{% endtab %}
{% tab title='functional_component.js' %}

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

{% endtab %}
{% endtabs %}

* Functional Component
  * Hook allows you to use functional component
  * Only call Hooks at the top level. Don’t call Hooks inside loops, conditions, or nested functions.
  * Only call Hooks from React function components. Don’t call Hooks from regular JavaScript functions

> Dom

* Update real DOM for only those objects which are changed in Virtual DOM
* To allow React to create a Virtual DOM, you will need React’s Components
* Replace class attribute name to className, because it is reserved in javascript

{% tabs %}
{% tab title='tick_update.js' %}

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

{% endtab %}
{% endtabs %}

> States

* Read-only
* share state by moving to closest common ancestor of the components that need it → lifting state up
* State is reserved only for interactivity, that is, data that changes over time

{% tabs %}
{% tab title='constructor.js' %}

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

{% endtab %}
{% tab title='crud.js' %}

```js
// Add, delete, update
this.setState(prev => ({  v: [...prev.v, added]}))
this.setState(prev => ({ v: prev.v.filter(n => n !== e.target.value) }));
this.setState({ v: update(this.state.v, {1: {name: {$set: 'updated field name'}}})})
```

{% endtab %}
{% endtabs %}

### Example

> [1] Button Counter

{% tabs %}
{% tab title="public/index.html" %}

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#000000" />
  <meta name="description" content="Web site created using create-react-app" />
  <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
  <title>React App</title>
</head>

<body>
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <div id="root"></div>
</body>

</html>
```

{% endtab %}
{% tab title="src/App.js" %}

```jsx
import React, { Component } from "react";

export default class App extends Component {
  constructor() {
    super();
    this.state = {
      number: 0
    };
  }
  render() {
    return (
      <div className="App">
        <p>{this.state.number}</p>
        <button onClick={() => { this.setState({ number: this.state.number + 1 }); }}> + </button>
        <button onClick={() => { this.setState({ number: this.state.number - 1 }); }}> - </button>
        <button onClick={() => { this.setState({ number: 0 }); }}> Reset </button>
      </div>
    );
  }
}
```

{% endtab %}
{% tab title="src/index.js" %}

```jsx
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

ReactDOM.render(<App />, document.getElementById("root"));
```

{% endtab %}

{% endtabs %}

> [2] Todo Router

{% tabs %}
{% tab title="public/index.html" %}

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#000000" />
  <meta name="description" content="Web site created using create-react-app" />
  <title>App</title>
</head>

<body>
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <div id="root"></div>
</body>
</html>
```

{% endtab %}
{% tab title="components/App.js" %}

```jsx
import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";

import Home from "./pages/Home";
import About from "./pages/About";
import Header from "./components/Header";

export default function App() {
  return (
    <Router>
      <Header></Header>
      <Route exact path="/" component={Home}></Route>
      <Route path="/about" component={About}></Route>
    </Router>
  );
}
```

{% endtab %}
{% tab title="components/index.js" %}

```jsx
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

ReactDOM.render(<App />, document.getElementById("root"));
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="components/Header.js" %}

```jsx
import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header>
      <h1>TodoList</h1>
      <Link to="/">Home</Link> | <Link to="/about">About</Link>
    </header>
  );
}
```

{% endtab %}
{% tab title="components/Todo.js" %}

```jsx
import React from "react";

export default function Todo(props) {
  return (
    <div>
      <p style={{ display: "inline" }}>{props.title}</p>
      <button onClick={() => { props.delTodo(props.id); }} >
        x
      </button>
    </div>
  );
}
```

{% endtab %}
{% tab title="components/TodoForm.js" %}

```jsx
import React, { useState } from "react";

export default function TodoForm(props) {
  const [title, setTitle] = useState("");
  return (
    <form
      onSubmit={e => {
        e.preventDefault();
        props.addTodo(title);
        setTitle("");
      }}
    >
      <input onChange={e => setTitle(e.target.value)} value={title}></input>
      <button>submit</button>
    </form>
  );
}
```

{% endtab %}
{% endtabs %}

> [3] Firebase

{% tabs %}
{% tab title="public/index.html" %}

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="Web site created using create-react-app" />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>

```

{% endtab %}
{% tab title="components/App.js" %}

```jsx
import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import Header from "./components/Header";

require("firebase/auth");
export default function App() {
  return (
    <Router>
      <Header />
      <Route exact path="/" component={Home}></Route>
      <Route path="/about" component={About}></Route>
    </Router>
  );
}

```

{% endtab %}
{% tab title="components/index.js" %}

```jsx
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

ReactDOM.render(<App />, document.getElementById("root"));
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="components/Todo.js" %}

```jsx
import React from "react";

export default function Todo(props) {
  return (
    <div>
      <p style={{ display: "inline" }}>{props.title}</p>
      <button onClick={() => { props.delTodo(props.id); }} >
        x
      </button>
    </div>
  );
}
```

{% endtab %}
{% tab title="components/TodoForm.js" %}

```jsx
import React, { useState } from "react";

export default function TodoForm(props) {
  const [title, setTitle] = useState("");
  return (
    <form
      onSubmit={e => {
        e.preventDefault();
        props.addTodo({ title: title });
        setTitle("");
      }}
    >
      <input onChange={e => setTitle(e.target.value)} value={title}></input>
      <button>submit</button>
    </form>
  );
}
```

{% endtab %}
{% tab title="components/Header.js" %}

```jsx
import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
  return ( <div>
             <h1>Todo app</h1>
             <Link to="/">Home</Link> | <Link to="/about">About</Link> |
           </div>
         );
}
```

{% endtab %}
{% tab title="pages/Home.js" %}

```jsx
import React, { useState, useEffect } from "react";
import Todo from "../components/Todo";
import TodoForm from "../components/TodoForm";
import { firestore } from "../database/firebase";

export default function Home() {
  const [todos, setTodos] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      await firestore
        .collection("todos").get().then((snapshot) => {
          setTodos(
            snapshot.docs.map((doc) => { return { id: doc.id, ...doc.data() }; })
          );
        });
    };
    const listen = async () => {
      firestore.collection("todos").onSnapshot((snapshot) => {
        setTodos(
          snapshot.docs.map((doc) => { return { id: doc.id, ...doc.data() }; })
        );
      });
    };
    fetchData();
    listen();
  }, []);

  return (
    <>
      {todos.map((todo) => (
        <Todo key={todo.id} id={todo.id} title={todo.title} done={todo.done} delTodo={async (id) => {
            await firestore.doc(`todos/${id}`).delete();
          }} ></Todo>
      ))}
      <TodoForm addTodo={async (post) => { await firestore.collection("todos").add(post); }}
      ></TodoForm>
    </>
  );
}
```

{% endtab %}
{% tab title="pages/About.js" %}

```jsx
import React from "react";
import { FirebaseAuthConsumer } from "@react-firebase/auth";

export default function About() {
  return (
    <>
      <FirebaseAuthConsumer>
        {isSignedIn => {
          if (isSignedIn) {
            return <p> secret message </p>;
          } else {
            return <p>only logged in user can see this!</p>;
          }
        }}
      </FirebaseAuthConsumer>
    </>
  );
}
```

{% endtab %}
{% tab title="database/firebase.js" %}

```jsx
import firebase from "firebase/app";
import "firebase/firestore";

const config = {
  apiKey: "AIzaSyC98sPjNQHieYs2NmsJORADRDG85U1-Z8",
  authDomain: "polar-gasket-172700.firebaeapp.com",
  databaseURL: "https://polar-gasket-17270.firebaseio.com",
  projectId: "polar-gasket-17270",
  storageBucket: "polar-gasket-17270.appspot.com",
  messagingSenderId: "53621080903",
  appId: "1:536210809093:web:cb20f99edf24530"
};

export default firebase.initializeApp(config);

export const firestore = firebase.firestore();
```

{% endtab %}
{% endtabs %}

### Nav

> Router nav bar

```jsx
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
