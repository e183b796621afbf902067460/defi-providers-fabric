from head.interfaces.abstracts.interface import IAbstractFabric
from head.interfaces.fabrics.interface import IConcreteFabric

from providers.fabrics.http.fabric import httpProviderFabric
from providers.fabrics.ipc.fabric import ipcProviderFabric
from providers.fabrics.websocket.fabric import wsProviderFabric
from providers.fabrics.scan.fabric import scanProviderFabric
from providers.fabrics.api.fabric import apiProviderFabric
from providers.fabrics.block.fabric import blockLimitProviderFabric


class ProviderAbstractFabric(IAbstractFabric):

    def addFabric(self, fabricType: str, fabric: IConcreteFabric) -> None:
        if not self._fabrics.get(fabricType):
            self._fabrics[fabricType]: IConcreteFabric = fabric

    def getFabric(self, fabricType: str) -> IConcreteFabric:
        fabric: IConcreteFabric = self._fabrics.get(fabricType)
        if not fabric:
            raise ValueError(f'Set Fabric for {fabricType} fabric type')
        return fabric


providerAbstractFabric = ProviderAbstractFabric()

providerAbstractFabric.addFabric(fabricType='http', fabric=httpProviderFabric)
providerAbstractFabric.addFabric(fabricType='ipc', fabric=ipcProviderFabric)
providerAbstractFabric.addFabric(fabricType='ws', fabric=wsProviderFabric)
providerAbstractFabric.addFabric(fabricType='scan', fabric=scanProviderFabric)
providerAbstractFabric.addFabric(fabricType='api', fabric=apiProviderFabric)
providerAbstractFabric.addFabric(fabricType='block', fabric=blockLimitProviderFabric)
