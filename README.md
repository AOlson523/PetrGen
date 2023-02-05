PetrGen

Go to the backend folder

python instaPetrScrape.py

on terminal 

utalized instaloader github repo: https://github.com/instaloader/instaloader
utalized pokemon generator on Hugging Face: https://huggingface.co/spaces/sayakpaul/pokemon-sd-kerascv

## Inspiration
We were inspired by the current model that we have access to, the pokemon generator by sayakpaul on Hugging Face. Current working model->(https://huggingface.co/spaces/sayakpaul/pokemon-sd-kerascv)
## What it does
Our model generates images based on user input, using deep neural networks.
## How we built it
We built the code using a GitHub repository called instaloader (https://github.com/instaloader/instaloader), to scrape and download posts from about 50 different Petr Instagram accounts. From there a script takes the data from those profile folders and generates an JSON file of the images and their captions. The JSON file is provided to the neural networks so that it may run and be able to be utilized for image generation.
## Challenges we ran into
We initially were going to use another neural network to generate captions for each image, but we made the switch to using the already provided in order to save time. Unfortunately, we did not have enough time for the Petr generation to be fully complete, however the pokemon generator is available and shows how the Petr generation would work. Current working model->(https://huggingface.co/spaces/sayakpaul/pokemon-sd-kerascv)
## Accomplishments that we're proud of
However, were are very proud of our ability to scrape and download each image (aprox. 1200 images), and then create a code that takes the post information and organizes it into a list of dictionaries in a JSON file, to be used by the generator.
## What we learned
The Instagram API would have definitely been more useful and have been given the time to be approved by Meta.
## What's next for PetrGen
To get the final product, our Petr generation, to fully finish processing to be used by the user. Once that is squared away, we can add more images to generator, to give PetrGen more flexibility. 
