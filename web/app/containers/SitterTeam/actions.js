/*
 *
 * SitterTeam actions
 *
 */

import {
  REMOVE_SITTER_FROM_TEAM,
} from './constants';

/**
 * Remove sitter from a team
 */
export function removeSitterFromTeam(id) {
  return {
    type: REMOVE_SITTER_FROM_TEAM,
    id,
  };
}
