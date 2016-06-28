import expect from 'expect';
import { shallow } from 'enzyme';
import React from 'react';

import Header from '../index';
import Img from 'components/Img';

describe('<Header />', () => {
  it('should render the logo', () => {
    const renderedComponent = shallow(<Header />);
    expect(renderedComponent.find(Img)).toExist();
  });
});
