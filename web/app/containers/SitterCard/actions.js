/*
 *
 * SitterCard actions
 *
 */

import {
  ADD_SITTER_TO_TEAM,
} from './constants';

/**
 * Add a sitter to a team
 */
export function addSitterToTeam(id, name) {
  return {
    type: ADD_SITTER_TO_TEAM,
    id,
    name,
  };
}
