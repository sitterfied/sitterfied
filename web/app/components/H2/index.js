import React from 'react';

import styles from './styles.css';

function H2(props) {
  const { className, ...other } = props;
  return (
    <h2 {...other} className={`${styles.heading2} ${className}`} />
  );
}

H2.propTypes = {
  className: React.PropTypes.string,
};

export default H2;
