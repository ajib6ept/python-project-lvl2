### Project #2 "Generate Difference"
***

### Tests and linter status:
[![Actions Status](https://github.com/ajib6ept/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/ajib6ept/python-project-lvl2/actions)
[![Actions Status](https://github.com/ajib6ept/python-project-lvl2/workflows/hexlet-code/badge.svg)](https://github.com/ajib6ept/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/38b1070ff74e961e566d/maintainability)](https://codeclimate.com/github/ajib6ept/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/38b1070ff74e961e566d/test_coverage)](https://codeclimate.com/github/ajib6ept/python-project-lvl2/test_coverage)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ajib6ept/python-project-lvl2/main.svg)](https://results.pre-commit.ci/latest/github/ajib6ept/python-project-lvl2/main)

***

This is the second project in the Python learning course [hexlet.io](https://ru.hexlet.io)


This package allows you to compare two files (json/yaml).
Shows the difference between them using different output formats ('stylish', 'plain', 'json')

#### Installation
* Install [poetry](https://python-poetry.org/docs/#installation)
* ```git clone https://github.com/ajib6ept/python-project-lvl2```
* ```cd python-project-lvl2/ && make install```
* ```make build```
* ```make package-install```

![brain-even](gif/install.gif)

***
#### Usage
* ```gendiff file1.json file2.yml```
* ```gendiff -f plain file1.yml file2.json```

***
##### Comparing simple files 

![brain-even](gif/simple_files.gif)

##### Comparing nested files

![brain-even](gif/nested_files.gif)