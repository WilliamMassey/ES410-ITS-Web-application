import React, { useState } from 'react'; 
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import LoginForm from "./components/login.component";
import SignUp from "./components/signup.component";
import Home from "./components/home.component";
import About from "./components/about.component";
import Map from "./components/map.component";
import PrivMap from "./components/privmap.component";
import Navbar from "./components/navbar.component";
import MyAccount from "./components/myaccount.component";
import MyBookings from "./components/mybookings.component";
import AddCar from "./components/addcar.component";


function App() {

  const [token, setToken] = useState("")
  const [isLoggedIn, setIsLoggedIn] = useState(false)

  const userLoginToken = (tok) => {
    setToken(tok)
  ;
  }

  const isUserLoggedIn = (login) =>{
    setIsLoggedIn(login);
    console.log(isLoggedIn)
  }

  return (<Router>
    <div className="App">
      {/* assigning route locations */}

      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/home" component={Home} />
        <Route path="/about" render={(routeProps) => <About {...routeProps} token={token} />} />
        <Route path="/sign-in" render={(routeProps) => <LoginForm {...routeProps} userLoginToken={userLoginToken} isUserLoggedIn={isUserLoggedIn}/>} />
        <Route path="/sign-up" component={SignUp} />
        <Route path="/map" component={Map} />
        <Route path="/privmap" component={PrivMap} />
        <Route path="/myaccount" render={(routeProps) => <MyAccount {...routeProps} token={token} />} />
        <Route path="/mybookings" render={(routeProps) => <MyBookings {...routeProps} token={token} />} />
        <Route path="/addcar" render={(routeProps) => <AddCar {...routeProps} token={token} />} />
      </Switch>
    </div>
  </Router>);
}

export default App;