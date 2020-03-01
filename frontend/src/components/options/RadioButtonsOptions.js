import React from 'react';
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';

class RadioButtonsOptions extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

        };
    }

    render() {
        return (
            <header className="App-header">
                Choose map options...
                <Form inline>
                    <FormGroup className="form">
                        <row>
                            <Label>
                                <Input type="radio" name="radio1" />{' '}
                                Country View
                            </Label>
                            <br/>
                            <Label>
                                <Input type="radio" name="radio1" />{' '}
                                World View
                            </Label>
                        </row>
                    </FormGroup>
                    <FormGroup className="form">
                        <row>
                            <Label>
                                <Input type="radio" name="radio2" />{' '}
                                Density Map
                            </Label>
                            <br/>
                            <Label>
                                <Input type="radio" name="radio2" />{' '}
                                Pinpoints Map
                            </Label>
                        </row>
                    </FormGroup>
                </Form>
                <Button outline block href="/options/countries" size="lg">Enter</Button>
            </header>
        )
    }
}

export default RadioButtonsOptions