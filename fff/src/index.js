import React from 'react';
import ReactDOM from 'react-dom';
import './assets/global.css';
import App from './app/App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);


serviceWorker.unregister();
