import {BaseServiceClass} from "./base.service";

class UserServiceClass extends BaseServiceClass {

    base = 'user/';

    getUserInformation = () => {
        this.endPoint = this.base;
        return this.get();
    };

    getUsersInformation = () => {
        this.endPoint = 'users/';
        return this.get();
    };

    loginUser = (email, password) => {
        this.endPoint = this.base + 'login';
        return this.createRequest().post(this.endPoint, {email, password});
    };

    logoutUser = () => {
        this.endPoint = this.base + 'logout';
        return this.createRequest().put(this.endPoint);
    };

    registerUser = (data) => {
        this.endPoint = this.base + 'register';
        return this.createRequest().post(this.endPoint, data);
    };

    isEmailUsed = (email) => {
        this.endPoint = this.base + 'is-email-used';
        return this.createRequest().post(this.endPoint, {email});
    };

}

const UserService = new UserServiceClass();
export default UserService;