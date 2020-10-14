const fs = require('fs');
const path = require('path');
const Confirm = require('prompt-confirm');

const IMG_FOLDER = 'imgs';

const deleteAllImages = () => {
	fs.readdir(IMG_FOLDER, (err, files) => {
		if (err){
			throw err;
		}
	
		for (const file of files) {
			fs.unlink(path.join(IMG_FOLDER, file), err => {
				if (err){
					throw err;
				}
			});
		}
	});
}

console.log('Clearing all saved images')
new Confirm('Are you sure?')
	.run()
	.then(function(answer) {
		if (answer){
			deleteAllImages()
		}
	});
