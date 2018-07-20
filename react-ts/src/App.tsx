import * as React from 'react';
import './App.css';

import logo from './logo.svg';

class App extends React.Component<any, any> {
  constructor(props: any){
    super(props)
    this.state = {json: []}
  }

  // tslint:disable-next-line:member-access
  componentDidMount(){
    fetch('/api/lead')
    .then(res => res.json())
    .then(data => this.setState({json:data}))
  }

  public render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.tsx</code> and save to reload.
        </p>
          {this.state.json.length > 0 && (
            <div>
              <h4>from djang api:</h4>
              <p>{this.state.json[0].id}</p>
              <p>{this.state.json[0].name}</p>
              <p>{this.state.json[0].email}</p>
              <p>{this.state.json[0].message}</p>
            </div>
          )}
      </div>
    );
  }
}

export default App;
