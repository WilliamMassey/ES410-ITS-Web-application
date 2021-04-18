import React, { Component } from "react";


class About extends Component {
    constructor(props){
        super(props);

        this.state = {
            cars:[],
            isLoading: true
        }
    }
    
    componentDidMount(props){
        fetch('http://localhost:8000/accounts/car-view/', {
        method: 'GET',
        headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${this.props.token}`}
        })
        .then( data => data.json())
        .then(
        data => {
        this.setState({cars: data})
        console.log(this.props.token)
        console.log(this.state.cars[0].car_number_plate)
        this.setState({isLoading:false})}
    )
    .catch( error => console.error(error))
    }
    
        render(){
            return (
                <div className="about-title">
                    <h1>About us</h1>
                    <h2>Your Vehicle:</h2>
                    {this.state.isLoading ? "" : this.state.cars.map( car => {
                        return <h3 key={car.id}>Vehicle Manufacturer: {car.manufacturer}</h3>
                    })} 
                    {/* <h3>{this.state.isLoading ? "" : "Vehicle Manufacturer:"{this.state.cars[0].maunfacturer}}</h3> */}
                    <button>Load Cars</button>
                </div>
            );

        }
    }

export default About