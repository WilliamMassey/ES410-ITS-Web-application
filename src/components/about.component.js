import React, { useState } from "react";

function About(props) {

    const checker = e => {
            e.preventDefault ();
            
            console.log(props.token)
    }

    const [cars, setCars] = useState({cars:[]})

    const loadCars = () =>{
        fetch('http://localhost:8000/accounts/car-view/', {
        method: 'GET',
        headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${props.token}`,
        body:JSON.stringify({})}
        })
    .then( data => data.json())
    .then(
        data => {
        setCars({cars: data})
        }
    )
    .catch( error => console.error(error))
    }
    
    
        return (
            <div className="about-title">
                <h1>About us</h1>
                
                <button onClick={checker}>Load Cars</button>
            </div>
        );
    }

export default About