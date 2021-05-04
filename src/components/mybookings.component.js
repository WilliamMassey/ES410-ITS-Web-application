import React, { Component } from "react";
import PrivNavbar from "./privnavbar.component";
import {DateTimePickerComponent} from '@syncfusion/ej2-react-calendars'

class MyBookings extends Component {
      constructor(props){
         super(props);

         this.state = {
            booking:[],
            isLoading: true,
         }
      }
      
      componentDidMount(props){
         fetch('http://localhost:8000/accounts/booking-view/', {
         method: 'GET',
         headers: {
         'Content-Type': 'application/json',
         Authorization: `Token ${this.props.token}`}
         })

         .then( data => data.json())
         .then(
            data => {
               this.setState({booking: data})
               console.log(this.props.token)
               console.log(this.state.booking)
               this.setState({isLoading:false})
            })

         .catch( error => console.error(error))
         }

   render(){
      return(
         <div className="booking-title">
            <PrivNavbar/>
               <div className="general-wrapper">
                  <div className="general-inner">
                     <form>
                        <h3>Make A Booking</h3>
                        <div className="form-group">
                           <label>Car Selected:</label>
                           <input type="text"
                           className="form-control"
                           value={""}
                           />
                        </div>
                        <div className="row">
                           <div className="column-booking-left">
                              <h6>Start Time:</h6>
                              <DateTimePickerComponent/>
                           </div>
                           <div className="column-booking-right">
                              <h6>End Time:</h6>
                              <DateTimePickerComponent/>
                           </div>
                        </div>
                        <div className="booking-parking-location-list">
                           <h6>Carpark Location:</h6>
                           <div style={{ display: 'flex', justifyContent: 'center' }}>
                              <select className="form-select" aria-label="Default select example">
                                    <option selected>Choose location...</option>
                                    <option value="1">Argent Court Car Park</option>
                                    <option value="2">Old Sport Centre Car Park</option>
                                    <option value="3">Science Car Park</option>
                                    <option value="4">Sports and Wellness Hub Car Park</option>
                                    <option value="5">Westwood Games Hall Car Park</option>
                                    <option value="6">Tennis Centre Car Park</option>
                              </select>

                           </div>
                        </div>
                        <button type="submit" className="btn btn-primary btn-block">Submit</button>
                     </form>
                  </div>
               </div>
         </div>
      )
   }
}

export default MyBookings