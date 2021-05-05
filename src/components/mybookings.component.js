import React, { Component } from "react";
import PrivNavbar from "./privnavbar.component";
import {DateTimePickerComponent} from '@syncfusion/ej2-react-calendars'
import Location2 from '../Location2.jpg';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

class MyBookings extends Component {
      constructor(props){
         super(props);

         this.state = {
            cars:[],
            isLoading: true,
            formData:{
               car:"",
               carpark:"",
               start_datetime:"",
               end_datetime:""
            }
         }

         this.submitHandler = this.submitHandler.bind(this);
         this.handleCarChange = this.handleCarChange.bind(this);
         this.handleParkChange = this.handleParkChange.bind(this);
         this.handleStartChange = this.handleStartChange.bind(this);
         this.handleEndChange = this.handleEndChange.bind(this);
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
               this.setState(prevState => {
                  let formData = Object.assign({},prevState.formData);
                  formData.car = data[0].car_number_plate;
                  return {formData}
               })
               console.log(this.props.token)
               console.log(this.state.cars)
               this.setState({isLoading:false})
            })

         .catch( error => console.error(error))
         }
         
         handleCarChange = e => {
            e.preventDefault()
            this.setState(prevState => {
                  let formData = Object.assign({},prevState.formData);
                  formData.car = e.target.value;
                  return {formData}
               })
         }
         
         handleParkChange = e => {
            e.preventDefault()
            this.setState(prevState => {
                  let formData = Object.assign({},prevState.formData);
                  formData.carpark = e.target.value;
                  return {formData}
               })
         }

         handleStartChange = e => {
            this.setState(prevState => {
                  let formData = Object.assign({},prevState.formData);
                  formData.start_datetime = e.target.value;
                  return {formData}
               })
         }

         handleEndChange = e => {
            this.setState(prevState => {
                  let formData = Object.assign({},prevState.formData);
                  formData.end_datetime = e.target.value;
                  return {formData}
               })
         }

         submitHandler = e => {
            e.preventDefault()
            console.log(this.state.formData)

            fetch("http://localhost:8000/accounts/booking-create/", { 
               method: "POST", 
               headers: {"Content-Type": "application/json",
               Authorization: `Token ${this.props.token}`}, 
               body: JSON.stringify(this.state.formData) 
            })
            .then( data => data.json())
            .then(
                  data => { 
                  } 
            ).catch(error => console.error)
            }

   render(){
      return(
         <div className="booking-title">
            <PrivNavbar/>
               <div className="general-wrapper">
                  <div className="general-inner">
                     <form onSubmit={this.submitHandler}>
                        <h3>Make A Booking</h3>
                        <div className="form-group">
                           <label>Car Selected:</label>
                           <input type="text"
                           className="form-control"
                           onChange={this.handleCarChange}
                           value={this.state.isLoading ? "" : this.state.cars[0] == null ? "" : this.state.cars[0].car_number_plate}
                           />
                        </div>
                        <div className="row">
                           <div className="column-booking-left">
                              <h6>Start Time:</h6>
                              <DateTimePickerComponent placeholder="Choose start time"
                              format="dd-MMM-yyyy HH:mm"
                              step={60}
                              onChange={this.handleStartChange} value ={this.state.formData.start_datetime}/>
                           </div>
                           <div className="column-booking-right">
                              <h6>End Time:</h6>
                              <DateTimePickerComponent placeholder="Choose end time"
                              format="dd-MMM-yyyy HH:mm"
                              step={60}
                              onChange={this.handleEndChange} value ={this.state.formData.end_datetime}/>
                           </div>
                        </div>
                        <div className="booking-parking-location-list">
                           <h6>Carpark Location:</h6>
                           <div style={{ display: 'flex', justifyContent: 'center' }}>
                              <select className="form-select" aria-label="Default select example"
                              onChange={this.handleParkChange} value ={this.state.formData.carpark}>
                                    <option selected>Choose location...</option>
                                    <option value="Argent Court Car Park">Argent Court Car Park</option>
                                    <option value="Old Sport Centre Car Park">Old Sport Centre Car Park</option>
                                    <option value="Science Car Park">Science Car Park</option>
                                    <option value="Sports and Wellness Hub Car Park">Sports and Wellness Hub Car Park</option>
                                    <option value="Westwood Games Hall Car Park">Westwood Games Hall Car Park</option>
                                    <option value="Tennis Centre Car Park">Tennis Centre Car Park</option>
                              </select>
                              <div className="location-icon-2">
                                 <Link to={"/privmap"}><img src={Location2} width="25" alt="location img" /></Link>
                              </div>
                           </div>
                        </div>
                        <button type="submit" className="btn btn-primary btn-block">Submit</button>
                        <p className="have-account text-left">
                           <Link to={"/myaccount"}>Back</Link>
                        </p>
                     </form>
                  </div>
               </div>
         </div>
      )
   }
}

export default MyBookings