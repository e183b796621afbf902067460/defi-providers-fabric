# DeFi Providers Fabric

Depends on: [defi-head-core](https://github.com/e183b796621afbf902067460/defi-head-core).

---
Based on input arguments an [`ProviderAbstractFabric`](https://github.com/e183b796621afbf902067460/defi-providers-fabric/blob/master/providers/abstracts/fabric.py) return [`IConcreteFabric`](https://github.com/e183b796621afbf902067460/defi-head-core/blob/master/head/interfaces/fabrics/interface.py) object such as: [*HTTPProviderFabric*](https://github.com/e183b796621afbf902067460/defi-providers-fabric/blob/master/providers/fabrics/http/fabric.py), [*IPCProviderFabric*](https://github.com/e183b796621afbf902067460/defi-providers-fabric/blob/master/providers/fabrics/ipc/fabric.py) or [*WebsocketProviderFabric*](https://github.com/e183b796621afbf902067460/defi-providers-fabric/blob/master/providers/fabrics/websocket/fabric.py).
`IConcreteFabric` (HTTP, IPC, WebSocket) can produce needed `Provider Object` for different Blockchains.

For example, to get `BSC_HTTP_PROVIDER` need to call [`BridgeConfigurator`](https://github.com/e183b796621afbf902067460/defi-head-core/blob/master/head/bridge/configurator.py) and pass to it constructor next arguments and then call `produceProduct()` method:
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
