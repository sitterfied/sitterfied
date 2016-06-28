import { createSelector } from 'reselect';

const selectSearchPage = () => (state) => state.get('searchPage');

const selectSitters = () => createSelector(
  selectSearchPage(),
  (searchState) => searchState.get('sitters')
);

const selectLoading = () => createSelector(
  selectSearchPage(),
  (searchState) => searchState.get('loading')
);

const selectError = () => createSelector(
  selectSearchPage(),
  (searchState) => searchState.get('error')
);

const selectFilters = () => createSelector(
  selectSearchPage(),
  (searchState) => searchState.get('appliedFilters').toJS()
);

export {
  selectSearchPage,
  selectSitters,
  selectLoading,
  selectError,
  selectFilters,
};
