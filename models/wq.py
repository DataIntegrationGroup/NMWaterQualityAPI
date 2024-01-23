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


class WQMixin:
    POINT_ID = Column(String(50))
    CollectionDate = Column(DateTime, primary_key=True)
    HistoricDate = Column(Integer)
    Latitude = Column(Float)
    Longitude = Column(Float)
    WellDepth = Column(Float)
    DataSource = Column(String(50))
    DataSourceInfo = Column(String(100))


class WQ_Arsenic(Base, WQMixin):
    __tablename__ = "WQ_Arsenic"
    Arsenic = Column(Float)
    Arsenic_Symbol = Column(String(255))


class WQ_Calcium(Base, WQMixin):
    __tablename__ = "WQ_Calcium"
    Calcium = Column(Float)
    Calcium_Symbol = Column(String(255))


class WQ_Chlorine(Base, WQMixin):
    __tablename__ = "WQ_Chlorine"
    Chlorine = Column(Float)
    Chlorine_Symbol = Column(String(255))


class WQ_Fluoride(Base, WQMixin):
    __tablename__ = "WQ_Fluoride"
    Fluoride = Column(Float)
    Fluoride_Symbol = Column(String(255))


class WQ_Magnesium(Base, WQMixin):
    __tablename__ = "WQ_Magnesium"
    Magnesium = Column(Float)
    Magnesium_Symbol = Column(String(255))


class WQ_Sodium(Base, WQMixin):
    __tablename__ = "WQ_Sodium"
    Sodium = Column(Float)
    Sodium_Symbol = Column(String(255))


class WQ_Sulfate(Base, WQMixin):
    __tablename__ = "WQ_Sulfate"
    Sulfate = Column(Float)
    Sulfate_Symbol = Column(String(255))


class WQ_TDS(Base, WQMixin):
    __tablename__ = "WQ_TDS"
    TDS = Column(Float)
    TDS_Symbol = Column(String(255))


class WQ_Uranium(Base, WQMixin):
    __tablename__ = "WQ_Uranium"
    Uranium = Column(Float)
    Uranium_Symbol = Column(String(255))
# ============= EOF =============================================
