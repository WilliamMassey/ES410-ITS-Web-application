import React, { Component } from "react";
import PrivNavbar from "./privnavbar.component";

class MyAccount extends Component {
      constructor(props){
         super(props);

         this.state = {
            cars:[],
            isLoading: true,
            isLoggedIn: true
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
         this.setState({isLoading:false})
         this.setState({isLoggedIn:false})}
      )
      .catch( error => console.error(error))
      }
      
         render(){
               return (
                  <div className="about-title">
                     <PrivNavbar/>
                     <h2>Your Vehicle(s):</h2>
                     {this.state.isLoading ? "" : this.state.cars.map( car => {
                        return <h3 key={car.id}>Vehicle Manufacturer: {car.manufacturer}</h3>
                     })}
                     {this.state.isLoading ? "" : this.state.cars.map( car => {
                        return <h3 key={car.id}>Number Plate: {car.car_number_plate}</h3>
                     })}
                     {this.state.isLoading ? "" : this.state.cars.map( car => {
                        return <h3 key={car.id}>Vehicle Colour: {car.colour}</h3>
                     })} 
                  </div>
            );
         }
      }

export default MyAccount
