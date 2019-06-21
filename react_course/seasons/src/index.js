import React from 'react';
import ReactDOM from 'react-dom';
import SeasonDisplay from './SeasonDisplay'

class App extends React.Component {
    //anytime a new instance of the app component and show on screen, this is called
    
    // constructor(props) {
    //     super(props);
    //     //this is the only time we do direct assignment to this.state
    //     this.state = { lat: null, errorMessage: '' }; 
    
    // This entire cosntructor function can be reduced down to the state declaration line, runs when the component is first loaded

    // };
    state = {lat: null, errorMessage: ''};

    componentDidMount() {
        window.navigator.geolocation.getCurrentPosition(
            position =>  this.setState({ lat: position.coords.latitude }),
            err => this.setState({errorMessage: err.message})
        );
    };
    componentDidUpdate() {
        console.log('My comp was updated - it rerendered compDidUpdate')
    };
    //React says we have to define render that returns JSX
    render() {
        if (this.state.errorMessage && !this.state.lat) {
            return <div>Error: {this.state.errorMessage}</div> 
        }
        if (!this.state.errorMessage && this.state.lat) {
            return <SeasonDisplay lat={this.state.lat}/> 
            //state from one component and pass it down to the child
        }
        return <div>Loading!</div>
    };
};

ReactDOM.render(
    <App />,
    document.querySelector('#root')
);

