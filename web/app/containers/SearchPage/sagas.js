import { take, call, put, select } from 'redux-saga/effects';

import { LOAD_SITTERS, APPLY_FILTER, REMOVE_FILTER } from 'containers/SearchPage/constants';
import { sittersLoaded, sitterLoadingError } from 'containers/SearchPage/actions';

import request from 'utils/request';
import { selectFilters } from 'containers/SearchPage/selectors';

export default [
  getSitterData,
];

export function* getSitterData() {
  while (yield take([LOAD_SITTERS, APPLY_FILTER, REMOVE_FILTER])) {
    const appliedFilters = yield select(selectFilters());
    let query = '';
    Object.keys(appliedFilters).forEach((type) => {
      if (appliedFilters[type].length > 0) {
        query += `${type}=${appliedFilters[type].join()}&`;
      }
    });
    query = query.slice(0, -1);
    const requestURL = `/api/parents/59/sitters/${query ? `?${encodeURI(query)}` : ''}`;
    const sitters = yield call(request, requestURL);
    if (sitters.err === undefined || sitters.err === null) {
      yield put(sittersLoaded(sitters.data, appliedFilters));
    } else {
      yield put(sitterLoadingError(sitters.err));
    }
  }
}
