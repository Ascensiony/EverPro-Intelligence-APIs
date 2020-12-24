import React, {Component} from 'react'
import classes from './Modal.module.scss'

class Modal extends Component {

   state = {

   }

   render() {
      return (
         <div className={classes.Modal}>
            <div className={classes.content}>
               Hey
            </div>
         </div>
      )
   }
}

export default Modal
