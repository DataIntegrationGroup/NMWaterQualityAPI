# ===============================================================================
# Copyright 2024 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
from sqlalchemy import Column, Float, String, DateTime, Integer

from database import Base


class MasterUnionWaterQuality(Base):
    POINT_ID = Column(String(255))
    CollectionDate = Column(DateTime, primary_key=True)
    HistoricDate = Column(Integer)
    Arsenic = Column(Float)
    Arsenic_Symbol = Column(String(255))
    U = Column(Float)
    Uranium_Symbol = Column(String(255))
    F = Column(Float)
    F_Symbol = Column(String(255))
    TDS = Column(Float)
    TDS_Symbol = Column(String(255))
    CONDLAB = Column(Float)
    CONDLAB_Symbol = Column(String(255))
    Ca = Column(Float)
    Ca_Symbol = Column(String(255))
    Na = Column(Float)
    Na_Symbol = Column(String(255))
    Mg = Column(Float)
    Mg_Symbol = Column(String(255))
    HCO3 = Column(Float)
    HCO3_Symbol = Column(String(255))
    Cl = Column(Float)
    Cl_Symbol = Column(String(255))
    SO4 = Column(Float)
    SO4_Symbol = Column(String(255))
    Latitude = Column(Float)
    Longitude = Column(Float)
    WellDepth = Column(Float)
    DataSource = Column(String(255))
    DataSourceInfo = Column(String(255))
# ============= EOF =============================================
