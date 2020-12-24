import React, {Component} from 'react'
import classes from './Card.module.scss'
import {Link} from "react-router-dom";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faArrowRight} from "@fortawesome/free-solid-svg-icons";

class Card extends Component {
   render() {
      return (
         <Link className={classes.card}>
            <p className={classes.one}>{this.props.name}</p>
            <p className={classes.desc}>{this.props.desc}</p>
            <span>{this.props.num}</span>
            <p className={classes.icon}><FontAwesomeIcon icon={faArrowRight}/></p>
         </Link>
      )
   }
}

export default Card
