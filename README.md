# netloc-map

Visualizing Server Locations based on browsing histor

## Table of Contents

- [netloc-map](#netloc-map)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Quick Start](#quick-start)
  - [Usage](#usage)
  - [License](#license)
  - [Contributing](#contributing)
  - [Tests](#tests)
  - [Questions](#questions)
  - [Motivation TL;DR](#motivation-tldr)

## Installation

To install the package, run:

```shell
pip install netloc-map
```

## Quick Start

```python
import netloc_map as nlm
nlm.plot_map(locations, 'netloc-map.png')
```

## Usage

To use the package, run:

```python
from netloc_map import NetlocMap
```

## License

This project is licensed under the MIT license.

## Contributing

This project is open source. Feel free to contribute!

## Tests

To run tests, run:

```shell
python -m unittest discover
```

## Questions

If you have any questions about the project, open an issue or contact the [author](


## Motivation TL;DR

I absolutely adore data visualisation! Who doesn't enjoy looking at pretty graphs?

Before this project, i had never done any map visualisation, so I decided to do something with maps.
i knew i wanted to visualise something involving **maps**, but I didn't know what.

This is due to the fact that IP addresses are **geo-specific**. For example, if you are from Brazil, you have a unique set of IP addresses, and if you are from Russia, you have a unique set of IP addresses.

It's not fun to use any **random set of IP** addresses. Everyone enjoys **personalised visualisation**, and I am no exception. I decided to generate the visualisation using my web browsing history from the previous couple months.
