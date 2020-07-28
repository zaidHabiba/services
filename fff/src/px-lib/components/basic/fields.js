import * as React from "react";
import {FieldController} from "../flow/controller";
import {Input} from "semantic-ui-react";

export class InputField extends FieldController {
    render() {
        return <Input {...this.getControllers()}/>
    }
}
