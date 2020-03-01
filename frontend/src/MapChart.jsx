import React, { Component, useEffect, useState } from "react";
import { csv } from "d3-fetch";

import { scaleLinear, scaleLog } from "d3-scale";
import {
  ComposableMap,
  Geographies,
  Geography,
  Sphere,
  Graticule
} from "react-simple-maps";


export default class MapChart extends Component {
  
  

  constructor(props){
    super(props);
    this.state = {
        userData: null,
    };
  }


  render(){
    const geoUrl = "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";

    const colorScale = scaleLog()
    .domain([0, 90000])
    .range(["#73956F", "#95D7AE"]);

    var data = this.props.mapdata


    return (
      <ComposableMap
        projectionConfig={{
          rotate: [-10, 0, 0],
          scale: 147
        }}
      >
        <Sphere stroke="#E4E5E6" strokeWidth={0.5} />
        <Graticule stroke="#E4E5E6" strokeWidth={0.5} />
        {data.length > 0 && (
          <Geographies geography={geoUrl}>

            {({ geographies }) =>
              geographies.map(geo => {
                
                const d = data.find(s => s.ISO3 === geo.properties.ISO_A3);
                console.log(d)
                return (
                  <Geography
                    key={geo.rsmKey}
                    geography={geo}
                    fill={d ? colorScale(d["Confirmed"]) : "#F5F4F6"}
                  />
                );
              })
            }
          </Geographies>
        )}
      </ComposableMap>
    );


  }    
}
