import React from 'react';
import {Button} from 'reactstrap';

export default class TitlePage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

        };
    }

    render() {
        return (
            <header className="App-header">
                Title Page
                <Button href="/options">Enter</Button>
            </header>
        )
    }
}