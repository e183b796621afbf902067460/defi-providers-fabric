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


httpProviderFabric = HTTPProviderFabric()

httpProviderFabric.addProduct(chain=Chains.ETH, uri=os.getenv('ETH_HTTP_PROVIDER', 'https://mainnet.infura.io/v3/3c9943304cf64593a4013a87cc5fd3f5'))
httpProviderFabric.addProduct(chain=Chains.BSC, uri=os.getenv('BSC_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain=Chains.AVAX, uri=os.getenv('AVAX_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain=Chains.ARB, uri=os.getenv('ARB_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain=Chains.FTM, uri=os.getenv('FTM_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain=Chains.MATIC, uri=os.getenv('MATIC_HTTP_PROVIDER', ''))
httpProviderFabric.addProduct(chain=Chains.OPT, uri=os.getenv('OPT_HTTP_PROVIDER', ''))
