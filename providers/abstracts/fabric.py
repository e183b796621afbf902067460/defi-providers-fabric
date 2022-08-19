from head.interfaces.abstracts.interface import IAbstractFabric
from head.interfaces.fabrics.interface import IConcreteFabric

from providers.fabrics.http.fabric import httpProviderFabric
from providers.fabrics.ipc.fabric import ipcProviderFabric
from providers.fabrics.websocket.fabric import wsProviderFabric


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
