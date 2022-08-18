from head.interfaces.abstracts.interface import IAbstractFabric
from head.interfaces.fabrics.interface import IConcreteFabric

from providers.fabrics.http.fabric import HTTPProviderFabric
from providers.fabrics.ipc.fabric import IPCProviderFabric
from providers.fabrics.websocket.fabric import WebsocketProviderFabric


class ProviderAbstractFabric(IAbstractFabric):

    def addFabric(self, fabricType: str, fabric: IConcreteFabric) -> None:
        if not self._fabrics.get(fabricType):
            self._fabrics[fabricType]: IConcreteFabric = fabric

    def getFabric(self, fabricType: str) -> IConcreteFabric:
        fabric: IConcreteFabric = self._fabrics.get(fabricType)
        if not fabric:
            raise ValueError(f'Set Fabric for {fabricType} fabric type')
        return fabric


ProviderAbstractFabric = ProviderAbstractFabric()

ProviderAbstractFabric.addFabric(fabricType='http', fabric=HTTPProviderFabric)
ProviderAbstractFabric.addFabric(fabricType='ipc', fabric=IPCProviderFabric)
ProviderAbstractFabric.addFabric(fabricType='ws', fabric=WebsocketProviderFabric)
