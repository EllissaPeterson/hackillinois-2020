import React from 'react';
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';

export default class OptionsPageCountries extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

        };
    }

    render() {
        return (
            <header className="App-header">
                Select country...
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <Form>
                    <FormGroup>
                        <Input type="select" name="select" id="select">
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </Input>
                    </FormGroup>
                </Form>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
                <div style={{width:"70%"}}>
                <Button block outline size="lg" href="/map">Enter</Button>
                </div>

            </header>
        )
    }
}