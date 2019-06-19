function group(collection, grouper) {
  const output = {};
  collection.forEach((element) => {
    const funcOut = grouper(element);
    if (funcOut in output === false) {
      output[funcOut] = [element];
    } else {
      output[funcOut].push(element);
    }
  });
  return output;
}

console.log(group([6.5, 4.2, 6.3], Math.ceil));
