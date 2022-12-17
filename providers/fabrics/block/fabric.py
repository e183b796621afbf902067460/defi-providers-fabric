from head.interfaces.fabrics.interface import IConcreteFabric


class BlockLimitProviderFabric(IConcreteFabric):

    def addProduct(self, chain: str, limit: int) -> None:
        if not self._products.get(chain):
            self._products[chain]: int = limit

    def getProduct(self, chain: str) -> int:
        limit: int = self._products.get(chain)
        if not limit:
            raise ValueError(f'Set Block limit for {chain} blockchain')
        return limit


blockLimitProviderFabric = BlockLimitProviderFabric()

blockLimitProviderFabric.addProduct(chain='bsc', limit=3000)
blockLimitProviderFabric.addProduct(chain='matic', limit=3000)
blockLimitProviderFabric.addProduct(chain='opt', limit=3000)
