from drizzlepac.astrodrizzle import AstroDrizzle
from stsci.tools import teal

from tests import DATA_DIRECTORY


def test_drizzlepac():
    inputs = [
        str(DATA_DIRECTORY / "j94f05bgq_flt.fits"),
        str(DATA_DIRECTORY / "j9irw1rqq_flt.fits"),
    ]

    adriz_parObj = teal.load("astrodrizzle", defaults=True)

    adriz_parObj["output"] = "acs_tweak"
    adriz_parObj["build"] = True
    adriz_parObj["in_memory"] = True
    adriz_parObj["runfile"] = "drizzlepac.run"

    adriz_parObj["STATE OF INPUT FILES"]["preserve"] = False
    adriz_parObj["STATE OF INPUT FILES"]["clean"] = True

    adriz_parObj["STEP 2: SKY SUBTRACTION"]["skywidth"] = 0.3
    adriz_parObj["STEP 2: SKY SUBTRACTION"]["use_static"] = False
    adriz_parObj["STEP 2: SKY SUBTRACTION"]["sky_bits"] = None
    adriz_parObj["STEP 4: CREATE MEDIAN IMAGE"]["combine_maskpt"] = 0.7

    AstroDrizzle(inputs, configobj=adriz_parObj)
