import React, { useState } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

{/* creating form for signing up */}

function SignUp() {
        return (
            <div className="signup-wrapper">
                <div className="signup-inner">
                    <form>
                        <h3>Create an account to continue</h3>
                        <div className="form-group">
                            <label>First Name</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter first name"
                            id="first-name" />
                        </div>

                        <div className="form-group">
                            <label>Last Name</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter last name"
                            id="last-name" />
                        </div>

                        <div className="form-group">
                            <label>University ID</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter University ID"
                            id="uni-id" />
                        </div>

                        <div className="form-group">
                            <label>Vehicle Registration Number</label>
                            <input type="text"
                            className="form-control"
                            placeholder="Enter vehicle registration number"
                            id="regis-number" />
                        </div>

                        <div className="form-group">
                            <label>Email address</label>
                            <input type="email" 
                            className="form-control" 
                            placeholder="Enter email" 
                            id="email" />
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