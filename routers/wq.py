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
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import wq
from dependencies import get_db

router = APIRouter(prefix="/wq")


@router.get(
    "/arsenic",
)
def get_arsenic(pointid: str = None, db: Session = Depends(get_db)):
    return get_wq_table(wq.WQ_Arsenic, pointid, db)


@router.get(
    "/calcium",
)
def get_calcium(pointid: str = None, db: Session = Depends(get_db)):
    return get_wq_table(wq.WQ_Calcium, pointid, db)


def get_wq_table(tbl, pointid, db):
    q = db.query(tbl)
    if pointid:
        q = q.filter(tbl.POINT_ID == pointid)
    q = q.limit(10)
    return q.all()


# ============= EOF =============================================
