# DeFi Providers Fabric

Depends on: [defi-head-core](https://github.com/e183b796621afbf902067460/defi-head-core).

---
Based on input arguments an `Abstract Fabric` return `Concrete Fabric` object such as: *HTTP Provider Fabric*, *IPC Provider Fabric* or *WebSocket Provider Fabric*.
`Concrete Fabric` (HTTP, IPC, WebSocket) can produce needed `Provider Object` for different Blockchains.

For example, to get `BSC_HTTP_PROVIDER` need to call `BridgeConfigurator` and pass to it constructor next arguments and then call `produceProduct()` method:
```
from head.bridge.configurator import BridgeConfigurator
from providers.abstracts.fabric import providerAbstractFabric


concreteFabricKey = 'http'
concreteProductKey = 'bsc'

provider = BridgeConfigurator(
            abstractFabric=providerAbstractFabric,
            fabricKey=concreteFabricKey,
            productKey=concreteProductKey) \
            .produceProduct()
```

All fabrics and products keys can be viewed in the right factories.
