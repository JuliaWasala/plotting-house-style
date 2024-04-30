# plotting-house-style
This package has code, a stylesheet and colours frequently used by Julia in her plots.
## Contents
- stylesheet
- `colours.py` - a python file with the colours used in the stylesheet
- `legend.py` - dictionaries with kwargs to style different types of dictionaries
- `map.py` - a python file with functions to style maps, requires cartography packages
- `main.py` - a python file with functions to style plots

> [!TIP] Other style guidelines
>   - Capitalise the labels and title
>   - Set ylims of boxplots showing performance to [0.5,1]
>   - Remove grid if not helpful
>   - check if colours are color-blind friendly, e.g. [here](https://colorbrewer2.org/#type=qualitative&scheme=Dark2&n=3).