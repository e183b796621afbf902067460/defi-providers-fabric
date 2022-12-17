import os

from head.interfaces.fabrics.interface import IConcreteFabric


class APIProviderFabric(IConcreteFabric):

    def addProduct(self, chain: str, key: str) -> None:
        if not self._products.get(chain):
            self._products[chain]: str = key

    def getProduct(self, chain: str) -> str:
        key: str = self._products.get(chain)
        if not key:
            raise ValueError(f'Set Scan API provider for {chain} blockchain')
        return key


apiProviderFabric = APIProviderFabric()

apiProviderFabric.addProduct(chain='eth', key=os.getenv('ETH_SCAN_API_KEY', ''))
apiProviderFabric.addProduct(chain='bsc', key=os.getenv('BSC_SCAN_API_KEY', ''))
apiProviderFabric.addProduct(chain='avax', key=os.getenv('AVAX_SCAN_API_KEY', ''))
apiProviderFabric.addProduct(chain='arb', key=os.getenv('ARB_SCAN_API_KEY', ''))
apiProviderFabric.addProduct(chain='ftm', key=os.getenv('FTM_SCAN_API_KEY', ''))
apiProviderFabric.addProduct(chain='matic', key=os.getenv('MATIC_SCAN_API_KEY', ''))
apiProviderFabric.addProduct(chain='opt', key=os.getenv('OPT_SCAN_API_KEY', ''))
