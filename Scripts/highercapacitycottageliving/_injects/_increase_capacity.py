from animation.animation_constants import CreatureType
from bluuberrylibrary.logs.bb_log_registry import BBLogRegistry
from bluuberrylibrary.utils.debug.bb_injection_utils import BBInjectionUtils
from highercapacitycottageliving.mod_identity import HCCLModIdentity
from objects.animals.animal_service import AnimalHomeData

log = BBLogRegistry().register_log(HCCLModIdentity(), 'hccl_increase_capacity')
log.enable()


@BBInjectionUtils.inject(HCCLModIdentity(), AnimalHomeData, '__init__')
def _hccl_increase_capacity(original, self, animal_home_id, max_occupancy, animal_types, *_, **__):
    log.debug('Got data', me=self, animal_home_id=animal_home_id, max_occupancy=max_occupancy, animal_types=animal_types, argles=_, kwargles=__)
    # {'argles': (557058352410132561,
    #             8,
    #             [ < CreatureType.Chick = 4176957319 >,
    #             < CreatureType.Hen = 915067390 >,
    #             < CreatureType.Rooster = 3987889111 >],
    #             True,
    #             None,
    #             745083558062066853,
    #             0),
    #  'kwargles': {},
    #  'me': < objects.animals.animal_service.AnimalHomeData object at 0x00007FF46290F5D0 >}
    max_occupancy = 200
    animal_types.append(CreatureType.Cow)
    return original(self, animal_home_id, max_occupancy, animal_types, *_, **__)
