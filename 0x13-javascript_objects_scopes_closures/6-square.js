#!/urs/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
	super(size, size);
  }
  charPrint (c) {
	let i = 0;
	if (c === undefined) {
	  super.print();
	} else {
	  for (; i < this.width; i++) {
		console.log(c.repeat(this.width));
	  }
	}
  }
};
