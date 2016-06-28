/**
 *
 * App.react.js
 *
 * This component is the skeleton around the actual pages, and should only
 * contain code that should be seen on all pages. (e.g. navigation bar)
 */

import React from 'react';

// Import the CSS reset, which HtmlWebpackPlugin transfers to the build folder
import 'sanitize.css/sanitize.css';

import Header from 'components/Header';

import styles from './styles.css';

function App(props) {
  return (
    <div>
      <Header />
      <div className={styles.mainContent}>
        {props.children}
      </div>
    </div>
  );
}

App.propTypes = {
  children: React.PropTypes.node,
};

export default App;
