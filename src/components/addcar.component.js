import React, { Component } from "react";
import PrivNavbar from "./privnavbar.component";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

class AddCar extends Component {
   constructor(props){
            super(props);

            this.state = {
               car_number_plate:"",
               manufacturer: "",
            }

            this.submitHandler = this.submitHandler.bind(this);
            this.handleRegisChange = this.handleRegisChange.bind(this);
            this.handleManfChange = this.handleManfChange.bind(this);
            this.handleLogin = this.handleLogin.bind(this);
         }

         submitHandler = e => {
         e.preventDefault()

         console.log(this.state) 
         fetch("http://localhost:8000/accounts/car-create/", { 
               method: "POST", 
               headers: {"Content-Type": "application/json",
               Authorization: `Token ${this.props.token}`}, 
               body: JSON.stringify(this.state) 
         })
         .then( data => data.json())
         .then(
               data => { 
               } 
         ).catch(error => console.error)
         }

         handleRegisChange = e => {
            e.preventDefault()
            this.setState({car_number_plate : e.target.value})
         }

         handleManfChange = e => {
            e.preventDefault()
            this.setState({manufacturer : e.target.value})
         }

         handleLogin = e => {
            e.preventDefault()
            console.log(this.state)
         }

   render(){

      return(
         <div className="login-wrapper">
            <PrivNavbar/>
               <div className="login-inner">       
                  <form onSubmit={this.submitHandler}>
                     <h3>Add Car</h3>
                     <div className="form-group">
                           <label>Vehichle Registration Number</label>
                           <input type="text" 
                           className="form-control" 
                           placeholder="Enter registration number" 
                           id="regis" 
                           onChange={this.handleRegisChange} value ={this.state.car_number_plate} />
                     </div>

                     <div className="form-group">
                           <label>Vehicle Manufacturer</label>
                           <input type="text" 
                           className="form-control" 
                           placeholder="Enter vehicle manufacturer" 
                           id="manf"
                           onChange={this.handleManfChange} value ={this.state.manufacturer} />
                     </div>
                     <button type="submit" className="btn btn-primary btn-block">Submit</button>
                     <p className="have-account text-left">
                        <Link to={"/myaccount"}>Back</Link>
                     </p>
                  </form>
               </div> 
         </div>
      )
   }
}

export default AddCar