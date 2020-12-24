import * as actionTypes from "../actions/actionTypes";

const initialState = {
   name: null,
}

const reducer = (state = initialState, action) => {
   switch (action.type) {
      case actionTypes.SET_UI_PREFERENCE:
         return {
            ...state,
            name: action.nameClicked,
         }
      default:
         return state
   }
}

export default reducer
