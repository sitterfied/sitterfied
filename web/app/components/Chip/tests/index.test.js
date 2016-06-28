/**
 * Testing our link component
 */

import Chip from '../index';

import expect from 'expect';
import { shallow } from 'enzyme';
import React from 'react';

describe('<Chip />', () => {
  it('should render its children', () => {
    const children = 'Test';
    const renderedComponent = shallow(
      <Chip>
        {children}
      </Chip>
    );
    expect(renderedComponent.contains(children)).toEqual(true);
  });

  it('should adopt the className', () => {
    const renderedComponent = shallow(<Chip className="test" />);
    expect(renderedComponent.find('div').hasClass('test')).toEqual(true);
  });

  it('should handle click events', () => {
    const onClickSpy = expect.createSpy();
    const renderedComponent = shallow(<Chip handleClick={onClickSpy} />);
    renderedComponent.simulate('click');
    expect(onClickSpy).toHaveBeenCalled();
  });
});
