import React from 'react';

import Icon from 'components/Icon';

import styles from './styles.css';

export class Filter extends React.Component {

  toggleSelection = (name, value) => {
    const { selected, handleFilterSelect, handleFilterDeselect } = this.props;
    if (selected.indexOf(value) !== -1) {
      handleFilterDeselect(name, value);
    } else {
      handleFilterSelect(name, value);
    }
  };

  render() {
    const { name, title, data, selected, isOpen, handleVisibility } = this.props;
    let content = (<div></div>);

    if (data) {
      content = data.map((item, index) =>
        <div key={index} className={styles.item} onClick={() => this.toggleSelection(name, item.key)}>
          <Icon icon={selected.indexOf(item.key) !== -1 ? 'checkedbox' : 'checkbox'} className={styles.filterCheckbox} />
          {item.value}
        </div>
      );
    }

    return (
      <div className={[styles.wrapper, isOpen ? styles.open : ''].join(' ')}>
        <div className={styles.title} onClick={() => handleVisibility(name)}>
          {title}
          <Icon icon="arrow" className={styles.filterArrow} />
        </div>
        <div className={styles.items}>
          {content}
        </div>
      </div>
    );
  }
}

Filter.propTypes = {
  name: React.PropTypes.string.isRequired,
  title: React.PropTypes.string.isRequired,
  data: React.PropTypes.array.isRequired,
  selected: React.PropTypes.array,
  isOpen: React.PropTypes.bool,
  handleVisibility: React.PropTypes.func.isRequired,
  handleFilterSelect: React.PropTypes.func.isRequired,
  handleFilterDeselect: React.PropTypes.func.isRequired,
};

export default Filter;
