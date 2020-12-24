import React, {Component} from 'react'
import classes from './ConsumerSection.module.scss'
import Typist from 'react-typist';
import TypistLoop from 'react-typist-loop'
import table from '../../../../assets/svg/table.svg'
import ApplePhone from "./Phones/ApplePhone";
import PocoPhone from "./Phones/PocoPhone";
import HonorPhone from "./Phones/HonorPhone";
import RedmiPhone from "./Phones/RedmiPhone";
import SamsungPhone from "./Phones/SamsungPhone";
import VivoPhone from "./Phones/VivoPhone"
import person from "../../../../assets/images/person.png"
import {faArrowRight} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import Modal from "./Modal/Modal";
import SearchBar from "../../../../component/Reuse/SearchBar/SearchBar";

class ConsumerSection extends Component {

   state = {
      showModal: false,
   }

   buttonClickHandler = () => {
      this.setState({showModal: true})
   }

   buttonCancelHandler = () => {
      this.setState({showModal: false})
   }

   render() {

      const data = [
         {
            id: 1,
            text: (
               <div className={classes.headline}>
                  Find &nbsp;The &nbsp;<b>BEST PRODUCT </b>Here
               </div>
            )
         },
         {
            id: 2,
            text: (
               <div className={classes.headline}>
                  Reduce Your Search Time from <strike> DAYS </strike> to <b>MINUTES</b>
               </div>
            )
         },
         {
            id: 3,
            text: (
               <div className={classes.headline}>
                  Save Your <b>Money</b> & <b>Time</b>
               </div>
            )
         },
         {
            id: 4,
            text: (
               <div className={classes.headline}>
                  We Help You Take Decision <b>Early</b>
               </div>
            )
         }
      ]

      return (
         <div className={classes.consumerSection}>
            <TypistLoop interval={3000}>
               {data.map(text => <Typist
                  key={text.id}
                  cursor={{
                     show: false,
                  }}
               >{text.text}
               </Typist>)}
            </TypistLoop>
            <button className={classes.search} onClick={this.buttonClickHandler}>
               Get Started<FontAwesomeIcon icon={faArrowRight} className={classes.arrow}/>
            </button>
            <Modal show={this.state.showModal} modalClosed={this.buttonCancelHandler}>
               <SearchBar/>
            </Modal>
            <div className={classes.image}>
               <PocoPhone/>
               <ApplePhone/>
               <HonorPhone/>
               <RedmiPhone/>
               <SamsungPhone/>
               <VivoPhone/>
               <img src={table} alt={'table'}/>
               <img src={person} alt={'person'} className={classes.person}/>
            </div>
         </div>
      )
   }
}

export default ConsumerSection
