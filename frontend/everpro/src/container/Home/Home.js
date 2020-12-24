import React, {Component} from 'react'
import Layout from "../../component/Layout/Layout";
import ConsumerSection from "./body/ConsumerSection/ConsumerSection";
import BusinessSection from "./body/BusinessSection/BusinessSection";
import Testimonial from "./body/Testimonial/Testimonial";
import {connect} from "react-redux";

class Home extends Component {

   state = {
      name: null,
   }

   render() {

      let layout = null;
      if (this.props.preferredName === 'CONSUMER') {
         layout = (
            <Layout>
               <ConsumerSection/>
               <BusinessSection/>
               <Testimonial/>
            </Layout>
         )
      } else {
         layout = (
            <Layout>
               <BusinessSection/>
               <ConsumerSection/>
               <Testimonial/>
            </Layout>
         )
      }


      return layout
   }
}

const mapStateToProps = state => {
   return {
      preferredName: state.home.name,
   }
}

export default connect(mapStateToProps)(Home)
