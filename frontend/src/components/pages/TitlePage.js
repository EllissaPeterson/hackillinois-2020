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
                <div className="title">
                    COVID-19
                </div>
                <br/>
                <Button size="lg" outline color="secondary" href="/options">Launch</Button>
            </header>
        )
    }
}