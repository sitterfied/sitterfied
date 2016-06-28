/*
 *
 * SearchPage actions
 *
 */

import {
  LOAD_SITTERS,
  LOAD_SITTERS_SUCCESS,
  LOAD_SITTERS_ERROR,
  APPLY_FILTER,
  REMOVE_FILTER,
} from './constants';

/**
 * Load the sitters
 */
export function loadSitters() {
  return {
    type: LOAD_SITTERS,
  };
}

/**
 * Apply a filter
 */
export function applyFilter(name, value) {
  return {
    type: APPLY_FILTER,
    name,
    value,
  };
}

/**
 * Remove a filter
 */
export function removeFilter(name, value) {
  return {
    type: REMOVE_FILTER,
    name,
    value,
  };
}

/**
 * Dispatched when the sitters are loaded
 */
export function sittersLoaded(sitters, appliedFilters) {
  return {
    type: LOAD_SITTERS_SUCCESS,
    sitters,
    appliedFilters,
  };
}

/**
 * Dispatched when loading of the sitters fails
 */
export function sittersLoadingError(error) {
  return {
    type: LOAD_SITTERS_ERROR,
    error,
  };
}
