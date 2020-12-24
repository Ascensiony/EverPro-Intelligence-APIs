import React from 'react'
import classes from './Header.module.scss'
import NavigationItem from "./NavigationItem/NavigationItem";

const Header = (props) => {

   return (
      <ul className={classes.Header}>
         <span>EVER <span>PRO</span></span>
         <NavigationItem link="/" exact>MAIN</NavigationItem>
         <NavigationItem link="/home">HOME</NavigationItem>
         <NavigationItem link="/about">ABOUT</NavigationItem>
      </ul>
   )
}

export default Header
