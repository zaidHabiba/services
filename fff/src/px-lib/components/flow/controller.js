import * as React from "react";

export class FormController extends React.Component {

    state = {
        validatorsResult: []
    };

    constructor(props) {
        super(props);
        props.loadForm(this);
    }

    onChange = (field) => {
        if (this.props.changeCallBack) {
            this.props.changeCallBack(field);
        }
    };

    onBlur = (val) => {
        let result = this.state.validatorsResult;
        val.forEach(item => {
            result = result.filter(i => i.msg !== item.msg);
        });
        this.setState({validatorsResult: [...result, ...val]});
        const errorsList = [...result, ...val].filter(i => !i.valid);
        if (this.props.onError) {
            this.props.onError(errorsList);
        }
    };

    render() {
        return this.props.children;
    }

}

export class FieldController extends React.Component {

    state = {
        value: '',
        valid: true
    };

    onChange = (e) => {
        const newValue = e.target.value;
        let isValid = true;
        if (this.props.flow) {
            this.props.flow.forEach(flow => {
                isValid &= flow(newValue, this.props.flowProps);
            });
            if (isValid) {
                this.setState({value: newValue});
            }
        } else {
            this.setState({value: newValue});
        }
        this.props.form.onChange(this);
    };

    onBlur = (e) => {
        let validators = [];
        this.props.validators.forEach(validator => {
            validators.push({...validator(this.state.value, this.props.fieldName, this.props.flowProps)});
        });
        this.props.form.onBlur(validators);
        this.setState({valid: !validators.filter(v => !v.valid).length > 0});
    };

    getControllers = () => {
        return {onBlur: this.onBlur, onChange: this.onChange, value: this.state.value};
    };

}

