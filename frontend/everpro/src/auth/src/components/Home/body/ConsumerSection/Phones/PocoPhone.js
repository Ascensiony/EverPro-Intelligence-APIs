import React, {Component} from 'react'
import classes from "./Phone.module.scss"
import Poco from "../../../../Reuse/SVG/Poco";

class PocoPhone extends Component {
   state = {
      isHovered: false,
   }

   handleMouseEnter = () => {
      this.setState({isHovered: true})
   }

   handleMouseLeave = () => {
      this.setState({isHovered: false})
   }

   render() {
      return (
         <Poco
            className={classes.poco}
            color={this.state.isHovered ? '#00ff00' : '#b0b0b0'}
            onMouseEnter={this.handleMouseEnter}
            onMouseLeave={this.handleMouseLeave}
         />
      )
   }
}

export default PocoPhone
