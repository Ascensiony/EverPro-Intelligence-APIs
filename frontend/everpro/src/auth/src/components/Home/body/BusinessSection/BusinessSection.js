import React from 'react'
import classes from './BusinessSection.module.scss'
import Card from "./Card/Card";

const BusinessSection = (props) => {

   return (
      <div className={classes.business}>
         <h1>OUR <br/><span>SERVICES</span></h1>
         <div className={classes.cards}>
            <Card
               desc={'This is short description'}
               name={'INVENTORY SCRAPING'} num={'01'}/>
            <Card
               desc={'This is short description'}
               name={'REVIEW SCRAPING'} num={'02'}/>
            <Card
               desc={'This is short description'}
               name={'COMPETITION TRACKING'} num={'03'}/>
            <Card
               desc={'This is short description'}
               name={'EVENT MANAGEMENT'} num={'04'}/>
         </div>
      </div>
   )
}

export default BusinessSection
