/* eslint-disable react/prefer-stateless-function */

import React from 'react';
import { connect } from 'react-redux';

import { createSelector } from 'reselect';

import {
  selectSitterTeam,
} from '../SitterTeam/selectors';

import { addSitterToTeam } from './actions';

import GridListItem from 'components/GridListItem';
import Img from 'components/Img';
import H2 from 'components/H2';
import A from 'components/A';
import Icon from 'components/Icon';

import styles from './styles.css';

export class SitterCard extends React.Component {

  render() {
    const { item, sitterTeam, handleSitterSelect } = this.props;
    const isInSitterTeam = sitterTeam.find(teamMember => teamMember.id === item.id);
    const content = (
      <div className={styles.wrapper}>
        <Img className={styles.avatar} src={item.avatar} alt={`${item.first_name} ${item.last_name}`} />
        <H2 className={styles.name}>{`${item.first_name} ${item.last_name}`}</H2>
        <ul className={styles.details}>
          <li>{item.city}, {item.state}</li>
          <li>{item.sitter_teams.length} sitter teams</li>
          <li>{item.reviews.length} reviews</li>
        </ul>
        <A className={styles.addSitter} onClick={() => handleSitterSelect(item.id, `${item.first_name} ${item.last_name}`)}>
          <Icon icon={isInSitterTeam ? 'ok' : 'add'} className={!isInSitterTeam ? styles.rotate : null} />
          {isInSitterTeam ? 'In your' : 'Add to'} sitter team
        </A>
      </div>
    );

    return (
      <GridListItem key={`sitter-${item.id}`} content={content} />
    );
  }
}

SitterCard.propTypes = {
  item: React.PropTypes.object,
  sitterTeam: React.PropTypes.array,
  handleSitterSelect: React.PropTypes.func,
};

function mapDispatchToProps(dispatch) {
  return {
    handleSitterSelect: (id, name) => dispatch(addSitterToTeam(id, name)),
    dispatch,
  };
}

export default connect(createSelector(
  selectSitterTeam(),
  (sitterTeam) => ({ sitterTeam })
), mapDispatchToProps
)(SitterCard);
