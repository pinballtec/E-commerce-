import { createStore, combineReducers, applyMiddleware } from 'redux';
import  thunk  from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'

const CountReducer = (state = 0, action) => {
    switch (action.type) {
      case "ADD":
        return state + 1;
      default:
        return state;
    }
  };

const rootReducer = combineReducers({
    count: CountReducer
})

const initialState = {}

const middleware = [thunk]

const store = createStore(rootReducer, initialState, 
    composeWithDevTools(applyMiddleware(...middleware)));

export default store;