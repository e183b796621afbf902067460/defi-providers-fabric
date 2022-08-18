import os
from web3.providers.rpc import HTTPProvider

from head.interfaces.fabrics.interface import IConcreteFabric
from head.consts.chains.const import Chains


class HTTPProviderFabric(IConcreteFabric):

    def addProduct(self, chain: str, uri: str) -> None:
        if not self._products.get(chain):
            self._products[chain]: HTTPProvider = HTTPProvider(endpoint_uri=uri)

    def getProduct(self, chain: str) -> HTTPProvider:
        provider: HTTPProvider = self._products.get(chain)
        if not provider:
            raise ValueError(f'Set HTTP provider for {chain} blockchain')
        return provider


HTTPProviderFabric = HTTPProviderFabric()

HTTPProviderFabric.addProduct(chain=Chains.ETH, uri=os.getenv('ETH_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=Chains.BSC, uri=os.getenv('BSC_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=Chains.AVAX, uri=os.getenv('AVAX_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=Chains.ARB, uri=os.getenv('ARB_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=Chains.FTM, uri=os.getenv('FTM_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=Chains.MATIC, uri=os.getenv('MATIC_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=Chains.OPT, uri=os.getenv('OPT_HTTP_PROVIDER', ''))
