import React, { useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { Icon } from "leaflet"
import * as carparkData from "../data/carparks.json";
import PrivNavbar from "./privnavbar.component";

/* setting new parking icon */

const parking = new Icon ({
   iconUrl: "/images/parking.png",
   iconSize: [25,25]
   })

   function PrivMap(){
   const [activeCarpark, setActiveCarpark] = useState(null);

   return(

   /* initialising map from OpenStreetMap */

   <div  className="map">
      <PrivNavbar/>
      <MapContainer center ={[52.382921, -1.564097]} zoom ={15}>
         <TileLayer
         attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
         url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
         minZoom = {14}
         />

         {/* adding carpark locations to the map */}

         {carparkData.features.map(carpark => ( 
         <Marker 
            key={carpark.properties.CARPARK_ID} 
            position={carpark.geometry.coordinates}
            eventHandlers= {{mouseover: () =>{
               setActiveCarpark(carpark)
            }}}
            icon={parking}
         />
         ))}

         {/* adding the popup message when hovering over a carpark */}

         {activeCarpark && (
         <Popup
            position={activeCarpark.geometry.coordinates}
            eventHandlers= {{mouseout: () =>{
               setActiveCarpark(null)
            }}}
         >
         <div>
            <h3>{activeCarpark.properties.NAME}</h3>
            <p>{activeCarpark.properties.DESCRIPTION}</p>
         </div>
         </Popup>
         )}
      </MapContainer>
   </div>
   )
}

export default PrivMap