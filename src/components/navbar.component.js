import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Logo from "../UniOfWarwickLogo.jpg";



function Navbar(props) {
      console.log(props.isLoggedIn)

      return(
         props.isLoggedIn ? <nav className="navbar navbar-expand-lg navbar-light fixed-top">
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
                     <Link className="nav-link" to={"/myaccount"}>My Account</Link>
                  </li>
               </ul>
               </div>
            </div>
         </nav> 
         :
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
      )
}

export default Navbar