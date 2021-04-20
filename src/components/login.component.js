import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import Navbar from "./navbar.component";

function LoginForm(props) {
        const [details, setDetails] = useState({username:"", password:""})
        const [isLoggedIn, setIsLoggedIn] = useState(false)
        const [verify, setVerify] = useState("")
        const [redirect, setRedirect] = useState("")


        const renderRedirect = () => {
            if (redirect) {
                return <Redirect to='/myaccount' />
            }
        }

        /* checking login details after submitting */
        const submitHandler = e => {
            e.preventDefault ();
            console.log(details) 
            fetch("http://localhost:8000/accounts/auth/", { 
                method: "POST", 
                headers: {"Content-Type": "application/json"}, 
                body: JSON.stringify(details) 
            })
            .then(data => data.json())
            .then( 
                data => { 
                props.userLoginToken(data.token);
                data.token == null ? setIsLoggedIn(false) : setIsLoggedIn(true)
                data.token == null ? setIsLoggedIn(false) : setVerify("Yes")
                data.token == null ? setIsLoggedIn(false) : setRedirect(true)
                props.isUserLoggedIn(isLoggedIn)
                console.log(data.token);
            } 
            )
            .catch(error => console.error)
            .catch(setVerify("No"));
        } 
        
        /* creating form for logging in */
        
        return (
            <div className="login-wrapper">
                <Navbar isLoggedIn={isLoggedIn}/>
                    <div className="login-wrapper">
                        <div className="login-inner">       
                            <form onSubmit={submitHandler}>
                                <h3>Sign In</h3>
                                <div className="form-group">
                                    <label>Username</label>
                                    <input type="text" 
                                    className="form-control" 
                                    placeholder="Enter username" 
                                    id="user" 
                                    onChange={e => setDetails({...details, username: e.target.value})} value ={details.username} />
                                </div>

                                <div className="form-group">
                                    <label>Password</label>
                                    <input type="password" 
                                    className="form-control" 
                                    placeholder="Enter password" 
                                    id="password"
                                    onChange={e => setDetails({...details, password: e.target.value})} value ={details.password} />
                                </div>

                                <div className="form-group">
                                    <div className="custom-control custom-checkbox">
                                        <input type="checkbox" className="custom-control-input" id="customCheck1" />
                                        <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
                                    </div>
                                </div>

                                <button type="submit" className="btn btn-primary btn-block">Submit</button>
                                {renderRedirect()}
                                {verify == "No" ? <p style={{ color: 'red' }}>Login credentials could not be verified, please try again.</p> : ""}
                                <p className="forgot-password text-right">
                                    Forgot <a href="#">password?</a>
                                </p>
                            </form>
                        </div> 
                    </div>   
                </div>
        );
    }

export default LoginForm

