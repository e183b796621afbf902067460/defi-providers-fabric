import os
from typing import Union
from pathlib import Path
from web3.providers.ipc import IPCProvider

from head.interfaces.fabrics.interface import IConcreteFabric
from head.consts.chains.const import Chains


class IPCProviderFabric(IConcreteFabric):

    def addProduct(self, chain: str, path: Union[str, Path]) -> None:
        if not self._products.get(chain):
            self._products[chain]: IPCProvider = IPCProvider(ipc_path=path)

    def getProduct(self, chain: str) -> IPCProvider:
        provider: IPCProvider = self._products.get(chain)
        if not provider:
            raise ValueError(f'Set IPC provider for {chain} blockchain')
        return provider


ipcProviderFabric = IPCProviderFabric()

IPCProviderFabric.addProduct(chain=Chains.ETH, path=os.getenv('ETH_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=Chains.BSC, path=os.getenv('BSC_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=Chains.AVAX, path=os.getenv('AVAX_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=Chains.ARB, path=os.getenv('ARB_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=Chains.FTM, path=os.getenv('FTM_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=Chains.MATIC, path=os.getenv('MATIC_IPC_PROVIDER', ''))
IPCProviderFabric.addProduct(chain=Chains.OPT, path=os.getenv('OPT_IPC_PROVIDER', ''))
