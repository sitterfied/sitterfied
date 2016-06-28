import React from 'react';

import styles from './styles.css';

function GridListItem(props) {
  return (
    <div className={styles.item}>
        {props.content}
    </div>
  );
}

GridListItem.propTypes = {
  content: React.PropTypes.any,
};

export default GridListItem;
