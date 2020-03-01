import React from 'react';
import {Button} from 'reactstrap';
import RadioButtonsOptions from '../options/RadioButtonsOptions';

export default class OptionsPage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

        };
    }

    render() {
        return (
            <header className="App-header">
                <RadioButtonsOptions/>
            </header>
        )
    }
}