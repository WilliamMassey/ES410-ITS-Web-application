import React, { useState } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

function SignUp() {

    /* storing sign up data */
    const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    uni: "",
    registration: "",
    email: "",
    password: "",
    })

    const Register = formData => { 
        console.log(formData) 
        fetch("http://localhost:8000/accounts/register/", { 
            method: "POST", 
            headers: {"Content-Type": "application/json"}, 
            body: JSON.stringify(formData) 
        }).then( 
            data => { 
            console.log(data) 
            } 
        ).catch(error => console.error)
    }

    const submitHandler = e => {
        e.preventDefault()
        console.log(formData)
    }

        /* creating form for signing up */
        return (
            <div className="signup-wrapper">
                <div className="signup-inner">
                    <form onSubmit = {submitHandler}>
                        <h3>Create an account to continue</h3>
                        <div className="form-group">
                            <label>First Name</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter first name"
                            id="first-name" 
                            value={formData.firstName}
                            onChange = {e => {
                                setFormData({...formData, firstName:e.target.value})
                            }} />
                        </div>

                        <div className="form-group">
                            <label>Last Name</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter last name"
                            id="last-name" 
                            value={formData.lastName}
                            onChange = {e => {
                                setFormData({...formData, lastName:e.target.value})
                            }}/>
                        </div>

                        <div className="form-group">
                            <label>University ID (Optional)</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter University ID"
                            id="uni" 
                            value={formData.uni}
                            onChange = {e => {
                                setFormData({...formData, uni:e.target.value})
                            }}/>
                        </div>

                        <div className="form-group">
                            <label>Vehicle Registration Number</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter vehicle registration number"
                            id="regis-number" 
                            value={formData.registration}
                            onChange = {e => {
                                setFormData({...formData, registration:e.target.value})
                            }}/>
                        </div>

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
                            If you have an account <Link to={"/sign-in"}>login here</Link>
                        </p>
                        
                    </form>
                </div>
            </div>
        );
    }

export default SignUp