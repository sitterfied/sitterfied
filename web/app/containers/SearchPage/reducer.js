/*
 *
 * SearchPage reducer
 *
 */

import { fromJS } from 'immutable';
import {
  LOAD_SITTERS_SUCCESS,
  LOAD_SITTERS,
  LOAD_SITTERS_ERROR,
  APPLY_FILTER,
  REMOVE_FILTER,
} from './constants';
import {
  ADD_SITTER_TO_TEAM,
} from '../SitterCard/constants';
import sitterCardReducer from '../SitterCard/reducer';
import {
  REMOVE_SITTER_FROM_TEAM,
} from '../SitterTeam/constants';
import sitterTeamReducer from '../SitterTeam/reducer';

const initialState = fromJS({
  loading: false,
  error: false,
  sitters: false,
  appliedFilters: fromJS({}),
  sitterTeam: fromJS([]),
});

function searchPageReducer(state = initialState, action) {
  switch (action.type) {
    case LOAD_SITTERS:
      return state
        .set('loading', true)
        .set('error', false)
        .set('sitters', false);
    case APPLY_FILTER:
      return state
        .set('loading', true)
        .set('error', false)
        .set('sitters', false)
        .updateIn(['appliedFilters', action.name], fromJS([]), arr => arr.push(action.value));
    case REMOVE_FILTER:
      return state
        .set('loading', true)
        .set('error', false)
        .set('sitters', false)
        .updateIn(['appliedFilters', action.name], arr => arr.filter(val => val !== action.value));
    case LOAD_SITTERS_SUCCESS:
      return state
        .set('loading', false)
        .set('sitters', action.sitters);
    case LOAD_SITTERS_ERROR:
      return state
        .set('error', action.error)
        .set('loading', false);
    case ADD_SITTER_TO_TEAM:
      return sitterCardReducer(state, action);
    case REMOVE_SITTER_FROM_TEAM:
      return sitterTeamReducer(state, action);
    default:
      return state;
  }
}

export default searchPageReducer;
