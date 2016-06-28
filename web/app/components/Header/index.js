import React from 'react';

import Img from 'components/Img';
import A from 'components/A';
import Logo from './logo.png';
import styles from './styles.css';

function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.logoWrapper}>
        <A href="/" className={styles.link}>
          <Img src={Logo} alt="Sitterfied" className={styles.logo} />
        </A>
      </div>
    </header>
  );
}

export default Header;
