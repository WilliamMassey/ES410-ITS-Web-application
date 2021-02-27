import React, { useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { Icon } from "leaflet"
import * as carparkData from "../data/carparks.json";

const parking = new Icon ({
  iconUrl: "/images/parking.png",
  iconSize: [25,25]
})

function Map(){
  const [activeCarpark, setActiveCarpark] = useState(null);

  return(
  <div  className="map">
    <MapContainer center ={[52.382921, -1.564097]} zoom ={15}>
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        minZoom = {13}
      />

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

export default Map