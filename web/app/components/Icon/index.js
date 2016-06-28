/**
 * An icon
 */

import React, { PropTypes } from 'react';

import styles from './styles.css';

function Icon(props) {
  const { icon, className } = props;
  const classNames = `${styles.icon} ${styles[icon]} ${className}`;

  return (
    <i className={classNames}></i>
  );
}

Icon.propTypes = {
  icon: PropTypes.string.isRequired,
  className: PropTypes.string,
};

export default Icon;
