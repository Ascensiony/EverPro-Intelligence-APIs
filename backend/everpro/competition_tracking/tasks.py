from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

import json
import time

from .api.competition_track import amazon_track_competition

logger = get_task_logger(__name__)


def load():
    with open(
        "./competition_tracking/api/competition_tracker.json", "r", encoding="utf-8"
    ) as f:
        return json.load(f)


def write(db):
    with open(
        "./competition_tracking/api/competition_tracker.json", "w", encoding="utf-8"
    ) as f:
        json.dump(db, f, ensure_ascii=False, indent=4)


def periodic_update_competition_track_data():
    try:
        db = list(load())

        for index, data in enumerate(db):
            del db[index]
            db.insert(index, amazon_track_competition(data["asin"], data["zone"]))
            time.sleep(100)

        write(db)

    except Exception as e:
        print(e)
        print("ERROR!!! in periodic update, check it out!")


@periodic_task(
    run_every=(crontab(minute="*/10")),
    name="task_update_competitiontrack_db",
    ignore_result=True,
)
def task_update_competitiontrack_db():
    """
    Updates the competition Tracking Database
    """
    periodic_update_competition_track_data()
    logger.info("Upadated competition Tracking Database")