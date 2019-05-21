const { performance } = require('perf_hooks');

const nemo = ['nemo'];

const large = new Array(10000).fill('nemo');

function findNemo(array) {
    // let t0 = performance.now();
    for  (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo'){
            console.log("Found nemo");
        };
    };
    // let t1 = performance.now();
    // console.log('Call to find nemo took'+(t1-t0)+'milliseconds')
};
// basic loop to investigate how to optimize through using BigO notation
findNemo(large);

// function has a O(n) or linear time- in this case O(10000)
// fair Big O complexity