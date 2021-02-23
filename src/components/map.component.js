import React, { useState } from "react";
import ImageMapper from "react-image-mapper";

function Map(){
 return(
  <div  className="map">
   <ImageMapper 
   src = "images/WarwickCampus.png" 
   map = {{name : "warwick-map", areas: [
    { name: "sportshub", shape: "poly", coords: [121,407,130,415,233,330,236,310,225,290] },
    { name: "science", shape: "poly", coords: [306,122,340,160,355,151,337,133,385,85,370,67]},
    { name: "oldsports", shape: "poly", coords: [495,157,533,130,540,140,510,170] },
   ]}} 
   alt="warwick campus" 
   width= "750"/>
  </div>
 )
}

export default Map