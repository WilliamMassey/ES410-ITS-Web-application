import React, { useState } from "react";

function About(props) {

    const checker = e => {
            e.preventDefault ();
            
            console.log(props.token)
    }

    const [cars, setCars] = useState([])

    const loadCars = () =>{
        fetch('http://localhost:8000/accounts/car-view/', {
        method: 'GET',
        headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${props.token}`},
        })
    .then( data => data.json())
    .then(
        data => {
        setCars({cars: data})
        console.log(props.token)
        console.log(cars)
        // console.log(cars.cars[0])
        }
    )
    .catch( error => console.error(error))
    }
    
    // var carData = cars.cars[0]
    
        return (
            <div className="about-title">
                <h1>About us</h1>
                { cars.map( car => {
                    return <h3 key={car.id}>{car.title}</h3>
                    })}
                <button onClick={loadCars}>Load Cars</button>
            </div>
        );
    }

export default About