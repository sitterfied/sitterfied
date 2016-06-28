/*
 *
 * SitterCard reducer
 *
 */

import { fromJS } from 'immutable';
import {
  ADD_SITTER_TO_TEAM,
} from './constants';

const sitterCardReducer = (state, action) => {
  switch (action.type) {
    case ADD_SITTER_TO_TEAM:
      return state
        .update('sitterTeam', fromJS([]), arr => arr.push(fromJS({ id: action.id, name: action.name })));
    default:
      return state;
  }
};

export default sitterCardReducer;
