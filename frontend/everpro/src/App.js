import './App.css';
import React, {Component} from "react";
import {Redirect, Route, Switch, withRouter} from "react-router";
import {connect} from "react-redux";
import Main from "./container/Main/Main";
import Home from "./container/Home/Home";
import ServiceDescription from "./container/Service Description/ServiceDescription";
import SearchResult from "./container/Search Result/SearchResult";
import ProductReview from "./container/Product Review/ProductReview";
import Location from "./container/Location/Location";
import About from "./container/About/About";
import Feedback from "./container/Feedback/Feedback";
import Subscription from "./container/Subscription/Subscription";

/* if it doesn't work , change it to react-router-dom*/


class App extends Component {
   render() {

      let routes = (
         <Switch>
            {/*<Route path="/auth" component={asyncAuth}/>*/}
            <Route path="/service_description" exact component={ServiceDescription}/>
            <Route path="/search_result" exact component={SearchResult}/>
            <Route path="/product_review" exact component={ProductReview}/>
            <Route path="/location" exact component={Location}/>
            <Route path="/about" exact component={About}/>
            <Route path="/home" exact component={Home}/>
            <Route path="/feedback" exact component={Feedback}/>
            <Route path="/subscription" exact component={Subscription}/>
            <Route path="/" exact component={Main}/>
            <Redirect to={'/'}/>
         </Switch>
      )

      return (
         <div>
            {routes}
         </div>
      )
   }
}

const mapStateToProps = state => {
   return {
      // isAuthenticated: state.auth.token !== null,
   }
}

const mapDispatchToProps = dispatch => {
   return {
      // onTryAutoSignUp: () => dispatch(actions.authCheckState())
   }
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(App))
