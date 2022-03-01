#!/usr/bin/node
const dictInit = require('./101-data').dict;
const newDict = {};

for (const k in dictInit) {
  if (!(dictInit[k] in newDict)) {
    newDict[dictInit[k]] = [k];
  } else {
    newDict[dictInit[k]].push(k);
  }
}

console.log(newDict);
