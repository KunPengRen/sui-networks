# Sui Network Docker Compose

This was tested using MacOS 14.3.1, Docker Compose: v2.13.0.

This compose brings up 4 validators, 1 fullnode, and 1 faucet service

Beofre running the network,You must have the latest version (v1.29.9) of the [Sui binary](https://docs.sui.io/guides/developer/getting-started/sui-install) installed on your machine or complie locally using source code.

Steps for running:

1. generate the genesis and validator config file

```
./new-genesis.sh
```

2. run compose

```
(optional) `rm -r /tmp/sui`
docker compose up
```


**additional info**
The version of `sui` which is used to generate the genesis outputs much be on the same protocol version as the fullnode/validators (eg: `mysten/sui-node:sui-v1.29.0-release`)
Here's an example of how to build a `sui` binary that creates a genesis which is compatible with the release: `v1.29.0`
```
git checkout releases/sui-v1.19.0-release
cargo build --bin sui
```
you can also use `sui-network/Dockerfile` for building genesis
