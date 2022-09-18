# DeFi Providers Fabric
Based on input arguments an `Abstract Fabric` return `Concrete Fabric` object such as: HTTP Provider Fabric, IPC Provider Fabric and WebSocket Provider Fabric.
`Concrete Fabric` (HTTP, IPC, WebSocket) can produce needed `Provider Object` for different Blockchain.

For example, to get `BSC_HTTP_PROVIDER` need to call `BridgeConfigurator` and pass to it constructor next arguments:
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

All fabrics and products keys can be viewed in the right factories
