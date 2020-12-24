import React, {Component} from 'react'
import classes from './About.module.scss'
import team from '../../assets/images/team.png'
import aman from '../../assets/images/aman.png'
import akhil from '../../assets/images/akhil.png'
import abhishek from '../../assets/images/abhi.png'
import shivam from '../../assets/images/shiv.png'
import bipin from '../../assets/images/bip.png'
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faLink} from "@fortawesome/free-solid-svg-icons";
import Layout from "../../component/Layout/Layout";

class About extends Component {

   //  state = {
   //     x: 0,
   //     y: 0,
   //  }
   //
   //  handleMouseMove = e => {
   //   this.setState({
   //     x: e.clientX,
   //     y: e.clientY
   //   });
   // };

   render() {


      return (
         <Layout>
            <div className={classes.about}>
               <div className={classes.intro}>
                  <h1>ABOUT <span>US</span></h1>
                  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad adipisci atque dolorem eveniet facilis
                     laudantium nobis odit quos sed veniam! Adipisci beatae eligendi eum iusto minima, molestias quod
                     soluta tenetur.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad adipisci atque dolorem
                     eveniet facilis laudantium nobis odit quos sed veniam! Adipisci beatae eligendi eum iusto minima,
                     molestias quod
                     soluta tenetur.</p>
               </div>
               <img src={team} alt='team' className={classes.team_image}/>
            </div>
            <div className={classes.us}>
               <div className={classes.images}>
                  <p>OUR <span>TEAM</span></p>
                  <img src={abhishek} alt='abhishek' className={classes.abhishek}/>
                  <a href="https://www.linkedin.com/in/naklic0der/" target="_blank"><img src={aman} alt='aman' className={classes.aman}/></a>
                  <img src={akhil} alt='akhil' className={classes.akhil}/>
                  <img src={shivam} alt='shivam' className={classes.shivam}/>
                  <img src={bipin} alt='bipin' className={classes.bipin}/>
               </div>
               {/*<div className={classes.desc}>*/}
               {/*   <h1>Aman Shrivastava</h1>*/}
               {/*   <h3>Front-end Developer</h3>*/}
               {/*   <p>HI I AM AMAN Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi, eveniet, rerum?*/}
               {/*      Accusantium amet aperiam corporis exercitationem itaque modi pariatur, quae repellat. Accusantium*/}
               {/*      ex ipsa libero nisi obcaecati quibusdam repellendus temporibus.</p>*/}
               {/*   <div className={classes.social}>*/}
               {/*      <FontAwesomeIcon icon={faLink} className={classes.social_icon}/>*/}
               {/*      <FontAwesomeIcon icon={faLink} className={classes.social_icon}/>*/}
               {/*      <FontAwesomeIcon icon={faLink} className={classes.social_icon}/>*/}
               {/*   </div>*/}
               {/*</div>*/}
            </div>
         </Layout>
      )
   }
}

export default About
