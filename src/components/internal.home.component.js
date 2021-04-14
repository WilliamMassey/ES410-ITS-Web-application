import React, { useState } from "react";
import Background from '../BackgroundCarpark.jpg';
import Location from '../Location.png';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";


function InternalHome(){
   return(
      <div style={
         { backgroundImage: `url(${Background}`,
         backgroundPosition: "center", 
         height: "100%" }}>
         <div className="internal-home-title" style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <h1>Find Parking on Campus in Seconds</h1>
         </div>
         <div className="parking-location-title" style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <h2>Where would you like to park?</h2>
         </div>
         <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <div className="parking-location-list" style={{ display: 'flex', justifyContent: 'flex-end' }}>
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
            <div className="location-icon" style={{ display: 'flex', justifyContent: 'flex-end' }}>
               <Link to={"/map"}><img src={Location} width="50" alt="location img" /></Link>
            </div>
         </div>
         <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <button className="booking-button">Book Now!</button>
         </div>
      </div>
   );
}

export default InternalHome