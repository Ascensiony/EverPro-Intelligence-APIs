import React, {Component} from 'react'
import classes from "./Phone.module.scss"
import Apple from "../../../../Reuse/SVG/Apple";

class ApplePhone extends Component {
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
         <Apple
            className={classes.apple}
            color={this.state.isHovered ? '#00ff00' : '#b0b0b0'}
            onMouseEnter={this.handleMouseEnter}
            onMouseLeave={this.handleMouseLeave}
         />
      )
   }
}

export default ApplePhone
