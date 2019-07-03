import React from 'react';
import unsplash from '../api/unsplash';
import SearchBar from './SearchBar'
import ImageList from './ImageList'

// using async await instead of promise functions more readable
class App extends React.Component {
    state = { images: [] };

    onSearchSubmit = async (term) => {
        const response = await unsplash.get('search/photos', {
            params: { query: term },
        });
        // this needs to be binded otherwise it will try to set state on the props passed into the search bar
        this.setState({images: response.data.results});
    }

    render () {
        return (
            <div className="ui container" style={{marginTop: '10px'}}>
                <SearchBar onSubmit={this.onSearchSubmit} />
                <ImageList images={this.state.images}/>
                Found: {this.state.images.length} images!
            </div>
        );
    }
};

export default App
