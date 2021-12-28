# ArkenDoge
This repo is forked from (CyberDoggos)[https://github.com/cyberdoggos/generator]


## Setup and Run
This script was done with Python 3.8. All additional requirements can be found in the `requiremtents.txt`. 
To install them all at once just run `pip install -r requirements.txt` in the project folder.

Run `python generate.py` to start the generation of the images and properties. All generated files will end up in the 
build folder. The image is saved in the tiny original resolution as well as in an enlarged version. Besides the 
single images, the properties of each item are serialized into a yaml file. After all items are created, a collage of 
all images is stitched together.

## Make it your own
To make your own collection of generated images you don't even need to touch the Python script. You only have to replace 
the images in the corresponding folder with your own ones and adapt the three config files.

The `config.yaml` is used to adjust some general parameters of the collection and generation. Each parameter is 
well documented in the file.

The `config_normal.yaml` contains a list of the layers which are stacked on top of each other to generate the image. 
The order of the layers in the config file corresponds to the stacking order. So make sure to put the background layer 
at the top of the config file. Each layer has a category value (which is used as the headline for the trait) and a list 
of multiple traits available at this very layer. Each trait, in turn, consists of ...
- the name of the trait
- a target probability which sums up to one over the complete layer
- the path to the image resource of that trait
- an optional category which can override the category defined in the layer

The `config_legend.py` is used to mix some manually created images into the collection. The normal image that will be 
replaced by the legendary one is given by the image id. If you want to create a collection of only randomly created 
images, you can simply empty that file.


