import React, {Component} from 'react'
import classes from './Testimonial.module.scss'
import TestimonialCard from "./TestimonialCard/TestimonialCard";
import Carousel from '@brainhubeu/react-carousel';
import '@brainhubeu/react-carousel/lib/style.css';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faQuoteLeft, faQuoteRight} from "@fortawesome/free-solid-svg-icons";

class Testimonial extends Component {
   render() {
      return (
         <div className={classes.outer}>
            <h1>WHAT <span>OUR CUSTOMERS</span> SAY</h1>
            <div className={classes.testimonials}>
               <div className={classes.inner}>
                  <p className={classes.first}><FontAwesomeIcon icon={faQuoteLeft}/></p>
                  <p className={classes.second}><FontAwesomeIcon icon={faQuoteRight}/></p>
                  <Carousel
                     className={classes.carousel}
                     arrows
                     animationSpeed={1500}
                     autoPlay={4000}
                     stopAutoPlayOnHover
                     clickToChange
                     centered
                     infinite
                  >
                     <TestimonialCard/>
                     <TestimonialCard/>
                     <TestimonialCard/>
                  </Carousel>
               </div>
            </div>

         </div>
      )
   }
}

export default Testimonial
