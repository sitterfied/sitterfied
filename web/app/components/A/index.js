/**
 * A link to a certain page, an anchor tag
 */

import React, { PropTypes } from 'react';

import styles from './styles.css';

function A(props) {
  return (
    <a
      className={`${styles.link} ${props.className}`}
      {...props}
    />
  );
}

A.propTypes = {
  className: PropTypes.string,
  href: PropTypes.string,
  target: PropTypes.string,
  children: PropTypes.node.isRequired,
};

export default A;
