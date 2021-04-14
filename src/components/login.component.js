import React, { useState } from "react";

function LoginForm({Login, error}) {
        const [details, setDetails] = useState({email:"", password:""})

        /* checking login details after submitting */
        const submitHandler = e => {
            e.preventDefault ();
            
            Login(details);
        }
        
        /* creating form for logging in */
        
        return (
            <div className="login-wrapper">
                <div className="login-inner">       
                    <form onSubmit={submitHandler}>
                        <h3>Sign In</h3>
                        {(error !=="") ? (<div className="error">{error}</div>) : ""}
                        <div className="form-group">
                            <label>Email address</label>
                            <input type="email" 
                            className="form-control" 
                            placeholder="Enter email" 
                            id="email" 
                            onChange={e => setDetails({...details, email: e.target.value})} value ={details.email} />
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
                        <p className="forgot-password text-right">
                            Forgot <a href="#">password?</a>
                        </p>
                    </form>
                </div> 
            </div>     
        );
    }

export default LoginForm

