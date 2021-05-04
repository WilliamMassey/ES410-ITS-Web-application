import React, { Component } from "react";
import PrivNavbar from "./privnavbar.component";

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
         <div className="account-title">
            <PrivNavbar/>
               
         </div>
      )
   }
}

export default MyBookings