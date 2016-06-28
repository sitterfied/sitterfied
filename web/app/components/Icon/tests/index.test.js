/**
 * Testing our icon component
 */

import Icon from '../index';

import expect from 'expect';
import { shallow } from 'enzyme';
import React from 'react';

describe('<Icon />', () => {
  it('should adopt the className', () => {
    const renderedComponent = shallow(<Icon className="test" icon="foo" />);
    expect(renderedComponent.closest('i').hasClass('test')).toEqual(true);
  });
});
