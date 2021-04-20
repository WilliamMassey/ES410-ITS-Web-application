import React, { useState } from "react";
import { Redirect } from 'react-router-dom'

function About () {

    const [redirect, setRedirect] = useState(false)

    const setPath = () => {
            setRedirect(true) 
        }
    
    const renderRedirect = () => {
        if (redirect) {
            return <Redirect to='/sign-up' />
        }
    }

        return (
            <div className="about-title">
                <h1>About us</h1>
                {renderRedirect()}
                <button onClick={setPath}>Redirect</button>
            </div>
        )
}

export default About