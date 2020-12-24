import * as actionTypes from "./actionTypes";


export const setUIPreference = (nameClicked) => {
   return {
      type: actionTypes.SET_UI_PREFERENCE,
      nameClicked: nameClicked,
   }
}
