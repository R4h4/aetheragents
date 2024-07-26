# AetherAgents

[![PyPI version](https://badge.fury.io/py/aetheragents.svg)](https://badge.fury.io/py/aetheragents)
[![Python Versions](https://img.shields.io/pypi/pyversions/aetheragents.svg)](https://pypi.org/project/aetheragents/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/R4h4/aetheragents/actions/workflows/ci.yml/badge.svg)](https://github.com/R4h4/aetheragents/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/R4h4/aetheragents/branch/main/graph/badge.svg)](https://codecov.io/gh/R4h4/aetheragents)
[![Documentation Status](https://readthedocs.org/projects/aetheragents/badge/?version=latest)](https://aetheragents.readthedocs.io/en/latest/?badge=latest)

AetherAgents is an easy-to-use framework for creating AI agents, designed to simplify the process of building and deploying intelligent systems.

<p style="color: red; font-weight: bold;">Warning: AetherAgents is currently in early Alpha and the API will change</p>

## Features

- 🚀 Quick and easy setup for AI agents
- 🧠 Flexible architecture supporting various AI models
- 🔗 Seamless integration with popular AI services
- 📊 Built-in tools for agent performance monitoring
- 🛠️ Extensible plugin system for custom functionalities

## Installation

You can install AetherAgents using pip:

```bash
pip install git+https://github.com/R4h4/aetheragents.git
```

## Quick Start

Here's a simple example to get you started with AetherAgents:

```python
from aetheragents import TextAgent

# Create an agent
agent = TextAgent("You are an AI Agent that greets the world")

# Define a task
task = Task("Hi")

# Assign the task to the agent
result = agent.execute(task)

print(result)  # Output: "Hello, World!"
```

## Documentation

For more detailed information about AetherAgents, please refer to our [documentation](https://aetheragents.readthedocs.io/).

## License

AetherAgents is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

If you encounter any problems or have any questions, please [open an issue](https://github.com/R4h4/aetheragents/issues) on our GitHub repository.

## Acknowledgements

AetherAgents is built with love by the open-source community. We'd like to thank all our contributors and the amazing Python ecosystem that makes this project possible.

---

Made with ❤️ by Karsten Eckhardt ([@R4h4](https://github.com/R4h4))