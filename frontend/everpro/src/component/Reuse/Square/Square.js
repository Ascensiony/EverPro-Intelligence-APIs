import React from 'react'
import classes from './Square.module.scss'

const Square = (props) => {

   return (
      <div className={classes.Square} onClick={props.clicked}>
         <p>{props.name} </p>
      </div>
   )
}

export default Square
