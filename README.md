## Dependencies


## Installation
Clone EOSFactory source code from the repository:
```sh
git clone https://github.com/tokenika/eosfactory.git
```
Run the `install` script:
```sh
cd eosfactory
./install.sh
```
When prompted, supply the path pointing to the location of your smart-contract workspace:
```sh
## For example:
/Users/tuantran/Documents/workspace/contracts
```
Verify if EOSFactory works and is properly hooked up to EOSIO:
```sh
python3 -m eosfactory.config
```
Below is a sample of correct configuration:
```
EOSFactory version 3.4.0
Found eosio version 1.8.1
Found eosio.cdt version 1.6.2.
... all the dependencies are in place.


EOSFactory package is installed as a link to the directory:
    '/Users/tuantran/Documents/workspace/eosfactory/eosfactory/'
    

The current configuration of EOSFactory:
{
    "CONFIG_FILE": "/Users/tuantran/Documents/workspace/eosfactory/config/config.json",
    "EOSFACTORY_DATA_DIR": "/Users/tuantran/Documents/workspace/eosfactory",
    "EOSFACTORY_DIR": "/Users/tuantran/Documents/workspace/eosfactory",
    "EOSIO_CDT_ROOT": "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/",
    "EOSIO_CDT_VERSION": [
        "1.6.2"
    ],
    "EOSIO_CLI_EXECUTABLE": "cleos",
    "EOSIO_CONTRACT_WORKSPACE": "/Users/tuantran/Documents/workspace/contracts",
    "EOSIO_CPP": "eosio-cpp",
    "EOSIO_CPP_INCLUDES": [
        "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include",
        "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include/libcxx",
        "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include/eosiolib/core",
        "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include/eosiolib/contracts"
    ],
    "EOSIO_GENESIS_JSON": null,
    "EOSIO_KEY_PRIVATE": "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3",
    "EOSIO_KEY_PUBLIC": "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV",
    "EOSIO_SHARED_MEMORY_SIZE_MB": "300",
    "EOSIO_VERSION": [
        "1.8.1"
    ],
    "INCLUDE": null,
    "KEOSD_EXECUTABLE": "keosd",
    "KEOSD_WALLET_DIR": "/Users/tuantran/eosio-wallet/",
    "LIBS": null,
    "LOCAL_NODE_ADDRESS": "127.0.0.1:8888",
    "LOCAL_NODE_EXECUTABLE": "nodeos",
    "NODEOS_CONFIG_DIR": null,
    "NODEOS_DATA_DIR": null,
    "NODEOS_OPTIONS": [],
    "NODEOS_STDOUT": null,
    "TEMPLATE_DIR": "/Users/tuantran/Documents/workspace/eosfactory/templates/contracts",
    "VERSION": "3.4.0",
    "WALLET_MANAGER_ADDRESS": "127.0.0.1:8888",
    "WSL_ROOT": ""
}

You can overwrite the above settings with entries in the configuration 
file located here:
/Users/tuantran/Documents/workspace/eosfactory/config/config.json


There are undefined setting:
{
    "EOSIO_GENESIS_JSON": null,
    "INCLUDE": null,
    "LIBS": null,
    "NODEOS_CONFIG_DIR": null,
    "NODEOS_DATA_DIR": null,
    "NODEOS_STDOUT": null
}
```
## Test Contracts
Create a new contract
```sh
cd eosfactory
python3 -m eosfactory.create_project $CONTRACT_NAME
```
To test a smart contract, use this command
```sh
python3 $DIRECTORY/$TEST_FILE

## For example:
## python3 tests/hello_world.py
```
## Troubleshooting
### Error: The local 'nodeos' failed to start few times in sequence
This error may come from a variety of causes, however, most of them are because of the incorrect configuration of nodes.

Firstly, try a random `cleos` command:
```sh
cleos wallet list
```
If you see some warning `errors` like the below:
```
Warning: Failed to set locale category LC_NUMERIC to en_VN.
Warning: Failed to set locale category LC_TIME to en_VN.
Warning: Failed to set locale category LC_COLLATE to en_VN.
Warning: Failed to set locale category LC_MONETARY to en_VN.
Warning: Failed to set locale category LC_MESSAGES to en_VN.
```
Then you need to fix those errors first. Otherwise, eosfactory will denote it as a bug and stop nodes. In this case, you can fix this error by changing `Region` to `United States` on `Language & Region` for Mac users.

### Cannot determine the source file of the contract. There is many files in the 'src' directory
Navigate to contract directory then
```sh
cd .vscode
nano c_cpp_properties.json
```
Copy the below content. Pay attention to the object `codeOptions` and modify `$CONTRACT_FILE` to your main contract file name
```
{
    "configurations": [
        {
            "includePath": [
                "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include",
                "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include/libcxx",
                "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include/eosiolib/core",
                "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include/eosiolib/contracts",
                "${workspaceFolder}",
                "${workspaceFolder}/include"
            ],
            "libs": [],
            "codeOptions": [
                "--src src/$CONTRACT_FILE.cpp"
            ],
            "testOptions": [],
            "defines": [],
            "intelliSenseMode": "clang-x64",
            "browse": {
                "path": [
                    "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include",
                    "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include/libcxx",
                    "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include/eosiolib/core",
                    "/usr/local/Cellar/eosio.cdt/1.6.2/opt/eosio.cdt/include/eosiolib/contracts",
                    "${workspaceFolder}",
                    "${workspaceFolder}/include"
                ],
                "limitSymbolsToIncludedHeaders": true,
                "databaseFilename": ""
            }
        }
    ],
    "version": 4
}
```
