import os
from web3.providers.rpc import HTTPProvider

from interfaces.fabrics.interface import IConcreteFabric
from orm.consts.chainName import ChainName


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

HTTPProviderFabric.addProduct(chain=ChainName.ETH, uri=os.getenv('ETH_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=ChainName.BSC, uri=os.getenv('BSC_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=ChainName.AVAX, uri=os.getenv('AVAX_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=ChainName.ARB, uri=os.getenv('ARB_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=ChainName.FTM, uri=os.getenv('FTM_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=ChainName.MATIC, uri=os.getenv('MATIC_HTTP_PROVIDER', ''))
HTTPProviderFabric.addProduct(chain=ChainName.OPT, uri=os.getenv('OPT_HTTP_PROVIDER', ''))
