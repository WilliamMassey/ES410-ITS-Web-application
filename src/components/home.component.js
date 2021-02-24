import React, { useState } from "react";
import Map from "./map.component"

function Home() {
        return (
            <div>
                <div className="home-title">
                    <h1>Homepage</h1>
                </div>
                <div  className="map">
                    <Map />
                </div>
            </div>
        );
    }


export default Home