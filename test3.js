function minArgs(...numbers) {
  const compare = [...numbers];
  const min = Math.min(...[].concat(...compare));
  return min;
}

const test = minArgs([2, 1, -20], -30);
console.log(test);
