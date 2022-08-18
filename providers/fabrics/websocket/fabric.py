import os
from web3.providers.websocket import WebsocketProvider

from interfaces.fabrics.interface import IConcreteFabric
from orm.consts.chainName import ChainName


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

WebsocketProviderFabric.addProduct(chain=ChainName.ETH, uri=os.getenv('ETH_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=ChainName.BSC, uri=os.getenv('BSC_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=ChainName.AVAX, uri=os.getenv('AVAX_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=ChainName.ARB, uri=os.getenv('ARB_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=ChainName.FTM, uri=os.getenv('FTM_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=ChainName.MATIC, uri=os.getenv('MATIC_WS_PROVIDER', ''))
WebsocketProviderFabric.addProduct(chain=ChainName.OPT, uri=os.getenv('OPT_WS_PROVIDER', ''))
