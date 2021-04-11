import React, { useState } from "react";
import Background from '../BackgroundCarpark.jpg';

function InternalHome(){
   return(
      <div style={
         { backgroundImage: `url(${Background}`,
         backgroundPosition: "center", 
         height: "100%" }}>
         <div className="about-title">
            <h1>Find Parking on Campus in Seconds</h1>
         </div>
      </div>
   );
}

export default InternalHome