import H2 from '../index';

import expect from 'expect';
import { shallow } from 'enzyme';
import React from 'react';

describe('<H2 />', () => {
  it('should adopt the className', () => {
    const renderedComponent = shallow(<H2 className="test" />);
    expect(renderedComponent.find('h2').hasClass('test')).toEqual(true);
  });

  it('should render its text', () => {
    const children = 'Text';
    const renderedComponent = shallow(
      <H2>{children}</H2>
    );
    expect(renderedComponent.contains(children)).toEqual(true);
  });
});
