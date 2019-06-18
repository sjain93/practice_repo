function makeCounter(start) {
  let output = start;
  if (typeof start === 'undefined') {
    return 0;
  }
  function value() {
    return output;
  }
  function increment() {
    output += 1;
    return output;
  }
  function decrement() {
    output -= 1;
    return output;
  }
  return {
    increment,
    decrement,
    value,
  };
}

const counter2 = makeCounter(4);
counter2.increment();
console.log(counter2.value());
