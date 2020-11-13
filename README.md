<img alt="FactSet" src="https://www.factset.com/hubfs/Assets/images/factset-logo.svg" height="56" width="290">

# Sample API Python SDK

[![build](https://img.shields.io/github/workflow/status/factset/sampleapi-python-sdk/CI)](https://github.factset.com/factset/sampleapi-python-sdk/actions?query=workflow%3ACI)
[![PyPi](https://img.shields.io/pypi/v/fds.sampleapi)](https://pypi.org/project/fds.sampleapi/)
![API version](https://img.shields.io/badge/API-v1-blue)
[![Apache-2 license](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)

---

**Important note**
This is a template repository to help get started with SDK generation process. Use this template to create your own repository and customize it as per your requirement. Also, refer [Sample API SDK Generator](https://github.factset.com/factset/sampleapi-sdk-generator) which is the start point of the SDK generation process and this repository is dependent on that.

---

Use this library to integrate with FactSet's Sample APIs. Below APIs are supported by this SDK.

* [Sample API](https://developer.factset.com/api-catalog/sample-api)

## Contents

* [auto-generated-sdk](auto-generated-sdk) - Auto-generated code using [Sample API SDK Generator](https://github.factset.com/factset/sampleapi-sdk-generator)
* [examples](examples) - Sample project containing code snippets to quickly get started with the SDK  
* [tests](tests) - Integration tests

## Requirements

* Python 3.4 or higher

## Installation

* Install the latest SDK using pip:

  ```sh
  pip install fds.sampleapi
  ```

* Alternatively, download or clone this repository and install the SDK by  running Setuptools in the SDK installation directory:

  ```sh
  git clone https://github.factset.com/factset/sampleapi-python-sdk.git
  cd auto-generated-sdk
  python setup.py install --user
  ```

## Usage

Refer [examples](examples) project for sample code snippets to quickly get started with the SDK

## Tests

First, clone the repo locally and `cd` into the directory.

```sh
git clone https://github.factset.com/factset/sampleapi-python-sdk.git
cd tests
```

Next, install dependencies.

```sh
pip install -r requirements.txt
```

Before running the tests, set the below environment variables. Use the [Developer Portal Manage API Keys page](https://developer.factset.com/manage-api-keys) to get these values.

```sh
export SAMPLE_API_USERNAME_SERIAL = "username-serial"
export SAMPLE_API_PASSWORD = "apikey"
```

Run the tests with below command.

```sh
python -m test
```

## Contributing

* Files in [auto-generated-sdk](auto-generated-sdk) directory are auto-generated and should not be manually edited here. Refer [Sample API SDK Generator](https://github.factset.com/factset/sampleapi-sdk-generator) for instructions on how to modify these files.
* Projects [examples](examples) and [tests](tests) are open to enhancements and bug fixes. Please create a pull requests with the proposed changes.
