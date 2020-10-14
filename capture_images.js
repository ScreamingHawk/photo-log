const NodeWebcam = require("node-webcam");
const fs = require('fs');
const path = require('path');

const INTERVAL_SECONDS = 1
const IMG_FOLDER = "imgs"

// Count the images in the folder
const countImages = () => {
	const files = fs.readdirSync(IMG_FOLDER);
	return files.length;
}

// Save an image to the folder
const captureImage = () => {
	const imageCount = `000000${countImages() + 1}`.slice(-6);
	const imageName = `image${imageCount}.jpg`
	NodeWebcam.capture(path.join(IMG_FOLDER, imageName), {}, function( err, data ) {
		if (err){
			console.error(err)
		}
		if (data){
			console.log(data)
		}
		console.log(`Saving ${imageName}`)
	});
}

// Run immediately
captureImage()
// Then run on a schedule
setInterval(captureImage, INTERVAL_SECONDS * 1000)
