import os

from head.interfaces.fabrics.interface import IConcreteFabric


class ScanProviderFabric(IConcreteFabric):

    def addProduct(self, chain: str, uri: str) -> None:
        if not self._products.get(chain):
            self._products[chain]: str = uri

    def getProduct(self, chain: str) -> str:
        scan: str = self._products.get(chain)
        if not scan:
            raise ValueError(f'Set Scan URL provider for {chain} blockchain')
        return scan


scanProviderFabric = ScanProviderFabric()

scanProviderFabric.addProduct(chain='eth', uri=os.getenv('ETH_SCAN_API_URL', ''))
scanProviderFabric.addProduct(chain='bsc', uri=os.getenv('BSC_SCAN_API_URL', ''))
scanProviderFabric.addProduct(chain='avax', uri=os.getenv('AVAX_SCAN_API_URL', ''))
scanProviderFabric.addProduct(chain='arb', uri=os.getenv('ARB_SCAN_API_URL', ''))
scanProviderFabric.addProduct(chain='ftm', uri=os.getenv('FTM_SCAN_API_URL', ''))
scanProviderFabric.addProduct(chain='matic', uri=os.getenv('MATIC_SCAN_API_URL', ''))
scanProviderFabric.addProduct(chain='opt', uri=os.getenv('OPT_SCAN_API_URL', ''))
