/*
 *
 * SearchPage
 *
 */

import React from 'react';
import { connect } from 'react-redux';

import { createSelector } from 'reselect';

import {
  selectSitters,
  selectFilters,
  selectLoading,
  selectError,
} from './selectors';

import { loadSitters, applyFilter, removeFilter } from './actions';

import Filter from 'components/Filter';
import GridList from 'components/GridList';
import SitterCard from 'containers/SitterCard';
import SitterTeam from 'containers/SitterTeam';
import LoadingIndicator from 'components/LoadingIndicator';

import styles from './styles.css';
import languages from './languages';
import education from './education';

class SearchPage extends React.Component {

  constructor() {
    super();
    this.state = {
      openFilter: null,
    };
  }

  componentWillMount() {
    this.props.loadSitters();
  }

  handleFilterVisibility = (name) => {
    if (this.state.openFilter === name) {
      this.setState({ openFilter: null });
    } else {
      this.setState({ openFilter: name });
    }
  };

  render() {
    let sitterResults = null;
    let filters = null;
    const filterData = { languages, education };

    if (this.props.loading) {
      sitterResults = (<LoadingIndicator />);
    } else if (this.props.sitters !== false) {
      sitterResults = (<GridList items={this.props.sitters} component={SitterCard} />);
    }

    filters = Object.keys(filterData).map((key) => {
      let title = key.charAt(0).toUpperCase() + key.substr(1);
      if (this.props.appliedFilters[key] && this.props.appliedFilters[key].length > 0) {
        title += ` (${this.props.appliedFilters[key].length})`;
      }

      return (
        <Filter
          key={key}
          name={key}
          title={title}
          data={filterData[key]}
          selected={this.props.appliedFilters[key] ? this.props.appliedFilters[key] : []}
          isOpen={this.state.openFilter === key}
          handleVisibility={this.handleFilterVisibility}
          handleFilterSelect={this.props.handleFilterSelect}
          handleFilterDeselect={this.props.handleFilterDeselect}
        />
      );
    });

    return (
      <div>
        <div className={styles.filters}>
          {filters}
        </div>
        <div className={styles.main}>
          <SitterTeam />
          <div className={styles.results}>
            {sitterResults}
          </div>
        </div>
      </div>
    );
  }
}

SearchPage.propTypes = {
  loading: React.PropTypes.bool,
  error: React.PropTypes.oneOfType([
    React.PropTypes.object,
    React.PropTypes.bool,
  ]),
  sitters: React.PropTypes.oneOfType([
    React.PropTypes.array,
    React.PropTypes.bool,
  ]),
  appliedFilters: React.PropTypes.oneOfType([
    React.PropTypes.object,
  ]),
  loadSitters: React.PropTypes.func,
  handleFilterSelect: React.PropTypes.func,
  handleFilterDeselect: React.PropTypes.func,
};

function mapDispatchToProps(dispatch) {
  return {
    handleFilterSelect: (name, value) => dispatch(applyFilter(name, value)),
    handleFilterDeselect: (name, value) => dispatch(removeFilter(name, value)),
    loadSitters: () => dispatch(loadSitters()),
    dispatch,
  };
}

export default connect(createSelector(
  selectSitters(),
  selectFilters(),
  selectLoading(),
  selectError(),
  (sitters, appliedFilters, loading, error) => ({ sitters, appliedFilters, loading, error })
), mapDispatchToProps)(SearchPage);
