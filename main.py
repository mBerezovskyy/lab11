from model.hose import Hose
from model.watering_funnel import WateringFunnel
from model.watering_gun import WateringGun
from model.submersible_pump import SubmersiblePump
from model.surface_pump import SurfacePump

from manager.watering_manager_utils import WateringManagerUtils

if __name__ == '__main__':

    watering_manager_utils = WateringManagerUtils()

    hose = Hose()
    watering_funnel = WateringFunnel()
    watering_gun = WateringGun()
    submersible_pump = SubmersiblePump()
    surface_pump = SurfacePump()

    print(hose)
    print(watering_funnel)
    print(watering_gun)
    print(submersible_pump)
    print(surface_pump)

    print(watering_manager_utils.sort_tools_by_price(hose))
