# Easy-FAS: A command-line tool for calculating Forward Association Strength

This repository contains a command-line tools that allows a user to easily calculate the Forward Association Strength between any two words.


## Forward Association Strength
The Forward Association Strength (FAS) of a word is a metric of how likely it is that someone will respond with a given word when presented with a specific cue word in a word association task—i.e., when asked to produce the first word that comes to mind. It is calculated based on the responses of a norming study. For example, if 100 people are presented with the cue word *one* and 75 of them respond with *two*, the FAS of the response *two* for the cue *one* is given by:

![](https://latex.codecogs.com/svg.image?\color{white}\frac{75}{100}=0.75)


## Current Implementation
Currently, this tool only supports calculating FAS based on two sets of norms:
* The Edinburgh Associative Thesaurus (EAT)
* The [University of South Florida Free Association Norms](http://w3.usf.edu/FreeAssociation/) (USFFAN)

The tool can calculate the Forward Association Strength based on one of these sets of norms or a combination of both (the provided data include the raw counts of each response). The data used by Easy-FAS are derived from the [XML files](http://rali.iro.umontreal.ca/rali/?q=en/Textual%20Resources) provided by the *Recherche appliquée en linguistique informatique* (Applied research in computational liguistics) laboratory at the Université de Montréal. Each set of norms were converted to python dictionaries using the code provided in `create_dicts.py` and are stored as `eat_dict.json` and `usffan_dict.json`.
 
## How to use

There are currently two options for how to use this tool.

### Option 1: Calculate the FAS of a word pair
This allows the user to calculate the FAS between a specific word pair, and returns the the FAS between the two. The user can select between the Edinburgh Associative Thesaurus (EAT) or University of South Florida Free Association Norms (USFFAN).

The following command returns the FAS of the response *two* given the cue word *one* using the EAT.

```
python calculate_distance.py --cue one --response two --norms eat
```

This returns the following response:

```
Cue: one	Response: two	FAS: 0.6363636363636364
```

Alternatively, we might want to return the FAS of the response *one* given the cue word *two* based on the USFFAN:

```
python calculate_distance.py --cue two --response one --norms usffan
```

This returns the following response:

```
Cue: two	Response: one	FAS: 0.14383561643835616
```
In order to calculate the FAS based on the combination of two sets of norms, we can set ther `--norms` argument to `all`, or omit the argument entirely (the default argument of `--norms` is `all`).

### Option 2: Calculate the FAS of a set of word pairs
This requires a `.csv` file as input with column names `Cue` and `Response`. Rather than using the `--cue` and `--response` arguments, the `--cue_response_input_file` (alias `-i`) argument is used, for example:
```
python calculate_distance.py -i test_file.csv 
```
This creates an output `.csv` file in the same directory as the input file that is identical to the input file, but with an additional `FAS` column, which either contains the FAS or is empty if the cue word does not appear in the selected norms. The output file is called `[input_file].output.csv`—this would be `test_file.output.csv` for the example presented above. Hence, the output in the terminal after running the code above is:

```
Successfully produced output file: test_file.output.csv
```


### Notes
In the current implementation:
* If the cue and response word are identical, Easy-FAS returns a FAS of 1.
* If the cue word is present in the selected norms but the response is not, Easy-FAS returns a FAS of 0.
* If the cue word is not present in the selected norms, Easy-FAS returns a FAS of `None`. This shows as blank in the terminal, and as an empty cell in the output `.csv` file.


## How to cite
If you use this tool in your research, please cite in the following way:

```
@misc{michaelov_2022_easyFAS,
  title = {Easy-FAS: A command-line tool for calculating Forward Association Strength},
  shorttitle = {Easy-FAS},
  author = {Michaelov, James A.},
  year = {2022},
  version = {0.1},
  copyright = {MIT License},
  note={\url{https://github.com/jmichaelov/easy-fas}}
}
```

## Citations
* Kiss, G. R., Armstrong, C., Milroy, R., & Piper, J. (1973). An associative thesaurus of English and its computer analysis. In A. J. Aitken, R. W. Bailey, & N. Hamilton-Smith (Eds.), *The Computer and Literary Studies*. Edinburgh University Press.
* Nelson, D. L., McEvoy, C. L., & Schreiber, T. A. (1998). The University of South Florida word association, rhyme, and word fragment norms. http://www.usf.edu/FreeAssociation/.
* Nelson, D. L., McEvoy, C. L., & Schreiber, T. A. (2004). [The University of South Florida free association, rhyme, and word fragment norms](https://doi.org/10.3758/BF03195588). *Behavior Research Methods, Instruments, & Computers, 36(3)*, 402–407.
