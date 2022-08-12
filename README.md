# Foreground extractor
---
## Input Image

![Input Image](Screenshots/original_image.png)

## Output Images

![Output Image](Screenshots/intermediate_image.png)

![Output Image](Screenshots/final_Image.png)


## Description
---
This program extracts the foreground from an image and then places it in another image. It takes in three parameters:
- **Image With Foreground**: the image from which you want to extract the foreground.
- **Background Image**: The background image on which you want to paste the foreground.
- **Rectangle**: A rectangle (coordinates) used to specify which area of the image the foreground you are interested in can be found. This rectangular coordinates can be obtained through various means but one of the ways to obtain it is to open the image in matplotlib and take note of the coordinates before inputing them into the program.

>**Note:** The the first two elements of the rectangle coordinates are the top left x and y axis and the last two elements are the bottom right x and y axis of the rectangle.

## Running the code
---
If you want to run the code with the default parameters (default images) run the code with the command:

```bash
python extract.py
```

If you want to change the default parameters (images and ractangle):

```bash
usage: extract.py [-h] [-f FORE] [-b BACK] [-r RECT]

optional arguments:
  -h, --help            show this help message and exit
  -f FORE, --fore FORE  The image containing the foreground
  -b BACK, --back BACK  The image containing the background
  -r RECT, --rect RECT  The rectangle that defines the region containing the foreground. Entered as a string separated by commas
```

**Example:**
```bash
python extract.py --fore "extract_minion.jpg" --back "background.jpg" --rect "322, 338, 728, 823"
```


