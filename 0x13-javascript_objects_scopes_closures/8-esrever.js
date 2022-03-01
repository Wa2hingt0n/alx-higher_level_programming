#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length;
  let j = 0;
  const newList = [];

  for (j = 0; j < list.length; j++) {
    newList[j] = list[i - 1];
    i--;
  }

  return newList;
};
