import os
from typing import Union
from pathlib import Path
from web3.providers.ipc import IPCProvider

from interfaces.fabrics.interface import IConcreteFabric
from orm.consts.chainName import ChainName


class IPCProviderFabric(IConcreteFabric):

    def addProduct(self, chain: str = None, path: Union[str, Path] = None) -> None:
        if not self._products.get(chain):
            self._products[chain]: IPCProvider = IPCProvider(ipc_path=path)

    def getProduct(self, chain: str = None) -> IPCProvider:
        provider: IPCProvider = self._products.get(chain)
        if not provider:
            raise ValueError(f'Set IPC provider for {chain} blockchain')
        return provider


IPCProviderFabric = IPCProviderFabric()

IPCProviderFabric.addProduct(chain=ChainName.ETH, path=os.getenv('ETH_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=ChainName.BSC, path=os.getenv('BSC_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=ChainName.AVAX, path=os.getenv('AVAX_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=ChainName.ARB, path=os.getenv('ARB_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=ChainName.FTM, path=os.getenv('FTM_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=ChainName.MATIC, path=os.getenv('MATIC_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=ChainName.OPT, path=os.getenv('OPT_IPC_PROVIDER', ''))
