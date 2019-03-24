# UrbanDictionary-PosterMaker
A python script that will create a poster with your favorite word definition from www.urbandictionary.com. The script will only take the top definition.
### Prerequisites
numpy, pillow
```
pip install numpy pillow
```
## How to use
1. find a word that you like the description of on www.urbandictionary.com
2. find a font that you want to use (I included bebas neue font)
3. navigate in cmd to the folder with the 2 .py files in it
4. run the createUrbanPoster.py with the following arguments: word fontfile.ttf definition_number font_size

definition_number: input number for desired definition like 2 for the second definition\
font_size: leave empty and the script will try to calculate a font size for the text or enter the font size you want

Example:
```
python createUrbanPoster.py word fontfolder\font.tff 1 150
```
If you want to change the color of the background or the color of the text change the variable bgColor for background and textColor for text

## Example
The word I want to have a poster of is computer science of course.

```
python createUrbanPoster.py "computer science" bebas_neue\BebasNeue-Regular.ttf
```

![](Poster.png)
