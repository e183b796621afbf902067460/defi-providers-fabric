import os
from web3.providers.rpc import HTTPProvider

from head.interfaces.fabrics.interface import IConcreteFabric


class HTTPProviderFabric(IConcreteFabric):

    def addProduct(self, chain: str, uri: str) -> None:
        if not self._products.get(chain):
            self._products[chain]: HTTPProvider = HTTPProvider(endpoint_uri=uri)

    def getProduct(self, chain: str) -> HTTPProvider:
        provider: HTTPProvider = self._products.get(chain)
        if not provider:
            raise ValueError(f'Set HTTP provider for {chain} blockchain')
        return provider


httpProviderFabric = HTTPProviderFabric()

httpProviderFabric.addProduct(chain='eth', uri=os.getenv('ETH_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain='bsc', uri=os.getenv('BSC_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain='avax', uri=os.getenv('AVAX_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain='arb', uri=os.getenv('ARB_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain='ftm', uri=os.getenv('FTM_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain='matic', uri=os.getenv('MATIC_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain='opt', uri=os.getenv('OPT_HTTP_PROVIDER', ''))
