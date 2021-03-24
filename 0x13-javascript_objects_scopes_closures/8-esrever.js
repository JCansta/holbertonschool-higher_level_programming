#!/usr/bin/node
exports.esrever = function (list) {
  let count = list.length - 1;
  let newl = [];
  for (; count >= 0; count--) {
    newl.push(list[count]);
  }
  return newl;
};
