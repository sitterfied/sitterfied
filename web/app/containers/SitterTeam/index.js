/* eslint-disable react/prefer-stateless-function */

import React from 'react';
import { connect } from 'react-redux';

import { createSelector } from 'reselect';

import {
  selectSitterTeam,
} from './selectors';

import { removeSitterFromTeam } from './actions';

import H2 from 'components/H2';
import Icon from 'components/Icon';
import Chip from 'components/Chip';

import styles from './styles.css';

export class SitterTeam extends React.Component {

  render() {
    const { sitterTeam, handleSitterRemoval } = this.props;
    let content = (<p className={styles.empty}>Your sitter team is empty! Add sitters from the list below.</p>);

    if (sitterTeam.length > 0) {
      content = sitterTeam.map((sitter) =>
        <Chip className={styles.sitterChip} key={sitter.id} handleClick={() => { handleSitterRemoval(sitter.id); }}>
          {sitter.name}
          <Icon icon="cancel" />
        </Chip>
      );
    }

    return (
      <div className={styles.wrapper}>
        <H2 className={styles.teamHeading}>Your Sitter Team</H2>
        {content}
      </div>
    );
  }
}

SitterTeam.propTypes = {
  sitterTeam: React.PropTypes.array,
  handleSitterRemoval: React.PropTypes.func,
};

function mapDispatchToProps(dispatch) {
  return {
    handleSitterRemoval: (id) => dispatch(removeSitterFromTeam(id)),
    dispatch,
  };
}

export default connect(createSelector(
  selectSitterTeam(),
  (sitterTeam) => ({ sitterTeam })
), mapDispatchToProps
)(SitterTeam);
