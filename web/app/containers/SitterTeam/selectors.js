import { createSelector } from 'reselect';
import { selectSearchPage } from '../SearchPage/selectors';

const selectSitterTeam = () => createSelector(
  selectSearchPage(),
  (sitterTeamState) => sitterTeamState.get('sitterTeam').toJS()
);

export {
  selectSitterTeam,
};
