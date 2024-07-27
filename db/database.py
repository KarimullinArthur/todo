import os
import sys 

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import config


engine = create_engine(config.DSN, echo=False)


class Base(DeclarativeBase):
    pass
