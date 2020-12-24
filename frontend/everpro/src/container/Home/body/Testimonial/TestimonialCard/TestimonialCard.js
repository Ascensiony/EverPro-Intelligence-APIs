import React from 'react'
import classes from './TestimonialCard.module.scss'
import {faUserCircle} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

const TestimonialCard = (props) => {

   return (
      <div className={classes.testCard}>
         <FontAwesomeIcon icon={faUserCircle} className={classes.profile}/>
         <div className={classes.data}>
            <p>Make it specific. If your positive feedback is vague, they won't know which of their skills are good
               <span>- Aman Shrivastava</span>
            </p>

         </div>

      </div>
   )
}

export default TestimonialCard
