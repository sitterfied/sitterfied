/**
 * A chip
 */

import React, { PropTypes } from 'react';

import styles from './styles.css';

function Chip(props) {
  return (
    <div onClick={props.handleClick} className={`${styles.chip} ${props.className}`}>
      {props.children}
    </div>
  );
}

Chip.propTypes = {
  className: PropTypes.string,
  handleClick: PropTypes.func.isRequired,
  children: PropTypes.node.isRequired,
};

export default Chip;
