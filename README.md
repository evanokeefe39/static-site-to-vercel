## AR.js and AFrame using multiple barcode images

This project utilizes AR.js and AFrame to create an augmented reality experience using multiple barcode images. The purpose of this project is to overlay mp4 files onto an artbook, enhancing the user's interaction with the physical book.

These are static files served from the "/public" folder. I use the npx http-server package:
```
npx http-server -o .
```
Refer to [this](https://github.com/nicolocarpignoli/artoolkit-barcode-markers-collection?tab=readme-ov-file) repo for info about different barcode marker sets
Markers are generated from [here](https://au.gmented.com/app/marker/marker.php)

Once you have everything set up, open the HTML file in a web browser that supports WebAR (e.g., Google Chrome on a mobile device). Point the camera at the barcode markers, and the mp4 overlays will be displayed on top of the artbook.

Enjoy the augmented reality experience with your artbook and barcode markers!

