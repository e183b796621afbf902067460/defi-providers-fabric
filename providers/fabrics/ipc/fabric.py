import os
from typing import Union
from pathlib import Path
from web3.providers.ipc import IPCProvider

from head.interfaces.fabrics.interface import IConcreteFabric


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

ipcProviderFabric.addProduct(chain='eth', path=os.getenv('ETH_IPC_PROVIDER', ''))
ipcProviderFabric.addProduct(chain='bsc', path=os.getenv('BSC_IPC_PROVIDER', ''))
ipcProviderFabric.addProduct(chain='avax', path=os.getenv('AVAX_IPC_PROVIDER', ''))
ipcProviderFabric.addProduct(chain='arb', path=os.getenv('ARB_IPC_PROVIDER', ''))
ipcProviderFabric.addProduct(chain='ftm', path=os.getenv('FTM_IPC_PROVIDER', ''))
ipcProviderFabric.addProduct(chain='matic', path=os.getenv('MATIC_IPC_PROVIDER', ''))
ipcProviderFabric.addProduct(chain='opt', path=os.getenv('OPT_IPC_PROVIDER', ''))
