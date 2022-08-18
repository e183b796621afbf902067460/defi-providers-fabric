import os
from web3.providers.websocket import WebsocketProvider

from head.interfaces.fabrics.interface import IConcreteFabric
from head.consts.chains.const import Chains


class WebsocketProviderFabric(IConcreteFabric):

    def addProduct(self, chain: str, uri: str) -> None:
        if not self._products.get(chain):
            self._products[chain]: WebsocketProvider = WebsocketProvider(endpoint_uri=uri)

    def getProduct(self, chain: str) -> WebsocketProvider:
        provider: WebsocketProvider = self._products.get(chain)
        if not provider:
            raise ValueError(f'Set Websocket provider for {chain} blockchain')
        return provider


WebsocketProviderFabric = WebsocketProviderFabric()

WebsocketProviderFabric.addProduct(chain=Chains.ETH, uri=os.getenv('ETH_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=Chains.BSC, uri=os.getenv('BSC_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=Chains.AVAX, uri=os.getenv('AVAX_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=Chains.ARB, uri=os.getenv('ARB_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=Chains.FTM, uri=os.getenv('FTM_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=Chains.MATIC, uri=os.getenv('MATIC_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=Chains.OPT, uri=os.getenv('OPT_WS_PROVIDER', ''))
