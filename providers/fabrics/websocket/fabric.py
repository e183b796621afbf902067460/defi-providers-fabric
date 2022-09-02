import os
from web3.providers.websocket import WebsocketProvider

from head.interfaces.fabrics.interface import IConcreteFabric


class WebsocketProviderFabric(IConcreteFabric):

    def addProduct(self, chain: str, uri: str) -> None:
        if not self._products.get(chain):
            self._products[chain]: WebsocketProvider = WebsocketProvider(endpoint_uri=uri)

    def getProduct(self, chain: str) -> WebsocketProvider:
        provider: WebsocketProvider = self._products.get(chain)
        if not provider:
            raise ValueError(f'Set Websocket provider for {chain} blockchain')
        return provider


wsProviderFabric = WebsocketProviderFabric()

wsProviderFabric.addProduct(chain='eth', uri=os.getenv('ETH_WS_PROVIDER', ''))
wsProviderFabric.addProduct(chain='bsc', uri=os.getenv('BSC_WS_PROVIDER', ''))
wsProviderFabric.addProduct(chain='avax', uri=os.getenv('AVAX_WS_PROVIDER', ''))
wsProviderFabric.addProduct(chain='arb', uri=os.getenv('ARB_WS_PROVIDER', ''))
wsProviderFabric.addProduct(chain='ftm', uri=os.getenv('FTM_WS_PROVIDER', ''))
wsProviderFabric.addProduct(chain='matic', uri=os.getenv('MATIC_WS_PROVIDER', ''))
wsProviderFabric.addProduct(chain='opt', uri=os.getenv('OPT_WS_PROVIDER', ''))
