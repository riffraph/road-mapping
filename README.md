# Road Mapping

[![pipeline status](https://gitlab.com/riffraph/road-mapping/badges/master/pipeline.svg)](https://gitlab.com/riffraph/road-mapping/commits/master) [![coverage report](https://gitlab.com/riffraph/road-mapping/badges/master/coverage.svg)](https://gitlab.com/riffraph/road-mapping/commits/master)

App to interpret a logical breakdown of work (e.g. capabilities and features) and create a visual representation of it.

Usually the input would be a model represented as rows and columns, such as an Excel export from JIRA.

The output is a diagram describing the dependencies and relationships between the entities. Boiling it down it is just a dependency graph.

## Getting Started

TODO ...

### Prerequisites

* Python3
* Graphviz

Install the following Python packages using `pip install`
* Graphviz (https://github.com/xflr6/graphviz)
* OpenPyXL (https://openpyxl.readthedocs.io/)

### Installing

TODO ...

## Running the tests

`pytest` is used as the testing framework.

`tox` is used to automatically orchestrate the steps of packaging the code, installing dependencies, creating a virtual environment and invoking the test runner.

From the project folder simply run `tox -e py36`


### Break down into end to end tests

TODO ...

Explain what these tests test and why

```
Give an example
```

## Deployment

TODO ...

Add additional notes about how to deploy this on a live system

## Built With

* [Tox](https://tox.readthedocs.io) - the test automation framework used


## Authors

* **Raphael Chan** - [riffraph](https://github.com/riffraph)


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

TODO ...

* Hat tip to anyone whose code was used
* Inspiration
* etc
