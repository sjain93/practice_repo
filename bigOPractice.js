const nemo = ['nemo'];

function findNemo(array) {
    for  (let i = 0; i < array.length; i++) {
        if (array[i]=== 'nemo'){
            console.log("Found nemo");
        };
    };
};
// basic loop to investigate how to optimize through using BigO notation
findNemo(nemo);
