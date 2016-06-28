import GridListItem from '../index';

import expect from 'expect';
import { shallow } from 'enzyme';
import React from 'react';

describe('<GridListItem />', () => {
  it('should render the content passed to it', () => {
    const content = 'Hello world!';
    const renderedComponent = shallow(
      <GridListItem content={content} />
    );
    expect(renderedComponent.contains(content)).toEqual(true);
  });
});
