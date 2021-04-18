import React, { useState } from 'react'; 
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import LoginForm from "./components/login.component";
import SignUp from "./components/signup.component";
import Home from "./components/home.component";
import About from "./components/about.component";
import Map from "./components/map.component"
import Logo from "./UniOfWarwickLogo.jpg"


function App() {

  const [token, setToken] = useState("")

  const userLogin = (tok) => {
    setToken(tok)
    ;
  }

  /* adding the routes to the navbar */

  return (<Router>
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-light fixed-top">
        <div className="container">
          <a href="https://warwick.ac.uk/" target ="_blank" rel="noreferrer">
            <img src={Logo} width="100" alt="warwick logo" />
          </a>
          <Link className="navbar-brand" to={"/home"}>ES410: Smart Car Park</Link>
          <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <Link className="nav-link" to={"/home"}>Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to={"/about"}>About Us</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to={"/sign-in"}>Login</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to={"/sign-up"}>Sign up</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

     {/* assigning route locations */}

      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/home" component={Home} />
        <Route path="/about" render={(routeProps) => <About {...routeProps} token={token} />} />
        <Route path="/sign-in" render={(routeProps) => <LoginForm {...routeProps} userLogin={userLogin} />} />
        <Route path="/sign-up" component={SignUp} />
        <Route path="/map" component={Map} />
      </Switch>
    </div>
  </Router>);
}

export default App;