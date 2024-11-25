# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np  
else:
    from . import nicePrints as np
    

# OTHER MODULES
import os
from datetime import datetime
# =============================================================================

# ottiene un timestamp del tipo dd-mm-yyyy_hh-mm-ss
def getTimeStamp_italian():
    currentDateTime = datetime.now()
    outStr = "{}-{}-{}_{}-{}-{}".format(
        currentDateTime.day,
        currentDateTime.month,
        currentDateTime.year,
        currentDateTime.hour,
        currentDateTime.minute,
        currentDateTime.second
    )
    return outStr



# iso8601 timestamp - yyyy-mm-dd_hh-mm-ss
def getTimeStamp_iso8601():
    currentDateTime = datetime.now()
    outStr = "{}-{}-{}_{}-{}-{}".format(
        currentDateTime.year,
        currentDateTime.month,
        currentDateTime.day,
        currentDateTime.hour,
        currentDateTime.minute,
        currentDateTime.second
    )
    return outStr