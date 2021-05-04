import React, { Component } from "react";
import PrivNavbar from "./privnavbar.component";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

class MyAccount extends Component {
      constructor(props){
         super(props);

         this.state = {
            cars:[],
            user:[],
            isLoading: true,
            isLoggedIn: true
         }
      }
      
      componentDidMount(props){
         Promise.all([
         fetch('http://localhost:8000/accounts/car-view/', {
         method: 'GET',
         headers: {
         'Content-Type': 'application/json',
         Authorization: `Token ${this.props.token}`}
         }),
         fetch('http://localhost:8000/accounts/user-detail/', {
         method: 'GET',
         headers: {
         'Content-Type': 'application/json',
         Authorization: `Token ${this.props.token}`}
         })])

         .then(([res1, res2]) => {
            return Promise.all([res1.json(), res2.json()])
         })

         .then(
            ([res1, res2]) => {
         this.setState({cars: res1})
         this.setState({user: res2})
         console.log(this.props.token)
         console.log(this.state.cars[0])
         this.setState({isLoading:false})
         this.setState({isLoggedIn:false})}
         )
         .catch( error => console.error(error))
         }

         render(){
               return (
                  <div className="account-title">
                     <PrivNavbar/>
                     <h2>My Account</h2>
                     <div className="row">
                        <div className="column">
                           <div className="general-wrapper">
                              <div className="general-inner">
                                 <form>
                                    <h3>General Details</h3>
                                       <div className="form-group">
                                          <label>First Name</label>
                                          <input type="text"
                                          className="form-control"
                                          value={this.state.isLoading ? "" : this.state.user.first_name}
                                          />
                                       </div>

                                       <div className="form-group">
                                          <label>Last Name</label>
                                          <input type="text"
                                          className="form-control"
                                          value={this.state.isLoading ? "" : this.state.user.last_name}
                                          />
                                       </div>

                                       <div className="form-group">
                                          <label>Username</label>
                                          <input type="text"
                                          className="form-control"
                                          value={this.state.isLoading ? "" : this.state.user.username}
                                          />
                                       </div>

                                       <div className="form-group">
                                          <label>Email address</label>
                                          <input type="email" 
                                          className="form-control" 
                                          value={this.state.isLoading ? "" : this.state.user.email}
                                          />
                                       </div>
                                 </form>
                              </div>
                           </div>
                        </div>

                        <div className="column">
                           {/* <h2>Hello {this.state.isLoading ? "" : this.state.user.first_name}</h2>
                           <h2>Your Vehicle(s):</h2>
                           {this.state.isLoading ? "" : this.state.cars.map( car => {
                              return <h3 key={car.id}>Number Plate: {car.car_number_plate}</h3>
                           })}
                           {this.state.isLoading ? "" : this.state.cars.map( car => {
                              return <h3 key={car.id}>Vehicle Manufacturer: {car.manufacturer}</h3>
                           })} */}
                           <div className="vehicle-wrapper">
                              <div className="vehicle-inner">
                                 <form>
                                    <h4>My Vehicle</h4>
                                    <div className="form-group">
                                       <label>Vehicle Registration Number</label>
                                       <input type="text" 
                                       className="form-control" 
                                       value={this.state.isLoading ? "" : this.state.cars[0] == null ? "" : this.state.cars[0].car_number_plate}
                                       />
                                    </div>
                                    <div className="form-group">
                                       <label>Vehichle Manufacturer</label>
                                       <input type="text" 
                                       className="form-control" 
                                       value={this.state.isLoading ? "" : this.state.cars[0] == null ? "" : this.state.cars[0].manufacturer}
                                       />
                                    </div>
                                    <Link to={"/addcar"}><button className="vehicle-button">Add Car</button></Link>
                                 </form>
                              </div>
                           </div>
                           <div className="general-wrapper">
                              <div className="general-inner">
                                 <form>
                                    <h4>My Bookings</h4>
                                 </form>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
            );
         }
      }

export default MyAccount
