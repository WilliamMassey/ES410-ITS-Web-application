import React, { useState } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Navbar from "./navbar.component";

function SignUp() {

    /* storing sign up data */
    const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    password: "",
    })

    // const Register = formData => { 
    //     console.log(formData) 
    //     fetch("http://localhost:8000/accounts/user-create/", { 
    //         method: "POST", 
    //         headers: {"Content-Type": "application/json"}, 
    //         body: JSON.stringify(formData) 
    //     }).then( 
    //         data => { 
    //         console.log(data) 
    //         } 
    //     ).catch(error => console.error)
    // }

    const submitHandler = e => {
        e.preventDefault()

        console.log(formData) 
        fetch("http://localhost:8000/accounts/user-create/", { 
            method: "POST", 
            headers: {"Content-Type": "application/json"}, 
            body: JSON.stringify(formData) 
        })
        .then( data => data.json())
        .then(
            data => { 
            console.log(data.token) 
            } 
        ).catch(error => console.error)
    }

        /* creating form for signing up */
        return (
            <div className="signup-wrapper">
                <Navbar/>
                <div className="signup-inner">
                    <form onSubmit = {submitHandler}>
                        <h3>Create an account to continue</h3>
                        <div className="form-group">
                            <label>First Name</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter first name"
                            id="first-name" 
                            value={formData.first_name}
                            onChange = {e => {
                                setFormData({...formData, first_name:e.target.value})
                            }} />
                        </div>

                        <div className="form-group">
                            <label>Last Name</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter last name"
                            id="last-name" 
                            value={formData.last_name}
                            onChange = {e => {
                                setFormData({...formData, last_name:e.target.value})
                            }}/>
                        </div>

                        <div className="form-group">
                            <label>Username (Optional)</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter Username"
                            id="user" 
                            value={formData.username}
                            onChange = {e => {
                                setFormData({...formData, username:e.target.value})
                            }}/>
                        </div>

                        {/* <div className="form-group">
                            <label>Vehicle Registration Number</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter vehicle registration number"
                            id="regis-number" 
                            value={formData.registration}
                            onChange = {e => {
                                setFormData({...formData, registration:e.target.value})
                            }}/>
                        </div> */}

                        <div className="form-group">
                            <label>Email address</label>
                            <input type="email" 
                            className="form-control" 
                            placeholder="Enter email" 
                            id="email" 
                            value={formData.email}
                            onChange = {e => {
                                setFormData({...formData, email:e.target.value})
                            }}/>
                        </div>

                        <div className="form-group">
                            <label>Password</label>
                            <input type="password" 
                            className="form-control" 
                            placeholder="Enter password" 
                            id="password" 
                            value={formData.password}
                            onChange = {e => {
                                setFormData({...formData, password:e.target.value})
                            }}/>
                        </div>

                        <button type="submit" className="btn btn-primary btn-block">Submit</button>

                        {/* linking to login page */}

                        <p className="have-account text-right">
                            Already have an account? <Link to={"/sign-in"}>Sign in here</Link>
                        </p>
                        
                    </form>
                </div>
            </div>
        );
    }

export default SignUp