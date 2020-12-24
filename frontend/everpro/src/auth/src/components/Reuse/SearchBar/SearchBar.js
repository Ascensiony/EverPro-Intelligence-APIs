import React, {Component} from 'react'
import classes from './SearchBar.module.scss'
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faSearch} from "@fortawesome/free-solid-svg-icons";

class SearchBar extends Component {
   render() {
      return (
         <div className={classes.searchBar}>
            <p>Search Your Product</p>
            <form>
               <FontAwesomeIcon icon={faSearch} className={classes.icon}/>
               <input type="text" placeholder="Product name .." name="search"/>
               <button type="submit">
                  <span>Search</span>
               </button>
            </form>
         </div>
      )
   }
}

export default SearchBar

