import React, {Component} from 'react'
import classes from "./Phone.module.scss"
import Redmi from "../../../../../component/Reuse/SVG/Redmi";

class RedmiPhone extends Component {
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
         <Redmi
            className={classes.redmi}
            color={this.state.isHovered ? '#00ff00' : '#b0b0b0'}
            onMouseEnter={this.handleMouseEnter}
            onMouseLeave={this.handleMouseLeave}
         />
      )
   }
}

export default RedmiPhone
