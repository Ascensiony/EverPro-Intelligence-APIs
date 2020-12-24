import React, {Component} from 'react'

import style from './Modal.module.css'
import Backdrop from "../Backdrop/Backdrop";
import Aux from "../../../../hoc/Aux/Aux";


class Modal extends Component {

   shouldComponentUpdate(nextProps, nextState, nextContext) {
      return nextProps.show !== this.props.show || nextProps.children !== this.props.children
   }

   render() {
      return (
         <Aux>
            <Backdrop show={this.props.show} clicked={this.props.modalClosed}/>
            <div className={style.Modal}
                 style={{
                    transform: this.props.show ? 'scale(1)' : 'scale(0)',
                    opacity: this.props.show ? '1' : '0',
                 }}
            >{this.props.children}
            </div>
         </Aux>
      )
   }
}

export default Modal
