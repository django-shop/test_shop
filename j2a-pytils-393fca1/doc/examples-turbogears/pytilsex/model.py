from sqlobject import *

from turbogears.database import PackageHub

hub = PackageHub("pytilsex")
__connection__ = hub

# class YourDataClass(SQLObject):
#     pass

