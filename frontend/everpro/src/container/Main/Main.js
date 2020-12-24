import React, {Component} from 'react'
import Square from "../../component/Reuse/Square/Square";
import classes from './Main.module.scss'
import {Link} from "react-router-dom";
import {connect} from "react-redux";
import * as actions from "../../store/actions/home";


class Main extends Component {

   businessClicked = () => {
      this.props.setUI_Preference('BUSINESS')
   }

   consumerClicked = () => {
      this.props.setUI_Preference('CONSUMER')
   }

   render() {

      return (
         <div className={classes.Main}>
            <Link to={'/home'}><Square name={'BUSINESS'} clicked={this.businessClicked}/></Link>
            <Link to={'/home'}><Square name={'CONSUMER'} clicked={this.consumerClicked}/></Link>
         </div>
      )
   }
}

const mapDispatchToProps = dispatch => {
   return {
      setUI_Preference: (nameClicked) => dispatch(actions.setUIPreference(nameClicked))
   }
}

export default connect(null, mapDispatchToProps)(Main)
