/*
 *
 * SitterTeam reducer
 *
 */

import {
  REMOVE_SITTER_FROM_TEAM,
} from './constants';

const sitterTeamReducer = (state, action) => {
  switch (action.type) {
    case REMOVE_SITTER_FROM_TEAM:
      return state
        .updateIn(['sitterTeam'], arr => arr.filter(val => val.get('id') !== action.id));
    default:
      return state;
  }
};

export default sitterTeamReducer;
