import React, { useState } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

const formData = {
    firstName: "",
    lastName: "",
    uni: "",
    registration: "",
    email: ""
}

function SignUp() {

    {/* storing sign up data */}
    const [state, setState] = useState(formData)

    const submitHandler = e => {
        e.preventDefault()
        console.log(state)
    }

        {/* creating form for signing up */}
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
                            value={state.firstName}
                            onChange = {e => {
                                setState({...state, firstName:e.target.value})
                            }} />
                        </div>

                        <div className="form-group">
                            <label>Last Name</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter last name"
                            id="last-name" 
                            value={state.lastName}
                            onChange = {e => {
                                setState({...state, lastName:e.target.value})
                            }}/>
                        </div>

                        <div className="form-group">
                            <label>University ID (Optional)</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter University ID"
                            id="uni" 
                            value={state.uni}
                            onChange = {e => {
                                setState({...state, uni:e.target.value})
                            }}/>
                        </div>

                        <div className="form-group">
                            <label>Vehicle Registration Number</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter vehicle registration number"
                            id="regis-number" 
                            value={state.registration}
                            onChange = {e => {
                                setState({...state, registration:e.target.value})
                            }}/>
                        </div>

                        <div className="form-group">
                            <label>Email address</label>
                            <input type="email" 
                            className="form-control" 
                            placeholder="Enter email" 
                            id="email" 
                            value={state.email}
                            onChange = {e => {
                                setState({...state, email:e.target.value})
                            }}/>
                        </div>

                        <div className="form-group">
                                <label>Password</label>
                                <input type="password" 
                                className="form-control" 
                                placeholder="Enter password" 
                                id="password" />
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